from typing import Tuple
from vkbottle.bot import Blueprint, Bot, rules, Message

from utils.config import TOKEN, GROUP_ID

bp = Blueprint()

@bp.on.message(rules.CommandRule("say", ["!", "/"]))
async def hello(m: Message) -> str:
    await m.answer("HELLO")

