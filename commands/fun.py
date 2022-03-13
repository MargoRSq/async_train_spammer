from vkbottle.bot import Blueprint, Message

bp = Blueprint()

trigger_duna = ['дюну', 'дюна', 'дюны', 'денис', 'авилов']
check_message = lambda m: True if any(trg in m for trg in trigger_duna) else False

@bp.on.message(func=lambda message: check_message(message.text.lower()))
async def today(m: Message) -> str:
    await m.answer('дюна говно 2/10')
