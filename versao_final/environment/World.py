import os.path
from entities.Character import Character
from environment.Region import Region
from modules.Collision import Collision
from random import randint
from PathSingleton import path_single
from ConstantSingleton import const_single
from score.Score import Score
from score.ScoreDAO import ScoreDAO
from menu_elements.TextBox import TextBox

class World:
    def __init__(self, width: int, height: int):
        self.__dimension = (width, height) # Dimensão da tela
        self.__col_module = Collision() # Modulo de colisão
        self.__world_vel = const_single.world_vel # Velocidade de movimento do mundo
        self.__score = Score("player") # Pontuação do jogador
        self.__scoreDAO = ScoreDAO()
        # Texto de score na tela
        self.__score_text = TextBox(path_single.button, (0.9*self.dimension[0], 0.1*self.dimension[1]), 
                                    str(self.__score.points), const_single.text_font, const_single.color_button_unselected)
        self.__init_player()
        self.__init_regions()

    @property
    def dimension(self):
        return self.__dimension

    @property
    def regions(self):
        return self.__regions

    @property
    def player(self):
        return self.__player

    @property
    def score(self):
        return self.__score

    @property
    def scoreDAO(self):
        return self.__scoreDAO
    
    @property
    def score_text(self):
        return self.__score_text

    # Inicializa jogador
    def __init_player(self):
        self.__player = Character((self.__dimension[0]/2, self.__dimension[1]/2), path_single.character_idle)

    # Inicializa regiões
    def __init_regions(self):
        self.__regions = [
                Region(
                    os.path.join(path_single.assets, "preset1.txt"),
                    self.dimension[0],
                    self.dimension[1], 0
                )]
        for i in range(-1, -4, -1):
            j = randint(1, const_single.preset_amount)
            self.regions.append(
                Region(
                    os.path.join(path_single.assets, f"preset{j}.txt"),
                    self.dimension[0],
                    self.dimension[1],
                    i * self.dimension[1])
            )

    def update_world(self):

        self.__move_world()
        self.player.update_sprite()
        self.__check_player_collision()
        self.score_text.change_text(str(self.score.points))
        
        self.score.increase_score(1)

    # Verifica colisao com cada plataforma
    # @Return plataforma que ocorreu colisao
    def __check_collisions(self):
        for region in self.regions:
            for step in region.objects:
                for obj in step:
                    hit = self.__col_module.Update_Hit(self.player, obj)
                    if hit:
                        return obj
        return False

    # Atualiza posição das regiões
    def __update_regions(self):
        # Atualiza posição
        for region in self.regions:
            region.update_region(self.__world_vel)
        
        # Verifica se nova regiao é necessaria
        if self.regions[0].offset > 2 * self.dimension[1]:
            self.regions.pop(0)
            j = randint(1, const_single.preset_amount)
            self.regions.append(
                Region(
                    os.path.join(path_single.assets, f"preset{j}.txt"),
                    self.dimension[0],
                    self.dimension[1],
                    self.regions[-1].offset - self.dimension[1])
            )

    # Move todos elementos no mundo
    def __move_world(self):
        # Acelera movimento da tela se jogador esta muito perto do topo
        if self.player.y < const_single.upper_limit:
            self.__world_vel += 1
        else:
            self.__world_vel = const_single.world_vel

        self.__update_regions()

        # Move jogador para baixo
        self.player.set_pos(0, self.__world_vel)

    def __check_player_collision(self):
        # Se jogador não estiver em uma plataforma
        if not self.player.hasCollided:
            self.player.fall()  # Atualiza velocidade de queda
        self.player.move()

        # Checa por colisões
        hit_plataform = self.__check_collisions()
        if hit_plataform is False:
            self.player.hasCollided = False  # Jogador nao colidiu
        else:
            #Trata colisão do jogador
            hit_plataform.player_collision(self.player)

        # Impede jogador de sair pela esquerda ou direita da tela
        if self.player.x + self.player.width >= (self.dimension[0] - const_single.wall_bound):
            self.player.set_pos(
                self.dimension[0] - (self.player.x + self.player.width + const_single.wall_bound), 0
            )
            self.player.update_movement("s")
        if self.player.x < const_single.wall_bound:
            self.player.set_pos((const_single.wall_bound-self.player.x), 0)
            self.player.update_movement("s")

    def check_defeat_conditions(self):
        if self.player.y > self.dimension[1] * const_single.defeat_condition_multiplier:
            return True
        return False

    # Desenha mundo na tela
    # @param screen -> tela na qual sera desenhada o mundo
    def draw(self, screen):
        screen.blit(path_single.background, screen.get_rect())

        for region in self.regions:
            for step in region.objects:
                for actor in step:
                    screen.blit(actor.image, actor.rect)
        screen.blit(self.player.image, self.player.rect)
        screen.blit(self.score_text.text, self.score_text.text_rect)

    # Reseta mundo
    # @param name -> Nome da pontuação a ser salva
    def reset(self, name):
        self.__init_regions()
        self.__init_player()
        if name == '':
            name = "player"
        self.__score.name = name
        self.__scoreDAO.add(self.__score)
        self.__score = Score(self.__score.name)
