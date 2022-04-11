import requests
from typing import Tuple

from io import BytesIO
from vkbottle.bot import Blueprint, rules, Message
from vkbottle.dispatch.rules.bot import DEFAULT_PREFIXES
from vkbottle import PhotoMessageUploader

from utils.config import tokens, bot

bp = Blueprint()

@bp.on.message(rules.CommandRule("лайки", DEFAULT_PREFIXES, 2))
async def today(m: Message, args: Tuple[str]) -> str:
    if m.chat_id in [1, 7, 8]:
        try:
            token = tokens[args[0]]
            count = await get_likes_count(token)
            await m.answer(f'работаю друк, тебя лайкнуло {count} девачек и мальчиков')
            photos = await get_likes(token, int(args[1]))
            for girl in photos:
                await m.answer('оп', attachment=girl)
        except BaseException as e:
            await m.answer(e)

async def get_likes_count(token: str):
    headers = {"x-auth-token": token}
    r = requests.get("https://api.gotinder.com/v2/fast-match/count", headers=headers)
    data_json = r.json()
    return data_json['data']['count']


async def get_likes(token: str, amount: int = 10):
    headers = {"x-auth-token": token}
    r = requests.get("https://api.gotinder.com/v2/fast-match/teasers", headers=headers)
    data_json = r.json()

    # names = []
    # for g_id in ids:
    #     names.append(rg)

    # 
    # data_json['data']['results'][0]['user']
    # ids =  [girl['user']['photos'] for girl in data_json['data']['results']]

    ids = [girl['user']['_id'] for girl in data_json['data']['results']]
    photos = [girl['user']['photos'] for girl in data_json['data']['results']]
    atchs = []
    for i, ph in enumerate(photos):
        amount -= 1
        rl = requests.get(f"https://api.gotinder.com/like/{ids[i]}", headers=headers)
        girl_image = requests.get(ph[0]['url']).content
        img = BytesIO(girl_image)
        photo = await PhotoMessageUploader(bot.api).upload(img)
        atchs.append(photo)
        if not amount:
            break
    return atchs
