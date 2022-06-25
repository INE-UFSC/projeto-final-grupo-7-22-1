        

import pygame
from Character import Character
from PlayerController import PlayerCharacter
from Plataform import PLATAFORM_TYPE
from BasicPlataform import BasicPlataform
from World import World


FPS = 60


class GameController:
    def __init__(self, width: int, height: int):
        pygame.init()

        self.__world = World(width, height)
        self.__controller = PlayerCharacter(self.__world.player)
        self.__clock = pygame.time.Clock()

    def game_loop(self):
        while True:
            self.__clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    self.__controller.update_keyboard(event)

            self.__controller.update_char()
            self.__world.update_world()
            self.__world.draw_world()
            pygame.display.update()