from typing import List
from sqlalchemy import select

from db.db import engine, session
from db.models import Roster

def get_roster():
    select_all = (
        select(Roster.fullname)
    )
    with engine.connect() as conn:
        return conn.execute(select_all).fetchall()


def push_roster(roster: List):
    session.query(Roster).delete()
    for i, item in enumerate(roster):
        guy = Roster(id=i, fullname=item)
        session.merge(guy)
    session.commit()
