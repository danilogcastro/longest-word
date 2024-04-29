from longest_word.game import Game

class TestGame:
  def test_game_initialization(self):
    # setup
    game = Game()
    # exercise
    grid = game.grid
    # verify
    assert isinstance(grid, list)
    assert len(grid) == 9

  def test_is_valid(self):
    game = Game()
    game.grid = ['O','Q','U','W','R','B','A','Z','E']

    assert game.is_valid('BAROQUE') == True
    assert game.is_valid('WAGON') == False
    assert game.is_valid('BARROQUE') == False
