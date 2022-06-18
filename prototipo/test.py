import pygame
from Character import Character
from PlayerController import PlayerCharacter
from Plataform import PLATAFORM_TYPE
from BasicPlataform import BasicPlataform

#TEST
pygame.init()

square = Character((400,100), (100,100), 'hitbox.png')
plataform = BasicPlataform((0,500), (400,700), PLATAFORM_TYPE.BASIC, 'plataform.png')
actors = [square,plataform]
controller = PlayerCharacter(square)
screen = pygame.display.set_mode((800, 600))
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
    square.fall()
    screen.fill('white')
    for actor in actors:
        screen.blit(actor.image, actor.rect)
        actor.move()
    pygame.display.update()