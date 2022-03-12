from typing import Tuple
from vkbottle.bot import Blueprint, rules, Message, Bot
from vkbottle.dispatch.rules.bot import DEFAULT_PREFIXES
from vkbottle import DocMessagesUploader

from utils.config import TOKEN
from utils.pres_parser import svg2pdf

bot = Bot(TOKEN)
bp = Blueprint()

@bp.on.message(rules.CommandRule("преза", DEFAULT_PREFIXES, 2))
async def today(m: Message, args: Tuple[str]) -> str:
    await m.answer('Начинаю спецоперацию по захвату презы')
    try:
        url = args[0]
        filename = args[1]
        pdf = await svg2pdf(url)
        pdf_bytes = pdf[0]
        doc = await DocMessagesUploader(bot.api).upload(f"{filename}.pdf", pdf_bytes, peer_id=m.peer_id)
        text = f'Slides: {pdf[2]}, seconds: {int(pdf[1])}'
        await m.answer(text, attachment=doc)
    except BaseException as e:
        await m.answer(f'Что-то явно пошло не так:\n({e})')
