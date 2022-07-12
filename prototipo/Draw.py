from World import World
import pygame
from Menu import Menu


class Draw:
    def __init__(self, object_world, width, height):
        self.__object_world = object_world
        self.__screen = pygame.display.set_mode((width, height))
        self.__menu = Menu(height, width)
        ### object_menu

    def draw(self):
        if isinstance(self.__object_world, World):
            self.__screen.fill("white")
            for region in self.__object_world.regions:
                for step in region.plataforms:
                    for plataform in step:
                        self.__screen.blit(plataform.image, plataform.rect)
            self.__screen.blit(
                self.__object_world.player.image, self.__object_world.player.rect
            )

    def draw_menu(self):
        self.__screen.fill("white")
        self.__screen.blit(self.__menu.button.image, self.__menu.button.rect)
