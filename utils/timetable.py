from db.timetable_operations import get_rasp
from utils.timetable_utils import (get_week_num,
                                   get_day_range,
                                   days, time)
from utils.config import PLACES_EVEN, PLACES_ODD

def get_day_timetable(day: int):
    rasp = get_rasp()
    ch, nech = rasp['ch'], rasp['nech']
    week_number = get_week_num()
    week_type = week_number % 2
    week_timetable = nech if week_type == 1 else ch
    if (len(week_timetable) < 30):
        return "Во мне нет расписания!"
    none_counter = 0
    places = PLACES_ODD if week_type == 1 else PLACES_EVEN

    day_range = get_day_range(str(day + 1))
    text = days[day] + f" ({places[day - 1]})" + ' - '
    text += f'Четная неделя ({week_number})' if week_number != 0 \
                                                   else f'Нечетная неделя ({week_number})'
    text += '\n'
    for class_num in day_range:
        class_name = week_timetable[class_num][0]
        if not class_name:
            none_counter += 1
        else:
            text += f"|{time[class_num % 5]}| {class_name} \n"
    if none_counter == 5:
        text += 'В этот день пар нет!'
    return text

def get_range_rasp(week_number=get_week_num(), rng=range(0, 30)):
    rasp = get_rasp()
    ch, nech = rasp['ch'], rasp['nech']
    week_timetable = nech if week_number % 2 == 1 else ch
    none_counter = 0

    text = f'Четная неделя ({week_number})' if week_number != 0 \
                                                   else f'Нечетная неделя ({week_number})'
    text += '\n'
    for class_num in rng:
        text += days[class_num // 5] + '\n' if class_num % 5 == 0 else ''
        none_counter = 0 if class_num % 5 == 0 else none_counter
        class_name = week_timetable[class_num][0]
        if not class_name:
            none_counter += 1
        else:
            text += f"|{time[class_num % 5]}| {class_name} \n"
        if none_counter == 5:
            text += 'В этот день пар нет!' + '\n'
            none_counter = 0
    return text

def get_weekday_rasp(day: str, week_number: int = get_week_num()):
    rng = get_day_range(day)
    if rng:
        return get_range_rasp(rng=rng, week_number=week_number)
    else:
        return "Не нашел такого дня недели"