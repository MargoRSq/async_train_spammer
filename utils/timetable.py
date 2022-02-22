from utils.timetable_utils import (get_week_num,
                                   get_day_range,
                                   ch, nech, days, time)
from utils.config import PLACES_EVEN, PLACES_ODD

def get_day_timetable(day: int):
    week_number = get_week_num()
    week_type = week_number % 2
    week_timetable = nech if week_type == 1 else ch
    none_counter = 0
    places = PLACES_ODD if week_type == 1 else PLACES_EVEN

    day_range = get_day_range(str(day))
    text = days[day] + f"({places[day - 1]})" + ' - '
    text += f'Четная неделя ({week_number})' if week_number != 0 \
                                                   else f'Нечетная неделя ({week_number})'
    text += '\n'
    for class_num in range(day_range - 5, day_range):
        class_name = week_timetable[class_num][0]
        if not class_name:
            none_counter += 1
        else:
            text += f"|{time[class_num % 5]}| {class_name} \n"
    if none_counter == 5:
        text += 'В этот день пар нет!'
    return text

def get_week_rasp(week_number=get_week_num()):
    week_timetable = nech if week_number % 2 == 1 else ch
    none_counter = 0

    text = f'Четная неделя ({week_number})' if week_number != 0 \
                                                   else f'Нечетная неделя ({week_number})'
    text += '\n'
    for class_num in range(0, 30):
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