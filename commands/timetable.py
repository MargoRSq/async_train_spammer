
from vkbottle.bot import Blueprint, Bot, rules, Message
from db.models import WeekType

from utils.config import TOKEN, GROUP_ID


bp = Blueprint()



@bp.on.message(rules.CommandRule("сегодня", ["!", "/"]))
async def hello(m: Message) -> str:
    await m.answer(get_day_raps(1, 'вт'))

@bp.on.message(rules.CommandRule("нрасп", ["!", "/"]))
async def upload_new_rasp(m: Message) -> str:
    url = m.attachments[0].doc.url
    return



spaces = '&#4448;&#4448;&#4448;&#4448;&#4448;'
long_lines = '---------------------'
short_lines = '--------'
days = ['Понедельник (ОП)',
        'Вторник (Мотор)',
        'Среда (Мотор)',
        'Четверг (ОП)',
        'Пятница (ОП)',
        'Суббота']

days_with_spaces = [f'{short_lines}{day}{short_lines}' for day in days]
time = ['| 09:30-11:05 |', '| 11:20-12:55 |', '| 13:10-14:45 |', '| 15:25-17:00 |', '| 17:15-18:50 |']


# async def timetable(vk, event, message, params):
#     message = event['object']['message']['text'].lower()
#         message_array = message.split(' ')
#         delta = delta_func()

#         nech = await simple_select(select_what=['para'], select_from='rasp', where="week = 'неч'", to_list=True)
#         ch = await simple_select(select_what=['para'], select_from='rasp', where="week = 'чет'", to_list=True)
        
#         week_type = {'чет': ch, 'нечет': nech}

#         try:
#             if len(message_array) == 1:
#                 rasp = ch if (delta // 7) % 2 != 0 else nech
#                 day = []
#                 for r in range(0, 30):
#                     day.append(rasp[r])
                
#                 text = rasp_with_time(day, 6)
#                 await async_send_message(vk, event, text)
#                 return True

#             elif len(message_array) == 2:
#                 arg = message_array[1]
#                 if arg in week_day:
                    
#                     day = []
#                     rasp = ch if (delta // 7) % 2 != 0 else nech
#                     for r in week_day[arg]:
#                         day.append(rasp[r])
                    
#                     text = rasp_with_time(day, 1)
#                     await async_send_message(vk, event, text)
#                     return True

#                 elif arg in week_type:
#                     rasp = week_type[arg]
                    
#                     day = []
#                     for r in range(0, 30):
#                         day.append(rasp[r])
                    
#                     text = rasp_with_time(day, 6, nofw=False)
#                     await async_send_message(vk, event, text)
#                     return True
            
#             elif len(message_array) == 3:
#                 day_of_the_week = message_array[1]
#                 type_of_the_week = message_array[2]
#                 rasp = week_type[type_of_the_week]
                
#                 day = []
#                 for r in week_day[day_of_the_week]:
#                     day.append(rasp[r])
#                 text = f'{day_of_the_week.capitalize()} | {type_of_the_week.capitalize()}ная неделя\n{rasp_with_time(day, 1, nofw=False)}'
#                 await async_send_message(vk, event, text)
#                 return True 
#         except KeyError:
#             text = 'Ты точно ввел чето не так дружок'
#             await async_send_message(vk, event, text) 
#             return True   
#         except BaseException as e:
#             print(e) 
#             text = 'Какая-то ошибка у меня'
#             await async_send_message(vk, event, text) 
#             return True


# def rasp_with_time(pr, mn, nofw=True):
    
#     if nofw:
#         delta = delta_func()
#         week_number = (delta // 7) + 1
#         week = f'Четная неделя ({week_number})' if (delta // 7) % 2 != 0 else f'Нечетная неделя ({week_number})'
        
#         text = f'{week}\n'
#     else:
#         text = ''

#     for i, item in enumerate(time * mn):
#         if i % 5 == 0 and mn > 1:
#             text = text + days_with_spaces[i//5] + '\n'
#         if pr[i] != None:
#             text = text + str(item) + ' ' + pr[i] + '\n'
#     return text



# def delta_func():
#     first_day = date(2021, 8, 30)
#     today = date.today()
#     delta = (today - first_day).days

#     return delta
