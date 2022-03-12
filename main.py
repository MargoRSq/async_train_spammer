from utils.config import bot
from utils.time_messages import time_loop
from commands import bps

for bp in bps:
    bp.load(bot)

print("Here we go!")

if __name__ == '__main__':
    time_loop()
    bot.run_forever()