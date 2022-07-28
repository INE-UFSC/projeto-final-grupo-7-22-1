

from abc import ABC
from abc import abstractmethod
import pygame


#Class actor abstracts implementation of any physical object in the world
#Inherits pygame Sprite class
class Actor(ABC, pygame.sprite.Sprite):
    def __init__(self, pos: tuple, img: str):
        super().__init__()
        
        # Attributes
        # Position (x, y)
        self.__x = pos[0]
        self.__y = pos[1]
        # Velocity vectors (x, y)
        self.__vx = 0 
        self.__vy = 0

        #Rectangle representation
        self.__image = img # Sprite Image
        self.__rect = self.image.get_rect() #Pygame rect object generated from sprite
        self.__rect.move_ip(*pos) # Sets intial position of rect

        self.__width, self.__height = self.__image.get_size() # Set size according to sprite dimension

    # Getters and Setters
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

    # Updates position
    @abstractmethod
    def move(self):
        pass

    # Updates velocity vectors
    @abstractmethod
    def update_movement(self):
        pass
