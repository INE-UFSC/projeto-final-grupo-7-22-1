
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
        self.__world_vel = 2.0

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
        for i in range(1,-3,-1):
            j = randint(1,1)
            self.regions.append(Region(os.path.join("prototipo", "assets",
                                f"preset{j}.txt"), self.dimension[0], 
                                self.dimension[1], i*self.dimension[1]))
    
    def update_world(self):
        
        # Acelera tela se jogador estiver muito perto do topo
        if self.player.y < 50:
            self.__world_vel += 1
        else:
            self.__world_vel = 2

        # Atualiza posicao das regioes
        self.__update_regions()

        # Atualiza posicao do player
        self.player.set_pos(0, self.__world_vel)
        # Se player nao esta numa plataforma
        if not self.player.hasCollided:
            self.player.fall() # Atualiza velocidade de queda
        self.player.move() # Move player

        #Verifica colisao
        hit = self.__check_collisions()
        if  hit == False:
            self.player.hasCollided = False # Se nao ocorrer jogador nao colide
        else:
            self.player.hasCollided = True # Se ocorrer jogador colidiu
            self.player.set_pos(0, -((self.player.y + self.player.height) - hit.y)) #Posiciona jogador acima da plataforma
            self.player.vy = 0 # Zera velocidade y do jogador

        #Impede jogador de sair para a esquerda ou direita da tela
        if self.player.x >= self.dimension[0]:
            self.player.set_pos(-self.player.vx, 0)
            self.player.update_movement('s')
        if self.player.x < 0:
            self. player.set_pos(-self.player.vx, 0)
            self.player.update_movement('s')
    
    # Desenha mundo
    def draw_world(self):
        self.screen.fill('white')
        for region in self.regions:
            for step in region.plataforms:
                for plataform in step:
                    self.screen.blit(plataform.image, plataform.rect)
        self.screen.blit(self.player.image, self.player.rect)
    
    # Verifica colisao para cada plataforma
    # Retorna plataforma se ocorrer colisão 
    def __check_collisions(self):
        for region in self.regions:
            for step in region.plataforms:
                for plataform in step:
                    hit = self.__col_module.Update_Hit(self.player, plataform)
                    if hit:
                        return plataform
        return False

    def __update_regions(self):
        #Update regions positions
        for region in self.regions:
            region.update_region(self.__world_vel)
        if self.regions[0].offset > 2*self.dimension[1]:
            self.regions.pop(0)
            j = randint(1,1)
            self.regions.append(Region(os.path.join("prototipo", "assets",
                                f"preset{j}.txt"), self.dimension[0], 
                                self.dimension[1], self.regions[-1].offset-self.dimension[1]))