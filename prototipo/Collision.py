import os.path
import World
import pygame
from Character import Character
from Region import Region


class Collision:
    def __init__(self):
        self.x_modificador = -15

    def Hit(self, player, object):
        Hit_Boolean = pygame.sprite.spritecollide(player, object, False)
        return Hit_Boolean

    def Update_Hit(self, player, objects):
        HitVar = self.Hit(player, objects)
        if HitVar:
            player.stop()
