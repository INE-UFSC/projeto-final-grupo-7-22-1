from ConstantSingleton import const_single
from controllers.GameController import GameController
from Menu_FSM import Menu_FSM

game = GameController(const_single.width, const_single.height)

main_loop = Menu_FSM(game)
main_loop.run_FSM()
