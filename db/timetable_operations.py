from sqlite3 import Time
from sys import argv
from sqlalchemy import select, insert, update

from db.db import engine, session
from db.models import Timetable, WeekType

def get_rasp():
    select_ch = (
        select(Timetable.class_name).
        where(Timetable.week == WeekType.ch)
    )
    select_nech = (
        select(Timetable.class_name).
        where(Timetable.week == WeekType.nech)
    )
    with engine.connect() as conn:
        ch = conn.execute(select_ch).fetchall()
        nech = conn.execute(select_nech).fetchall()
    return {'ch': ch, 'nech': nech}

def post_rasp(ch, nech):
    lists = {'ch': ch, 'nech': nech}
    for wtype in ['ch', 'nech']:
        for class_id, class_name in enumerate(lists[wtype]):
            class_id = class_id if wtype == 'ch' else class_id + 30
            pr = Timetable(id=class_id,
                        class_name=class_name,
                        week=wtype)
            session.merge(pr)
    session.commit()