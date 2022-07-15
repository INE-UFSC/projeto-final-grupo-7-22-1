import pygame

class Menu_States:
    def __init__(self, menu):
        self.__current_state = "start"
    def Menu_Loop(self):
        pass
        while True:
            self.__clock.tick(self.FPS)
            self.FPS += 0.01

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    else:
                        self.__controller.update_keyboard(event)
                elif event.type == pygame.KEYUP:
                    self.__controller.update_keyboard(event)
                elif event.type == pygame.KEYDOWN:
                    self.game_loop()
            if self.world.check_defeat_conditions():
                self.game_over_loop()

            self.controller.update_char()
            self.world.update_world()
            self.__drawn.draw()
            pygame.display.update()
