

from abc import ABC, abstractmethod


class AbstractMenu(ABC):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        return self.__width
        
    @property
    def height(self):
        return self.__height

    @abstractmethod
    def draw(self):
        pass