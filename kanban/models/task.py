from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from app import engine
from app.base_model import Base


class Task(Base):
    ____tablename__: str = ''

    uuid = Column(Integer, primary_key=True)
    name = Column(String(255))
    parent = Column(Integer, ForeignKey('task.uuid'))
    date_start = Column(DateTime)
    date_end = Column(DateTime)


Base.metadata.create_all(bind=engine)
