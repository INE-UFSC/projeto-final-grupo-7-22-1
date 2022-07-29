

from states.State import State


# Representa estado do menu de pontuações
class ScoreMenuState(State):
    def __init__(self, controller):
        super().__init__(controller)

    def execute(self):
        return self.controller.score_menu_loop()