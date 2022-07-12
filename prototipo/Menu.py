from Button import Button
from PathSingleton import path_single
import pygame


class Menu:
    def __init__(self, height, width):
        self.__height: height
        self.__width: width
        pygame.font.init()
        self.__button = Button(
            path_single.plataform,
            [height / 2, width / 2],
            "START",
            pygame.font.Font(pygame.font.get_default_font(), 50),
            pygame.Color(252, 233, 79),
            pygame.Color(237, 212, 0),
        )

    def return_button(self):
        return self.__button

    button = property(fget=return_button)


###---------TODO----------------###

###Abstract class menu, para fazer o menu do dao, menu do esc e menu inicial.
###Essa classe vai ser desenhada no Drawn
