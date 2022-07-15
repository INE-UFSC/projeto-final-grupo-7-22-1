import os.path
import pygame
from Character import Character
from Region import Region
from Collision import Collision
from random import randint
from PathSingleton import path_single
from Score import Score

class World:
    def __init__(self, width: int, height: int, name = "player"):
        self.__dimension = (width, height) # Screen dimensions
        self.__col_module = Collision() # Collision Module
        self.__world_vel = 2.0
        self.__score = Score(name) # Active player score
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

    # Initializes player
    def __init_player(self):
        self.__player = Character((self.__dimension[0]/2, self.__dimension[1]/2), (100, 100), path_single.player)

    # Initializes regions
    def __init_regions(self):
        self.__regions = []
        for i in range(1, -3, -1):
            j = randint(1, 2)
            self.regions.append(
                Region(
                    os.path.join(path_single.assets, f"preset{j}.txt"),
                    self.dimension[0],
                    self.dimension[1],
                    i * self.dimension[1],
                    path_single.plataform,
                )
            )

    def update_world(self):

        self.__move_world()
        self.__check_player_collision()
        
        self.score.increase_score(1)
        print(self.score.string())

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
            j = randint(1, 2)
            self.regions.append(
                Region(
                    os.path.join(path_single.assets, f"preset{j}.txt"),
                    self.dimension[0],
                    self.dimension[1],
                    self.regions[-1].offset - self.dimension[1],
                    path_single.plataform,
                )
            )

    # Move all elements in the world down
    def __move_world(self):
        # Speed up screen movement if player is to close to the top
        if self.player.y < 50:
            self.__world_vel += 1
        else:
            self.__world_vel = 2

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
            self.player.hasCollided = True  # Player collided
            # Moves player to top of plataform
            self.player.set_pos(
                0, -((self.player.y + self.player.height) - hit.y)
            )
            self.player.vy = 0

        # Stop player from leave to the left or right of the screen
        if self.player.x + self.player.width >= self.dimension[0]:
            self.player.set_pos(
                self.dimension[0] - (self.player.x + self.player.width), 0
            )
            self.player.update_movement("s")
        if self.player.x < 0:
            self.player.set_pos(-self.player.x, 0)
            self.player.update_movement("s")

    def check_defeat_conditions(self):
        if self.player.y > self.dimension[1] * 1.5:
            return True
        return False

    def reset(self):
        self.__init_regions()
        self.__init_player()
