

from states.State import State


# Representa estado de game over
class GameOverState(State):
    def __init__(self, controller):
        super().__init__(controller)
    
    def execute(self):
        return self.controller.game_over_loop()