
import os.path
import pygame
from Character import Character
from Region import Region
from Collision import Collision

class World:
    def __init__(self, width: int, height: int):
        self.__screen = pygame.display.set_mode((width, height))
        self.__dimension = (width,height)
        self.__player = Character((400,100), (100,100), 'hitbox.png')
        self.__regions = []
        self.__col_module = Collision()

        self.__init_regions()

    @property
    def screen(self):
        return self.__screen

    @property
    def dimension(self):
        return self.__dimension

    @property
    def regions(self):
        return self.__regions

    @property
    def player(self):
        return self.__player

    def __init_regions(self):
        for i in range(4):
            self.regions.append(Region(os.path.join('prototipo/assets','preset1.txt'), self.dimension[0], self.dimension[1], -i*self.dimension[1]))
    
    def update_world(self):
        
        for region in self.regions:
            for step in region.plataforms:
                for plataform in step:
                    if self.__col_module.Hit(self.player, pygame.sprite.Group(plataform)):
                        #print(f"{self.player} collided with {plataform}")
                        self.player.stop()
            region.update_region(5)

        self.player.fall()
        self.player.move()
    
    def draw_world(self):
        self.screen.fill('white')
        self.screen.blit(self.player.image, self.player.rect)
        for region in self.regions:
            for step in region.plataforms:
                for plataform in step:
                    self.screen.blit(plataform.image, plataform.rect)