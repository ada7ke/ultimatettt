from typing import Self
from enum import Enum

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
        self.board = [[Marker.EMPTY for i in range(9)] for j in range(9)]
        self.current_player = Marker.X
        self.previous_square = 4

    def move(self, position: int) -> bool:
        """ Puts marker of current player at position.
            Returns true if the move is valid or false otherwise. """
        
        if position < 0 or position > 8 or self.board[self.previous_square][position] != Marker.EMPTY:
            return False

        self.board[self.previous_square][position] = self.current_player
        self.previous_square = position
        self.current_player = Player.otherPlayer(self.current_player)
        return True
    
    def isOccupied(self, position: int) -> bool:
        return self.board[self.previous_square][position] == Marker.X or self.board[self.previous_square][position] == Marker.O
    
    @staticmethod
    def scoreMini(miniBoard):
        winner = Marker.EMPTY

        # Rows
        if miniBoard[0] == miniBoard[1] == miniBoard[2]:
            winner = miniBoard[0]
        elif miniBoard[3] == miniBoard[4] == miniBoard[5]:
            winner = miniBoard[3]
        elif miniBoard[6] == miniBoard[7] == miniBoard[8]:
            winner = miniBoard[6]

        # Columns
        elif miniBoard[0] == miniBoard[3] == miniBoard[6]:
            winner = miniBoard[0]
        elif miniBoard[1] == miniBoard[4] == miniBoard[7]:
            winner = miniBoard[1]
        elif miniBoard[2] == miniBoard[5] == miniBoard[8]:
            winner = miniBoard[2]

        # Diagonals
        elif miniBoard[0] == miniBoard[4] == miniBoard[8]:
            winner = miniBoard[0]
        elif miniBoard[2] == miniBoard[4] == miniBoard[6]:
            winner = miniBoard[2]

        return winner

    def scoring(self):
        miniScores = [self.scoreMini(miniBoard) for miniBoard in self.board]
        score = self.scoreMini(miniScores)
        return score


    def printBoard(self):
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




# BOARD LAYOUT
#  0 | 1 | 2
# -----------
#  3 | 4 | 5
# -----------
#  6 | 7 | 8