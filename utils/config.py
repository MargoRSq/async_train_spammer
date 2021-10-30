from starlette.config import Config

config = Config(".env")

DATABASE_URL: str = config("SQLALCH_DATABASE_URL")
TOKEN: str = config("TOKEN")

GROUP_ID: int = int(config("GROUP_ID"))
