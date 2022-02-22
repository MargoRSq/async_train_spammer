from sys import argv
from sqlalchemy import select, insert, update

from db.db import engine, session
from db.models import Timetable, WeekType, Roster

def get_roster():
    select_all = (
        select(Roster.fullname)
    )
    with engine.connect() as conn:
        return conn.execute(select_all).fetchall()