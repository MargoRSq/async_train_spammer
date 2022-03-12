from vkbottle.bot import Blueprint, Message
from utils.config import bot

bp = Blueprint()

triggers_array = ["@all", "@margosq", "zoom", "lms", "mtuci"]

check_phrase = lambda m: True if any(trg in m for trg in triggers_array) else False

@bp.on.message(func=lambda message: check_phrase(message.text.lower()))
async def today(m: Message) -> str:
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
    await m.answer(text, user_id=423750235)
