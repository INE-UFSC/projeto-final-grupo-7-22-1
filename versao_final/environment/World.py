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
    def __init__(self, width: int, height: int, name = "player"):
        self.__dimension = (width, height) # Screen dimensions
        self.__col_module = Collision() # Collision Module
        self.__world_vel = const_single.world_vel
        self.__score = Score("player") # Active player score
        self.__scoreDAO = ScoreDAO()
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

    # Initializes player
    def __init_player(self):
        self.__player = Character((self.__dimension[0]/2, self.__dimension[1]/2), path_single.character_idle)

    # Initializes regions
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

    # Check collision for each plataform
    # @Return plataform if a collision happened
    def __check_collisions(self):
        for region in self.regions:
            for step in region.objects:
                for obj in step:
                    hit = self.__col_module.Update_Hit(self.player, obj)
                    if hit:
                        return obj
        return False


    # Update regions positions
    def __update_regions(self):
        # Update position
        for region in self.regions:
            region.update_region(self.__world_vel)
        
        # Check if new region is necessary
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

    # Move all elements in the world down
    def __move_world(self):
        # Speed up screen movement if player is to close to the top
        if self.player.y < const_single.upper_limit:
            self.__world_vel += 1
        else:
            self.__world_vel = const_single.world_vel

        # Updates region positions
        self.__update_regions()

        # Moves player down
        self.player.set_pos(0, self.__world_vel)

    def __check_player_collision(self):
        # If player is not in a plataform
        if not self.player.hasCollided:
            self.player.fall()  # Updates fall velocity
        self.player.move()  # Move player

        # Check for collision
        hit = self.__check_collisions()
        if hit is False:
            self.player.hasCollided = False  # Player didn't collide
        else:
            # Moves player to top of plataform
            if self.player.y + self.player.height - self.player.vy <= hit.y + 5:
                self.player.hasCollided = True  # Player collided
                self.player.set_pos(
                    0, -((self.player.y + self.player.height) - hit.y))
                hit.player_collision(self.player)

        # Stop player from leave to the left or right of the screen
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

    def draw(self, screen):
        screen.blit(path_single.background, screen.get_rect())

        for region in self.regions:
            for step in region.objects:
                for actor in step:
                    screen.blit(actor.image, actor.rect)
        screen.blit(self.player.image, self.player.rect)
        screen.blit(self.score_text.text, self.score_text.text_rect)


    def reset(self, name):
        self.__init_regions()
        self.__init_player()
        self.__score.name = name
        self.__scoreDAO.add(self.__score)
        self.__score = Score(self.__score.name)
