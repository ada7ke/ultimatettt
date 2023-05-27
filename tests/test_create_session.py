from ultimate import Board
from loguru import logger
from room_entity import RoomEntity
import sqlalchemy as db
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.ext.declarative import declarative_base
import os

def test_create_session():
    board = Board()
    
    board.move(3)
    board.move(8)
    board.move(2)
    board.move(7)
    board.move(1)

    board_str = board.serialize()
    file_name = "database.db"
    engine = db.create_engine(f"sqlite:///{file_name}")
    Base = declarative_base()
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        room_entity = RoomEntity(id="test", board=board_str)
        session.add(room_entity)
        session.commit()
    
    session = Session(engine)
    
    stmt = select(RoomEntity).where(RoomEntity.id == "test")
    new_room_entity = session.scalar(stmt).one()
    new_board = Board.deserialize(new_room_entity.board)
    
    os.remove(file_name)
    assert new_board.equals(board)