from ultimate import Board
from loguru import logger

def test_serialize():
    board = Board()
    board.move(3)
    board.move(8)
    board.move(2)
    board.move(7)

    json = board.serialize()
    new_board = Board.deserialize(json)
    logger.info(f"New board: '{new_board}'")
    logger.info(f"Board: '{board}'")
    board.printBoard()
    print("\n")
    new_board.printBoard()

    # assert board.current_player == new_board.current_player
    # assert board.previous_square == new_board.previous_square
    # assert board.move_num == new_board.move_num
    # assert all(board.board[i][j] == new_board.board[i][j] for i in range(len(board.board)) for j in range(len(board.board[i])))

    for i in range(len(board.board)):
        for j in range(len(board.board[i])):
            assert board.board[i][j] == new_board.board[i][j]

    # assert board.equals(new_board)
