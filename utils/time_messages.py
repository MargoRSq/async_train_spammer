import asyncio
import aioschedule as schedule
import requests
import time

from threading import Thread
from io import BytesIO

from vkbottle import PhotoMessageUploader
from vkbottle.bot import Bot

from utils.timetable_utils import get_valid_weekday, get_week_num, get_weekday
from utils.timetable import get_day_timetable
from utils.config import (TOKEN, CAT_TOKEN, CHAT_ID,
                          MONDAY,
                          TUESDAY,
                          WEDNESDAY,
                          THURSDAY,
                          FRIDAY,
                          SATURDAY)

bot = Bot(TOKEN)

def select_pivoday():
    match get_weekday():
        case 0:
            return MONDAY
        case 1:
            return TUESDAY
        case 2:
            return WEDNESDAY
        case 3:
            return THURSDAY
        case 4:
            return FRIDAY
        case 5:
            return SATURDAY

async def good_night():
    weekday = get_valid_weekday(get_weekday())
    if weekday != 5:
        headers = {"x-api-key": CAT_TOKEN}
        cat_image_url = requests.get(url="https://api.thecatapi.com/v1/images/search", headers=headers).json()[0]['url']
        cat_image = requests.get(cat_image_url).content
        img = BytesIO(cat_image)
        photo = await PhotoMessageUploader(bot.api).upload(img)
        if weekday == 6:
            weeknum =  get_week_num()
            weeknum = 1 - weeknum
            timetable = get_day_timetable(weekday, weeknum)
        else:
            timetable = get_day_timetable(weekday)
        text = f'Спокойной ночи, малыши:3\nРасписание на завтра:\n{timetable}'
        await bot.api.messages.send(chat_id=CHAT_ID, message=text, random_id=0, attachment=photo)

async def good_morning():
    weekday = get_weekday()
    if weekday != 6:
        timetable = get_day_timetable(weekday)
        await bot.api.messages.send(
            message = f'Доброе утро, пупсики, воть расписание на сегодня :3\n{timetable}',
            attachment=select_pivoday(),
            chat_id=CHAT_ID,
            random_id=0)

def do_schedule():
    schedule.every().day.at("09:00").do(good_morning)
    schedule.every().day.at("23:30").do(good_night)
    loop = asyncio.new_event_loop()
    while True:
        loop.run_until_complete(schedule.run_pending())
        time.sleep(0.1)

def time_loop():
    thread = Thread(target=do_schedule)
    thread.start()