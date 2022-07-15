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
            [height / 4, width / 2],
            "START",
            pygame.font.Font(pygame.font.get_default_font(), 50),
            pygame.Color(252, 233, 79),
            pygame.Color(237, 212, 0),
        )
        self.__Score_Button = Button(
            path_single.plataform,
            [height / 4, width / 1.7],
            "SCORE",
            pygame.font.Font(pygame.font.get_default_font(), 50),
            pygame.Color(252, 233, 79),
            pygame.Color(237, 212, 0),
        )

    def return_button(self):
        return self.__button

    def return_score(self):
        return self.__Score_Button

    def update(self):
        pass

    button = property(fget=return_button)
    score = property(fget=return_score)

###---------TODO----------------###

###Abstract class menu, para fazer o menu do dao, menu do esc e menu inicial.
###Essa classe vai ser desenhada no Drawn
