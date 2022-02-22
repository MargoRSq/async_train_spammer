import datetime

from vkbottle.bot import Blueprint, Bot, rules, Message
from db.models import WeekType

from utils.config import TOKEN, GROUP_ID
from utils.timetable_utils import get_weekday
from utils.timetable_parser import get_new_timetable
from utils.timetable import get_day_timetable, get_week_rasp


bp = Blueprint()



@bp.on.message(rules.CommandRule("чет", ["!", "/"]))
async def today(m: Message) -> str:
    await m.answer(get_week_rasp(0))

@bp.on.message(rules.CommandRule("нечет", ["!", "/"]))
async def today(m: Message) -> str:
    await m.answer(get_week_rasp(1))

@bp.on.message(rules.CommandRule("р", ["!", "/"]))
async def today(m: Message) -> str:
    await m.answer(get_week_rasp())

@bp.on.message(rules.CommandRule("сегодня", ["!", "/"]))
async def today(m: Message) -> str:
    await m.answer(get_day_timetable(get_weekday()))

@bp.on.message(rules.CommandRule("завтра", ["!", "/"]))
async def tomorrow(m: Message) -> str:
    week_day = get_weekday()
    if week_day in [5, 6]:
        text = "Вывожу расписание на понедельник"
        text += get_day_timetable(0)
    else:
        text = get_day_timetable(week_day + 1)
    await m.answer(text)

@bp.on.message(rules.CommandRule("нрасп", ["!", "/"]))
async def upload_new_rasp(m: Message) -> str:
    url = m.attachments[0].doc.url
    text = "Done" if get_new_timetable(url) else "Some error happend"
    await m.answer(text)
