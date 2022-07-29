

from abc import ABC, abstractmethod
from entities.Actor import Actor
import enum


class PLATAFORM_TYPE(enum.Enum):
    BASIC = 3
    ICE = 1


class Plataform(Actor):
    def __init__(self, pos: tuple, type: PLATAFORM_TYPE, img):
        super().__init__(pos, img)
        self.__type = type

    @property
    def type(self):
        return self.__type

    # Tratamento da colisão com player
    @abstractmethod
    def player_collision(self, player):
        pass