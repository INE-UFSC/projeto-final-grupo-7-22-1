        

import pygame
from Character import Character
from PlayerController import PlayerCharacter
from Plataform import PLATAFORM_TYPE
from BasicPlataform import BasicPlataform
from World import World




class GameController:
    def __init__(self, width: int, height: int):
        pygame.init()

        self.__world = World(width, height)
        self.__controller = PlayerCharacter(self.__world.player)
        self.__clock = pygame.time.Clock()
        self.FPS = 60

    def game_loop(self):
        while True:
            self.__clock.tick(self.FPS)
            self.FPS += 0.01

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    self.__controller.update_keyboard(event)
            
            if self.world.check_defeat_conditions():
                self.world.reset()
                self.controller.char = self.world.player
                self.FPS = 60

            self.controller.update_char()
            self.world.update_world()
            self.world.draw_world()
            pygame.display.update()

    @property
    def world(self):
        return self.__world
    
    @property
    def controller(self):
        return self.__controller