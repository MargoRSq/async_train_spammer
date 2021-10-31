import enum
import io
import requests
import openpyxl

from datetime import date
from typing import Tuple, Union

from db.operations import get_rasp, post_rasp

rasp = get_rasp()
ch = rasp['ch']
nech = rasp['nech']


async def get_new_timetable(url) -> True | False:
    try:
        resp = requests.get(url)
        bytes = io.BytesIO(resp.read())
        new_timatable = parse_rasp(bytes)
        post_rasp(nech=new_timatable[0], ch=new_timatable[1])
        return True
    except:
        return False


def parse_rasp(file):
    ps = openpyxl.reader.excel.load_workbook(file)
    sheet = ps['Лист1']

    pr_numbers = [3 * i for i in range(1, 31)]
    ch_array = []
    nech_array = []
    for number in pr_numbers:
        nech_array.append(sheet[f'C{number}'].value)
        ch_array.append(sheet[f'D{number}'].value)

    return [nech_array, ch_array]


def get_day_raps(week: 1|0, day: str):
    week_timetable = nech if week == 1 else ch

    day_range = get_day_range(day)
    text = ''
    for class_name in range(day_range - 5, day_range):
        text += f"{week_timetable[class_name]}\n"

    return text

def get_day_range(day: str):
    match day:
        case 'понедельник' | '1' | 'пон':
            return 5
        case 'вторник' | '2' | 'вт':
            return 10
        case 'среда' | '3' | 'ср':
            return 15
        case 'четверг' | '4' | 'чт':
            return 20
        case 'пятница' | '5' | 'пт':
            return 25
        case 'суббота' | '6' | 'суб':
            return 30
        case _:
            return 0

def get_week_num():
    first_day = date(2021, 8, 30)
    today = date.today()
    delta = (today - first_day).days
    week_number = (delta // 7) + 1
    return week_number
