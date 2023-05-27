from ultimate import Board
from loguru import logger
from room_entity import Base, RoomEntity
import sqlalchemy as db
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.ext.declarative import declarative_base
from pathlib import Path

def test_create_session():
    board = Board()
    
    board.move(3)
    board.move(8)
    board.move(2)
    board.move(7)
    board.move(1)

    board_str = board.serialize()

    file_name = Path("database.db")
    if file_name.exists():
        file_name.unlink()
    engine = db.create_engine(f"sqlite:///{file_name}")
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        room_entity = RoomEntity(id="test", board=board_str)
        session.add(room_entity)
        session.commit()
    
    with Session(engine) as session:
        stmt = select(RoomEntity).where(RoomEntity.id == "test")
        new_room_entity = session.execute(stmt).scalar()
        new_board = Board.deserialize(new_room_entity.board)
        
    file_name.unlink()
    assert new_board.equals(board)