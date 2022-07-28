

from states.State import State


class GameLoopState(State):
    def __init__(self, controller):
        super().__init__(controller)

    def execute(self):
        return self.controller.game_loop()