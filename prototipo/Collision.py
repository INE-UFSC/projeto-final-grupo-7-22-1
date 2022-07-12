import os.path
import World
import pygame
from Character import Character
from Region import Region


class Collision:
    def __init__(self):
        self.x_modificador = -15

    def Hit(self, player, plataform):
        Hit_Boolean = pygame.sprite.spritecollide(player, plataform, False)
        if Hit_Boolean != []:
            return Hit_Boolean[0]
        else:
            return False

    def Update_Hit(self, player, plataform):
        """ 
        dx, dy = 0,0
        if (plataform.y < player.y < plataform.y + plataform.height):
            dy = min(player.y - (plataform.y), player.y - (plataform.y + plataform.height))
        elif (plataform.y < player.y + player.height < plataform.y + plataform.height):
            dy = abs((player.y + player.height) - plataform.y, (player.y + player.height) - (plataform.y + plataform.heigth))
        if (plataform.x < player.x < plataform.x + plataform.width):
            dx = min(abs(player.x - plataform.x), abs(player.x - (plataform.x + plataform.width)))
        elif (plataform.x < player.x + player.width < plataform.x + plataform.width):
            dx = min(abs((player.x + player.width) - plataform.x), abs((player.x + player.width) - (plataform.x + plataform.height)))
        return (dx, dy)        
        """
        #Checa colisao
        if ((player.y < plataform.y < player.y + player.height
            and ((player.y + player.height) - plataform.y) <= 0.3*plataform.height and player.vy > 0)
            and (plataform.x < player.x < plataform.x + plataform.width
            or plataform.x < player.x + player.width < plataform.x + plataform.width)):
                return True
        return False
