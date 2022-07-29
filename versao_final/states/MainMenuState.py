

from states.State import State


# Representa estado do menu principal
class MainMenuState(State):
    def __init__(self, controller):
        super().__init__(controller)

    def execute(self):
        return self.controller.main_menu_loop()