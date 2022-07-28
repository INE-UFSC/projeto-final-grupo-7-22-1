from ConstantSingleton import const_single
from controllers.GameController import GameController

game = GameController(const_single.width, const_single.height)
game.run()