

import pygame
from Character import Character
from controllers.PlayerController import PlayerCharacter
from Plataform import PLATAFORM_TYPE
from BasicPlataform import BasicPlataform
from World import World

#TEST
pygame.init()

world = World(800,600)
controller = PlayerCharacter(world.player)
FPS = 60
clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            controller.update_keyboard(event)

    controller.update_char()
    world.update_world()
    world.draw_world()
    pygame.display.update()