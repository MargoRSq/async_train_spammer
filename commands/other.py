import json
import requests

from vkbottle.bot import Blueprint, rules, Message
from vkbottle.dispatch.rules.bot import DEFAULT_PREFIXES

from db.other_opeations import get_roster, push_roster

bp = Blueprint()

@bp.on.message(rules.CommandRule("нсписок", DEFAULT_PREFIXES))
async def today(m: Message) -> str:
    url = m.attachments[0].__dict__['doc'].__dict__['url']
    response = requests.get(url)
    parsed = json.loads(response.content)['data']
    push_roster(parsed)
    await m.answer('доне(дюна)')

@bp.on.message(rules.CommandRule("список", DEFAULT_PREFIXES))
async def today(m: Message) -> str:
    lst = get_roster()
    text = ''
    for i, item in enumerate(lst):
        text += f'{i + 1}. {item[0]}\n'
    await m.answer(text)
