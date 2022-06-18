

from abc import ABC, abstractmethod
from Actor import Actor
import enum


class PLATAFORM_TYPE(enum.Enum):
    BASIC = 1
    ICY = 2


class Plataform(Actor):
    def __init__(self, pos: tuple, size: tuple, type: PLATAFORM_TYPE, img_path: str):
        super().__init__(pos, size, img_path)
        self.__type = type

    @property
    def type(self):
        return self.__type

    @abstractmethod
    def update_movement(self, vx, vy):
        pass
        
    @abstractmethod
    def move(self):
        pass