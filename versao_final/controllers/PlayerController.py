from pygame.event import Event
from pygame.locals import *
from entities.Character import Character

class PlayerCharacter:
    def __init__(self, char: Character):
        # Personagem sendo controlado
        self.__char = char
        self.init_keyboard()

    @property
    def char(self):
        return self.__char

    @char.setter
    def char(self, char: Character):
        self.__char = char
    
    @property
    def keyboard(self):
        return self.__keyboard

    # Recebe evento e analiza qual teclas foram pressionadas
    def update_keyboard(self, event: Event):
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

    # Atualiza movimento do personagem de acordo com teclas pressionadas
    def update_char(self):
        
        if self.keyboard['space'] == True:
            self.char.increase_jump_force()
        else:
            self.char.jump()
            if self.keyboard['a']:
                self.char.update_movement('l')
            elif self.keyboard['d']:
                self.char.update_movement('r')
    
    def init_keyboard(self):
        self.__keyboard = {
            'a': False,
            'd': False,
            'space': False}