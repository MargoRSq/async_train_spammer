from datetime import datetime
from starlette.config import Config
from vkbottle.bot import Bot


config = Config(".env")

DATABASE_URL: str = config("SQLALCH_DATABASE_URL")
TOKEN: str = config("TOKEN")
bot = Bot(TOKEN)

GROUP_ID: int = int(config("GROUP_ID"))
CHAT_ID: int = int(config("CHAT_ID"))
WEEKS_NUM: int = int(config("WEEKS_NUM"))

TOKEN: str = config("TOKEN")
CAT_TOKEN: str = config("CAT_TOKEN")
PLACES_ODD: list = config("PLACES_ODD").split(',')
PLACES_EVEN: list = config("PLACES_EVEN").split(',')
SEM_START: datetime = datetime.strptime(config("SEM_START"), "%d/%m/%Y")

MONDAY: str = "photo-202303736_457239162"
TUESDAY: str = "photo-202303736_457239163"
WEDNESDAY: str = "photo-202303736_457239166"
THURSDAY: str = "photo-202303736_457239165"
FRIDAY: str = "photo-202303736_457239167"
SATURDAY: str = "photo-202303736_457239164"