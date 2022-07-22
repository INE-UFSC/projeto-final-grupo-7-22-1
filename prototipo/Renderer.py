import pygame
from Menu import Menu


class Renderer:
    def __init__(self, object_world, object_menu, object_screen):
        self.__object_world = object_world
        self.__screen = object_screen
        self.__menu = object_menu
        ### object_menu

    def draw(self):
        self.__screen.fill("white")
        for region in self.__object_world.regions:
            for step in region.objects:
                for actor in step:
                    self.__screen.blit(actor.image, actor.rect)
        self.__screen.blit(
            self.__object_world.player.image, self.__object_world.player.rect
        )

    def draw_menu(self):
        self.__screen.fill("white")
        self.draw_button(self.__menu.start_button)
        self.draw_button(self.__menu.score_button)
        self.draw_button(self.__menu.quit_button)

        
    def draw_button(self, button):
        self.__screen.blit(button.image, button.rect)
        self.__screen.blit(button.text, button.text_rect)
