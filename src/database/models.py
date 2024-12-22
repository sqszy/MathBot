from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Cheatsheet(Base):
    __tablename__ = "cheatsheets"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    callback_data = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    caption = Column(String, nullable=False)
