

from abc import ABC
from abc import abstractmethod
import pygame
import os


class Actor(ABC, pygame.sprite.Sprite):
    def __init__(self, pos: tuple, size: tuple, img_path: str):
        super().__init__()
        
        #Attributes
        self.__x = pos[0]
        self.__y = pos[1]
        self.__width = size[0]
        self.__height = size[1]
        self.__vx = 0 
        self.__vy = 0

        #Rectangle representation
        self.__image = pygame.image.load(os.path.join("prototipo", "assets",img_path))
        self.__rect = self.image.get_rect()
        self.__rect.move_ip(*pos)

        self.__width, self.__height = self.__image.get_size()

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

    @property
    def rect(self):
        return self.__rect

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def update_movement(self):
        pass
