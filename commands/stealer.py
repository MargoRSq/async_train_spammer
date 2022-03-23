from vkbottle.bot import Blueprint, Message, rules
from utils.config import bot

from vkbottle_types.objects import BaseLink
from utils.config import MYUSER_ID

from enum import Enum

class MsgType(Enum):
    FWD = 1
    REPLY = 2

bp = Blueprint()

triggers_array = ["@all", "@margosq", "zoom", "lms", "mtuci", "нрасп"]
check_phrase = lambda m: True if any(trg in m for trg in triggers_array) else False

@bp.on.message(func=lambda message: check_phrase(message.text.lower()))
async def lul(m: Message) -> str:
    await send_to_bigbrother(m, m)

@bp.on.message(rules.ForwardMessagesRule())
async def lul_fwd(m: Message) -> str:
    wtr_m = m
    while (m.fwd_messages):
        m = m.fwd_messages[0]
    if (check_phrase(m.text.lower())):
        await send_to_bigbrother(m, wtr_m)
    if (m.attachments):
        if (m.attachments[0].link):
            await send_if_link(m, wtr_m, MsgType.FWD.value)

@bp.on.message(rules.ReplyMessageRule())
async def lul_reply(m: Message) -> str:
    wtr_m = m
    if (check_phrase(wtr_m.reply_message.text.lower())):
        await send_to_bigbrother(m, wtr_m)
    if (wtr_m.reply_message.attachments):
        if (wtr_m.reply_message.attachments):
            await send_if_link(m, wtr_m, MsgType.REPLY.value)

@bp.on.message(rules.AttachmentTypeRule(attachment_types='link'))
async def lul(m: Message) -> str:
    if (check_phrase(m.text.lower())):
        await send_to_bigbrother(m, m)
    if (m.attachments[0].link):
       await send_if_link(m, m, MsgType.FWD.value)

async def send_if_link(m: Message, wtr: Message, tp: MsgType):
    if tp == MsgType.FWD.value:
        link = m.attachments[0].link.url
    else:
        link = wtr.reply_message.attachments[0].link.url
    if (check_phrase(link)):
        return await wtr.answer(link, user_id=MYUSER_ID)

async def send_to_bigbrother(m: Message, wtr: Message):
    who = await bot.api.users.get(m.from_id)
    d = who[0].__dict__
    text = m.text + f"\n от {d['first_name']} {d['last_name']}"
    count = 0
    if m.attachments:
        for at in m.attachments:
            for tp in at:
                if tp[1]:
                    count+=1
    text += '\n' + f'attachments: {count}'
    await wtr.answer(text, user_id=MYUSER_ID)
