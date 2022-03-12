from vkbottle.bot import Blueprint, Message

bp = Blueprint()

trigger_duna = ['дюну', 'дюна', 'дюны', 'денис', 'авилов']
check_message = lambda m: True if any(trg in m for trg in trigger_duna) else False

@bp.on.message(func=lambda message: check_message(message.text.lower()))
async def today(m: Message) -> str:
    await m.answer('дюна говно 2/10')

# @bp.on.message(func=lambda message: check_message(message.text.lower()))
# async def today(m: Message) -> str:
#     await m.answer('дюна говно 2/10')

# PID = '••••••••••••••••••••'              # имя профиля
# KEY = '••••••••••••••••••••••••••••••••'  # секретный ключ

# query = 'pid=' + PID + '&method=getRandItem&uts=' + str(int(time.time()))  # формируем строку параметров
# signature = hashlib.md5((query + KEY).encode())  # получаем цифровую подпись
# url = 'http://anecdotica.ru/api?' + query + '&hash=' + signature.hexdigest()