import json
import requests

from typing import Tuple

from vkbottle.bot import Blueprint, rules, Message
from vkbottle.dispatch.rules.bot import DEFAULT_PREFIXES

from db.other_opeations import get_roster, push_roster
from utils.help_parser import get_full_help, get_cmd_help

bp = Blueprint()

@bp.on.message(rules.CommandRule("нсписок", DEFAULT_PREFIXES))
async def today(m: Message) -> str:
    try:
        url = m.attachments[0].__dict__['doc'].__dict__['url']
        response = requests.get(url)
        parsed = json.loads(response.content)['data']
        push_roster(parsed)
        await m.answer('доне(дюна)')
    except BaseException as e:
        await m.answer(f'Что-то ты сделал не так, друк\n{e}')

@bp.on.message(rules.CommandRule("список", DEFAULT_PREFIXES))
async def today(m: Message) -> str:
    lst = get_roster()
    if not lst:
        return await m.answer("Во мне нет списка, загрузите .json в меня!")
    text = ''
    for i, item in enumerate(lst):
        text += f'{i + 1}. {item[0]}\n'
    await m.answer(text)

@bp.on.message(rules.CommandRule("помощь", DEFAULT_PREFIXES))
async def today(m: Message) -> str:
    await m.answer(get_full_help())

@bp.on.message(rules.CommandRule("помощь", DEFAULT_PREFIXES, 1))
async def today(m: Message, args: Tuple[str]) -> str:
    await m.answer(get_cmd_help(args[0]))
