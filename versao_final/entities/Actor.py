

from abc import ABC
from abc import abstractmethod
import pygame

# Abstrai implementação de qualquer objeto fisico no mundo
# Herda classe Sprite do pygame
class Actor(ABC, pygame.sprite.Sprite):
    def __init__(self, pos: tuple, img: str):
        super().__init__()
        
        # Atributos
        # Posição (x, y)
        self.__x = pos[0]
        self.__y = pos[1]
        # Vetores velocidade (x, y)
        self.__vx = 0 
        self.__vy = 0

        # Representação do retangulo
        self.__image = img # Imagem do sprite
        self.__rect = self.image.get_rect() # Objeto rect do Pygame gerado a partir do sprite
        self.__rect.move_ip(*pos) # Configura posicão inicial do retangulo

        self.__width, self.__height = self.__image.get_size() # Configura tamanho de acordo com as dimensoes do sprite

    # Getters e Setters
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def vx(self):
        return self.__vx

    @vx.setter
    def vx(self, vx):
        self.__vx = vx

    @property
    def vy(self):
        return self.__vy

    @vy.setter
    def vy(self, vy):
        self.__vy = vy

    @property
    def image(self):
        return self.__image   

    @image.setter
    def image(self, image):
        self.__image = image   

    @property
    def rect(self):
        return self.__rect

    # Atualiza posição
    @abstractmethod
    def move(self):
        pass

    # Atualiza vetores de velocidade
    @abstractmethod
    def update_movement(self):
        pass
