import enum

from sqlalchemy import Column, Integer, String, Enum,  Float

from db.db import engine, Base


class WeekType(enum.Enum):
    ch = 'ch'
    nech = 'nech'


class Clouds(Base):
    __tablename__ = 'clouds'
    __table_args__ = {'extend_existing': True}

    pr = Column(String(30), primary_key=True)
    url = Column(String(300))


class Docs(Base):
    __tablename__ = 'docs'
    __table_args__ = {'extend_existing': True}

    pr = Column(String(30), primary_key=True)
    doc_id = Column(String(30))


class Timetable(Base):
    __tablename__ = 'timetable'
    __table_args__ = {'extend_existing': True}

    class_name = Column(String(100), primary_key=True)
    week = Column(Enum(WeekType))


class Confs(Base):
    __tablename__ = 'confs'
    __table_args__ = {'extend_existing': True}

    pr = Column(String(30), primary_key=True)
    conf_id = Column(String(30))
    conf_password = Column(String(30))


Base.metadata.create_all(engine)
