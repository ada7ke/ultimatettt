from ultimate import Board
from loguru import logger

def test_equal_boards():
    player_a = Board()
    player_a.move(3)
    player_a.move(8)
    player_a.move(2)
    player_a.move(7)

    player_b = Board()
    player_b.move(3)
    player_b.move(8)
    player_b.move(2)
    player_b.move(7)

    player_c = Board()
    player_c.move(3)
    player_c.move(8)
    player_c.move(2)
    player_c.move(7)
    player_c.move(4)


    assert player_a.equals(player_b)
    assert not player_a.equals(player_c)