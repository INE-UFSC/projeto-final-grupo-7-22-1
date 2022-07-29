

from states.State import State


# Representa estado do jogo
class GameLoopState(State):
    def __init__(self, controller):
        super().__init__(controller)

    def execute(self):
        return self.controller.game_loop()