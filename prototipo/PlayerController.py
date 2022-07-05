import pygame
from pygame.locals import *
from Character import Character

class PlayerCharacter:
    def __init__(self, char: Character):
        self.__char = char
        self.__keyboard = {
            'a': False,
            'd': False,
            'space': False}

    @property
    def char(self):
        return self.__char

    @char.setter
    def char(self, char: Character):
        self.__char = char
    
    @property
    def keyboard(self):
        return self.__keyboard

    def update_keyboard(self, event: pygame.event.Event):
        type = event.type
        key = event.key
        if type == KEYDOWN:
            if key == K_d:
                self.keyboard['a'] = False
                self.keyboard['d'] = True
            elif key == K_a:
                self.keyboard['a'] = True
                self.keyboard['d'] = False
            elif key == K_SPACE:
                self.keyboard['space'] = True
        if type == KEYUP:
            if key == K_d:
                self.keyboard['d'] = False
            elif key == K_a:
                self.keyboard['a'] = False
            elif key == K_SPACE:
                self.keyboard['space'] = False

    def update_char(self):
        if self.keyboard['a']:
            self.char.update_movement('l')
        elif self.keyboard['d']:
            self.char.update_movement('r')
        else:
            self.char.update_movement('s')

        if self.keyboard['space'] == True:
            self.char.increase_jump_force()
        else:
            self.char.jump()
        