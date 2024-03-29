from menu_elements.Button import Button
from PathSingleton import path_single
from ConstantSingleton import const_single


class MainMenu:
    def __init__(self, height, width):
        self.__Start_Button = Button(
            path_single.button,
            path_single.button2,
            [height / 4, width / 2],
            "START",
            const_single.button_font,
            const_single.color_button_unselected,
            const_single.color_button_selected,
        )
        self.__Score_Button = Button(
            path_single.button,
            path_single.button2,
            [height / 4, width / 2 + 60],
            "SCORE",
            const_single.button_font,
            const_single.color_button_unselected,
            const_single.color_button_selected,
        )
        self.__Quit_Button = Button(
            path_single.button,
            path_single.button2,
            [height / 4, width / 2 + 120],
            "QUIT",
            const_single.button_font,
            const_single.color_button_unselected,
            const_single.color_button_selected,
        )
        self.__state_Index = 0

    def return_button(self):
        return self.__Start_Button

    def return_score(self):
        return self.__Score_Button

    def return_quit(self):
        return self.__Quit_Button

    def return_state(self):
        return self.__state_Index

    def update(self):
        pass

    start_button = property(fget=return_button)
    score_button = property(fget=return_score)
    quit_button = property(fget=return_quit)
    state = property(fget=return_state)

    def state_Exec(self):
        if self.__state_Index == 0:
            self.Start_State()
        elif self.__state_Index == 1:
            self.Score_State()
        elif self.__state_Index == 2:
            self.Quit_State()

    def update(self, value):
        self.__state_Index += value
        if self.__state_Index == 3:
            self.__state_Index = 0
        elif self.__state_Index == -1:
            self.__state_Index = 2
        self.state_Exec()

    def Start_State(self):
        self.__Start_Button.change_Color()
        self.__Score_Button.og_Color()
        self.__Quit_Button.og_Color()

    def Score_State(self):
        self.__Start_Button.og_Color()
        self.__Score_Button.change_Color()
        self.__Quit_Button.og_Color()

    def Quit_State(self):
        self.__Start_Button.og_Color()
        self.__Score_Button.og_Color()
        self.__Quit_Button.change_Color()


###---------TODO----------------###

###Abstract class menu, para fazer o menu do dao, menu do esc e menu inicial.
###Essa classe vai ser desenhada no Drawn
