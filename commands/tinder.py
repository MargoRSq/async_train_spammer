import requests
from typing import Tuple

from io import BytesIO
from vkbottle.bot import Blueprint, rules, Message
from vkbottle.dispatch.rules.bot import DEFAULT_PREFIXES
from vkbottle import PhotoMessageUploader

from utils.config import TINDER_TOKEN_SVYAT, TINDER_TOKEN_DANYA, TINDER_TOKEN_ILYA, TINDER_TOKEN_VITYA,  bot

bp = Blueprint()


tokens = {
    'киев': TINDER_TOKEN_DANYA ,
    'свят': TINDER_TOKEN_SVYAT ,
    'илюха': TINDER_TOKEN_ILYA ,
    'ветя' : TINDER_TOKEN_VITYA
}

@bp.on.message(rules.CommandRule("лайки", DEFAULT_PREFIXES, 2))
async def today(m: Message, args: Tuple[str]) -> str:
    if m.chat_id in [1, 7, 8]:
        try:
            token = tokens[args[0]]
            count = await get_likes_count(token)
            await m.answer(f'работаю друк, тебя лайкнуло {count} девачек и мальчиков')
            photos = await get_likes(token)
            rng = int(args[1])
            for girl in photos:
                rng -= 1
                await m.answer('оп', attachment=girl)
                if not rng:
                    break
        except BaseException as e:
            await m.answer(e)

async def get_likes_count(token: str):
    headers = {"x-auth-token": token}
    r = requests.get("https://api.gotinder.com/v2/fast-match/count", headers=headers)
    data_json = r.json()
    return data_json['data']['count']


async def get_likes(token: str):
    headers = {"x-auth-token": token}
    r = requests.get("https://api.gotinder.com/v2/fast-match/teasers", headers=headers)
    data_json = r.json()

    # ids = [girl['user']['_id'] for girl in data_json['data']['results']]
    # names = []
    # for g_id in ids:
    #     rg = requests.get(f"https://api.gotinder.com/user/{g_id}", headers=headers)
    #     names.append(rg)

    photos = [girl['user']['photos'] for girl in data_json['data']['results']]
    atchs = []
    for ph in photos:
        girl_image = requests.get(ph[0]['url']).content
        img = BytesIO(girl_image)
        photo = await PhotoMessageUploader(bot.api).upload(img)
        atchs.append(photo)
    return atchs
