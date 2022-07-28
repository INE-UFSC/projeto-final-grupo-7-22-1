

from states.State import State


class MainMenuState(State):
    def __init__(self, controller):
        super().__init__(controller)

    def execute(self):
        return self.controller.main_menu_loop()