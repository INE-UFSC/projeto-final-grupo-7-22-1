import os.path
import pygame


class Collision:
    def Hit(self, player, plataform):
        Hit_Boolean = pygame.sprite.spritecollide(player, plataform, False)
        if Hit_Boolean != []:
            return Hit_Boolean[0]
        else:
            return False

    def Update_Hit(self, player, plataform):
        #Checa colisao
        if ((plataform.y < player.y + player.height < plataform.y + plataform.height)
            and (plataform.x < player.x < plataform.x + plataform.width
            or plataform.x < player.x + player.width < plataform.x + plataform.width)):
                return True
        return False
