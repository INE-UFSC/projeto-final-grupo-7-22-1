from menu_elements.Button import Button
from menu_elements.AbstractMenu import AbstractMenu
from PathSingleton import path_single
from ConstantSingleton import const_single

class MainMenu(AbstractMenu):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.__buttons = [
            Button(
                path_single.button,
                path_single.button2,
                [height / 4, width / 2],
                "START",
                const_single.button_font,
                const_single.color_button_unselected,
                const_single.color_button_selected,
            ),
            Button(
                path_single.button,
                path_single.button2,
                [height / 4, width / 2 + 60],
                "SCORE",
                const_single.button_font,
                const_single.color_button_unselected,
                const_single.color_button_selected,
            ),
            Button(
                path_single.button,
                path_single.button2,
                [height / 4, width / 2 + 120],
                "QUIT",
                const_single.button_font,
                const_single.color_button_unselected,
                const_single.color_button_selected,
            )
        ]
        self.__state = 0
        self.update_buttons()

    @property
    def buttons(self):
        return self.__buttons

    @property
    def state(self):
        return self.__state

    def update(self, value):
        self.__state += value
        if self.__state == 3:
            self.__state = 0
        elif self.__state == -1:
            self.__state = 2
        self.update_buttons()

    def update_buttons(self):
        for i, button in enumerate(self.buttons):
            if self.__state == i:
                button.change_Color()
            else:
                button.og_Color()

    def draw(self, screen):
        screen.blit(path_single.background, screen.get_rect())
        for button in self.buttons:
            screen.blit(button.image, button.rect)
            screen.blit(button.text, button.text_rect)

###---------TODO----------------###

###Abstract class menu, para fazer o menu do dao, menu do esc e menu inicial.
###Essa classe vai ser desenhada no Drawn
