import pygame
import sys


class TextBox:
    def __init__(self, input_rect, color_active, color_passive, base_font):
        if input_rect == None:
            self.__input_rect = pygame.Rect(200, 200, 140, 32)
            self.__color_1 = pygame.Color("lightskyblue3")
            self.__color_2 = pygame.Color("chartreuse4")
            self.__font = pygame.font.Font(None, 32)
        self.__color = self.__color_2
        self.__text = ""
        self.__active = False
        self.__text_surface = self.__font.render(self.__text, True, (255, 255, 255))
        self.__input_rect.w = max(100, self.__text_surface.get_width() + 10)

    def Click_Box(self, event):
        if self.__input_rect.collidepoint(event.pos):
            self.__active = True
        else:
            self.__active = False

    def BackSpace(self):
        self.__text = self.__text[:-1]
        self.__text_surface = self.__font.render(self.__text, True, (255, 255, 255))

    def Write(self, event):
        self.__text += event.unicode
        self.__text_surface = self.__font.render(self.__text, True, (255, 255, 255))

    def Self_Update(self):
        if self.__active:
            self.__color = self.__color_1

        else:
            self.__color = self.__color_2

    def Draw_Text(self):
        return (
            self.__text_surface,
            (self.__input_rect.x + 5, self.__input_rect.y + 5),
        )

    Draw = property(Draw_Text)
