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
    with engine.connect() as conn:
        for class_name in ch:
            insert_state = (
                insert(Timetable).
                values(class_name=class_name,
                       week=WeekType.ch.value))
            conn.execute(insert_state)
        for class_name in nech:
            insert_state = (
                insert(Timetable).
                values(class_name=class_name,
                       week=WeekType.nech.value))
            conn.execute(insert_state)
