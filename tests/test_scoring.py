from ultimate import Board, Marker
from loguru import logger

def test_scoring():
    board = Board()

    board.move(6)
    logger.info(f"\n{board.printBoard()}")
    board.move(0)
    logger.info(f"\n{board.printBoard()}")
    board.move(6)
    logger.info(f"\n{board.printBoard()}")
    board.move(3)
    logger.info(f"\n{board.printBoard()}")
    board.move(6)
    logger.info(f"\n{board.printBoard()}")
    board.move(6)
    logger.info(f"\n{board.printBoard()}")
    board.move(2)
    logger.info(f"\n{board.printBoard()}")
    board.move(7)
    logger.info(f"\n{board.printBoard()}")
    board.move(0)
    logger.info(f"\n{board.printBoard()}")
    board.move(7)
    logger.info(f"\n{board.printBoard()}")
    board.move(3)
    logger.info(f"\n{board.printBoard()}")
    board.move(7)
    logger.info(f"\n{board.printBoard()}")
    board.move(6)
    logger.info(f"\n{board.printBoard()}")
    board.move(2)
    logger.info(f"\n{board.printBoard()}")
    board.move(8)
    logger.info(f"\n{board.printBoard()}")
    board.move(0)
    logger.info(f"\n{board.printBoard()}")
    board.move(8)
    logger.info(f"\n{board.printBoard()}")
    board.move(3)
    logger.info(f"\n{board.printBoard()}")
    board.move(8)
    logger.info(f"\n{board.printBoard()}")
    board.move(6)
    logger.info(f"\n{board.printBoard()}")

    score = board.scoring()
    assert score == Marker.O