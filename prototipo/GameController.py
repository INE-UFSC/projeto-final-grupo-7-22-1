import pygame
from Character import Character
from PlayerController import PlayerCharacter
from Plataform import PLATAFORM_TYPE
from BasicPlataform import BasicPlataform
from World import World
from Renderer import Renderer
from Menu import Menu


class GameController:
    def __init__(self, width: int, height: int):
        pygame.init()
        self.__world = World(width, height)
        self.__menu = Menu(height, width)
        self.__screen = pygame.display.set_mode((width, height))
        self.__renderer = Renderer(self.__world, self.__menu, self.__screen)
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
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    else:
                        self.__controller.update_keyboard(event)
                elif event.type == pygame.KEYUP:
                    self.__controller.update_keyboard(event)

            if self.world.check_defeat_conditions():
                self.game_over_loop()

            self.controller.update_char()
            self.world.update_world()
            self.__renderer.draw()
            pygame.display.update()

    def game_over_loop(self):
        run = True
        while run:
            self.__clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    run = False
                    self.world.reset()
                    self.controller.char = self.world.player
                    self.FPS = 60

    def main_menu_loop(self):
        run = True
        while run:
            self.__renderer.draw_menu()
            self.__clock.tick(self.FPS)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    self.game_loop()

    @property
    def world(self):
        return self.__world

    @property
    def controller(self):
        return self.__controller
