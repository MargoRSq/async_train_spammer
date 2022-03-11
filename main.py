from vkbottle.bot import Bot

from utils.config import TOKEN
from commands import bps

bot = Bot(TOKEN)

for bp in bps:
    bp.load(bot)

print("Here we go!")
bot.run_forever()
