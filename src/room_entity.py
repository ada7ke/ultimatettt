from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class RoomEntity(Base):
    __tablename__ = "rooms"

    id = Column(String, primary_key=True)
    board = Column(String)
