from datetime import datetime
from starlette.config import Config

config = Config(".env")

DATABASE_URL: str = config("SQLALCH_DATABASE_URL")
TOKEN: str = config("TOKEN")

GROUP_ID: int = int(config("GROUP_ID"))
WEEKS_NUM: int = int(config("WEEKS_NUM"))

TOKEN: str = config("TOKEN")
PLACES_ODD: list = config("PLACES_ODD").split(',')
PLACES_EVEN: list = config("PLACES_EVEN").split(',')
SEM_START: datetime = datetime.strptime(config("SEM_START"), "%d/%m/%Y")
