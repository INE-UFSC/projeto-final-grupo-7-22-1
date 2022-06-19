import os.path
import World
import pygame
from Character import Character
from Region import Region


class Collision:
    def __init__(self):
        self.x_modificador = -15

    def Hit(self, Player, Objects):
        Hit_Boolean = pygame.sprite.spritecollide(Player, Objects, False)
        return Hit_Boolean

    def Update_Hit(self, Player, Objects):
        HitVar = self.Hit(Player, Objects)
        if HitVar:
            Player.stop()
