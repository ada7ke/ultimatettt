from ultimate import Board, Marker
from loguru import logger

def test_full_miniboard():
    testBoard = Board()

    testBoard.move(0)
    logger.info(f"\n{testBoard.printBoard()}")
    testBoard.move(4)
    logger.info(f"\n{testBoard.printBoard()}")
    testBoard.move(1)
    logger.info(f"\n{testBoard.printBoard()}")
    testBoard.move(4)
    logger.info(f"\n{testBoard.printBoard()}")
    testBoard.move(2)
    logger.info(f"\n{testBoard.printBoard()}")
    testBoard.move(6)
    logger.info(f"\n{testBoard.printBoard()}")
    testBoard.move(4)
    logger.info(f"\n{testBoard.printBoard()}")
    testBoard.move(3)
    logger.info(f"\n{testBoard.printBoard()}")
    testBoard.move(7)
    logger.info(f"\n{testBoard.printBoard()}")

    assert testBoard.board[3][3] == Marker.EMPTY
