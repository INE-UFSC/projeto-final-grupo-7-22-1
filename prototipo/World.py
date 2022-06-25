
import os.path
import pygame
from Character import Character
from Region import Region
from Collision import Collision
from random import randint
from math import sqrt


class World:
    def __init__(self, width: int, height: int):
        self.__screen = pygame.display.set_mode((width, height))
        self.__dimension = (width,height)
        self.__player = Character((400,100), (100,100), 'hitbox.png')
        self.__regions = []
        self.__col_module = Collision()
        self.__world_vel = 0.0

        self.i = 0
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
        for i in range(2,-2,-1):
            j = randint(1,1)
            self.regions.append(Region(os.path.join('prototipo/assets',
                                f"preset{j}.txt"), self.dimension[0], 
                                self.dimension[1], i*self.dimension[1]))
    
    def update_world(self):
        self.__world_vel = sqrt(self.__world_vel+1)
        
        #Update regions positions
        for region in self.regions:
            region.update_region(self.__world_vel)
        #Update player position
        self.player.set_pos(0, self.__world_vel)
        self.player.move()

        #Check collisions
        if self.__check_collisions():
            if self.player.vy >= 0:
                self.player.hasCollided = True
                self.player.set_pos(0, -self.player.vy)
                self.player.vy = 0
        else:
            self.player.hasCollided = False

        if self.player.x >= self.dimension[0]:
            self.player.set_pos(-self.player.vx, 0)
            self.player.update_movement('s')
        if self.player.x < 0:
            self. player.set_pos(-self.player.vx, 0)
            self.player.update_movement('s')
        if not self.player.hasCollided:
            self.player.fall()
    
    def draw_world(self):
        self.screen.fill('white')
        for region in self.regions:
            for step in region.plataforms:
                for plataform in step:
                    self.screen.blit(plataform.image, plataform.rect)
        self.screen.blit(self.player.image, self.player.rect)
    
    def __check_collisions(self):
        for region in self.regions:
            for step in region.plataforms:
                for plataform in step:
                    hit = self.__col_module.Hit(self.player, [plataform])
                    if hit:
                        return True
        return False