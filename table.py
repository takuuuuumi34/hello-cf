from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, TEXT, BLOB, DateTime, ForeignKey
from setting import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(TEXT, nullable=False)

