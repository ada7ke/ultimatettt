from enum import Enum
from loguru import logger
import json


class Marker(Enum):
    EMPTY = 0
    X = 1
    O = 2

    def __str__(self):
        if self == Marker.X:
            return "X"
        elif self == Marker.O:
            return "O"
        else:
            return " "

    @staticmethod    
    def fromString(square: str) -> 'Marker':
        if square == " ":
            return Marker.EMPTY
        elif square == "X":
            return Marker.X
        elif square == "O":
            return Marker.O
        raise Exception("Square not ' ', 'X', or 'O'")

class MoveState(Enum):
    INVALID = 0
    VALID = 1
    REPLAY = 2

class Player():
    @staticmethod
    def otherPlayer(player: Marker) -> Marker:
        """ Return the other player. """
        if player == Marker.X:
            return Marker.O
        elif player == Marker.O:
            return Marker.X
        return Marker.EMPTY

class Board():
    def __init__(self):
        self.reset()
    
    def reset(self):
        """ Clears board and resets to start of game. """
        self.board: list[list[Marker]] = [[Marker.EMPTY for i in range(9)] for j in range(9)]
        self.current_player = Marker.X
        self.previous_square = 4
        self.move_num = 0

    # def equals(self, target_board: 'Board') -> bool:
    #     return target_board.board == self.board \
    #         and target_board.current_player == self.current_player \
    #         and target_board.previous_square == self.previous_square \
    #         and target_board.move_num == self.move_num

    def equals(self, target_board: 'Board') -> bool:
        return all(self.board[i][j] == target_board.board[i][j] for i in range(len(self.board)) for j in range(len(self.board[i])))\
            and self.current_player == target_board.current_player and \
            self.previous_square == target_board.previous_square and \
            self.move_num == target_board.move_num
    
    # def serialize(self) -> str:
    #     return json.dumps(self, default=str)

    # @staticmethod
    # def deserialize(json_input: str) -> 'Board':
    #     return json.loads(json_input)

    def serialize(self) -> str:
        serialized_board = {
            'board': self.board,
            'current_player': self.current_player.value,
            'previous_square': self.previous_square,
            'move_num': self.move_num
        }
        return json.dumps(serialized_board, default=str)

    @staticmethod
    def deserialize(json_input: str) -> 'Board':
        deserialized_board = json.loads(json_input)
        board = Board()
        board.board = deserialized_board['board']
        for i in range(len(board.board)):
            for j in range(len(board.board[i])):
                board.board[i][j] = Marker.fromString(board.board[i][j])
        board.current_player = Marker(deserialized_board['current_player'])
        board.previous_square = deserialized_board['previous_square']
        board.move_num = deserialized_board['move_num']
        return board

    def isMiniboardFull(self) -> bool:
        return len([square for square in self.board[self.previous_square] if square != Marker.EMPTY]) == 9
    
    def fillWinner(self, miniboardID: int):
        winner = self.scoreMini(self.board[miniboardID])
        if winner != Marker.EMPTY:
            for i in range(0,9):
                if self.board[miniboardID][i] == Marker.EMPTY:
                    self.board[miniboardID][i] = winner

    def move(self, position: int) -> MoveState:
        """ Puts marker of current player at position.
            Returns true if the move is valid or false otherwise. """
        
        logger.info(f"Player {self.current_player} attempting to move to {position}")

        if position < 0 or position > 8:
            return MoveState.INVALID
        
        if self.isMiniboardFull():
            self.previous_square = position
            self.move_num += 1
            return MoveState.REPLAY
    
        if self.board[self.previous_square][position] != Marker.EMPTY:
            logger.info("Invalid move")
            return MoveState.INVALID

        self.board[self.previous_square][position] = self.current_player
        self.fillWinner(self.previous_square)
        self.previous_square = position
        self.current_player = Player.otherPlayer(self.current_player)
        self.move_num += 1
        logger.info(f"Move successful to {position}")

        return MoveState.VALID


    
    def isOccupied(self, position: int) -> bool:
        return self.board[self.previous_square][position] == Marker.X or self.board[self.previous_square][position] == Marker.O
    
    @staticmethod
    def scoreMini(miniBoard: list[Marker]) -> Marker:
        winner = Marker.EMPTY

        # Rows
        if miniBoard[0] == miniBoard[1] == miniBoard[2] != Marker.EMPTY:
            winner = miniBoard[0]
        elif miniBoard[3] == miniBoard[4] == miniBoard[5] != Marker.EMPTY:
            winner = miniBoard[3]
        elif miniBoard[6] == miniBoard[7] == miniBoard[8] != Marker.EMPTY:
            winner = miniBoard[6]

        # Columns
        elif miniBoard[0] == miniBoard[3] == miniBoard[6] != Marker.EMPTY:
            winner = miniBoard[0]
        elif miniBoard[1] == miniBoard[4] == miniBoard[7] != Marker.EMPTY:
            winner = miniBoard[1]
        elif miniBoard[2] == miniBoard[5] == miniBoard[8] != Marker.EMPTY:
            winner = miniBoard[2]

        # Diagonals
        elif miniBoard[0] == miniBoard[4] == miniBoard[8] != Marker.EMPTY:
            winner = miniBoard[0]
        elif miniBoard[2] == miniBoard[4] == miniBoard[6] != Marker.EMPTY:
            winner = miniBoard[2]
        
        return winner

    def scoring(self) -> Marker:
        miniScores = [self.scoreMini(miniBoard) for miniBoard in self.board]
        logger.info(f"Mini Scores: '{miniScores}'")
        score = self.scoreMini(miniScores)
        return score


    def printBoard(self) -> str:
        printed_board = f" \
{self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} || \
{self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} || \
{self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} \
\n-----------||-----------||-----------\n \
{self.board[0][3]} | {self.board[0][4]} | {self.board[0][5]} || \
{self.board[1][3]} | {self.board[1][4]} | {self.board[1][5]} || \
{self.board[2][3]} | {self.board[2][4]} | {self.board[2][5]} \
\n-----------||-----------||-----------\n \
{self.board[0][6]} | {self.board[0][7]} | {self.board[0][8]} || \
{self.board[1][6]} | {self.board[1][7]} | {self.board[1][8]} || \
{self.board[2][6]} | {self.board[2][7]} | {self.board[2][8]} \
\n_____________________________________\n_____________________________________\n \
{self.board[3][0]} | {self.board[3][1]} | {self.board[3][2]} || \
{self.board[4][0]} | {self.board[4][1]} | {self.board[4][2]} || \
{self.board[5][0]} | {self.board[5][1]} | {self.board[5][2]} \
\n-----------||-----------||-----------\n \
{self.board[3][3]} | {self.board[3][4]} | {self.board[3][5]} || \
{self.board[4][3]} | {self.board[4][4]} | {self.board[4][5]} || \
{self.board[5][3]} | {self.board[5][4]} | {self.board[5][5]} \
\n-----------||-----------||-----------\n \
{self.board[3][6]} | {self.board[3][7]} | {self.board[3][8]} || \
{self.board[4][6]} | {self.board[4][7]} | {self.board[4][8]} || \
{self.board[5][6]} | {self.board[5][7]} | {self.board[5][8]}\
\n_____________________________________\n_____________________________________\n \
{self.board[6][0]} | {self.board[6][1]} | {self.board[6][2]} || \
{self.board[7][0]} | {self.board[7][1]} | {self.board[7][2]} || \
{self.board[8][0]} | {self.board[8][1]} | {self.board[8][2]} \
\n-----------||-----------||-----------\n \
{self.board[6][3]} | {self.board[6][4]} | {self.board[6][5]} || \
{self.board[7][3]} | {self.board[7][4]} | {self.board[7][5]} || \
{self.board[8][3]} | {self.board[8][4]} | {self.board[8][5]} \
\n-----------||-----------||-----------\n \
{self.board[6][6]} | {self.board[6][7]} | {self.board[6][8]} || \
{self.board[7][6]} | {self.board[7][7]} | {self.board[7][8]} || \
{self.board[8][6]} | {self.board[8][7]} | {self.board[8][8]}"
        
        print(printed_board)
        return printed_board


def main():
    playing = True
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]


    board = Board()


    while playing == True:
        print(f"Player {board.current_player} turn")
        board.printBoard()
        playerInput = input("Please choose a square: ")
        while playerInput not in numbers or board.isOccupied(int(playerInput)):
            playerInput = input("Please choose a square: ")
        playerInput = int(playerInput)
        board.move(playerInput)
        print("\n")
        
        score = board.scoring()
        if score != Marker.EMPTY:
            print(f"Player {score} wins!")
            exit()

if __name__ == "__main__":
    main()



# BOARD LAYOUT
#  0 | 1 | 2
# -----------
#  3 | 4 | 5
# -----------
#  6 | 7 | 8