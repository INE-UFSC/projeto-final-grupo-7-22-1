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
        if Hit_Boolean != []:
            return Hit_Boolean[0]
        else:
            return False

    def Update_Hit(self, player, object):
        HitVar = object
        #Checa colisao
        if (player.y < HitVar.y < player.y + player.height
            and (HitVar.x < player.x < HitVar.x + HitVar.width
            or HitVar.x < player.x + player.width < HitVar.x + HitVar.width)):
            if player.vy >= 0:
                return True
        return False
