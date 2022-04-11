from typing import Tuple
from vkbottle.bot import Blueprint, rules, Message
from vkbottle.dispatch.rules.bot import DEFAULT_PREFIXES

from utils.config import WEEKS_NUM
from utils.timetable_utils import get_weekday, get_week_num
from utils.timetable_parser import get_new_timetable
from utils.timetable import get_day_timetable, get_range_rasp, get_weekday_rasp


bp = Blueprint()

@bp.on.message(rules.CommandRule("чет", DEFAULT_PREFIXES))
async def today(m: Message) -> str:
    await m.answer(get_range_rasp(0))

@bp.on.message(rules.CommandRule("нечет", DEFAULT_PREFIXES))
async def today(m: Message) -> str:
    await m.answer(get_range_rasp(1))

@bp.on.message(rules.CommandRule("р", DEFAULT_PREFIXES))
async def today(m: Message) -> str:
    await m.answer(get_range_rasp(get_week_num()))

@bp.on.message(rules.CommandRule("р", DEFAULT_PREFIXES, 1))
async def today(m: Message, args: Tuple[str]) -> str:
    await m.answer(get_weekday_rasp(args[0]))

@bp.on.message(rules.CommandRule("сегодня", DEFAULT_PREFIXES))
async def today(m: Message) -> str:
    weekday = get_weekday()
    if weekday != 6:
        timetable = get_day_timetable(weekday)
        await m.answer(timetable)

@bp.on.message(rules.CommandRule("завтра", DEFAULT_PREFIXES))
async def tomorrow(m: Message) -> str:
    weekday = get_weekday() + 1
    if weekday == 6:
        weeknum =  get_week_num() + 1
        timetable = get_day_timetable(0, weeknum)
    else:
        timetable = get_day_timetable(weekday)
        await m.answer(timetable)

@bp.on.message(rules.CommandRule("нрасп", DEFAULT_PREFIXES))
async def upload_new_rasp(m: Message) -> str:
    url = m.attachments[0].doc.url
    text = "Done" if get_new_timetable(url) else "Some error happend"
    await m.answer(text)

@bp.on.message(rules.CommandRule("неделя", DEFAULT_PREFIXES))
async def tomorrow(m: Message) -> str:
    wn = get_week_num()
    ch = 'Че' if wn % 2 == 0 else 'Нече'
    text = f'({wn}){ch}тная неделя! Осталось: {WEEKS_NUM - wn}!\n['
    for _ in range(wn):
        text += '💩'
    for _ in range(WEEKS_NUM - wn):
        text += '😢'
    text += ']'
    await m.answer(text)
