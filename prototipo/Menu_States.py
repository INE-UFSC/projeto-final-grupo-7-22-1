import pygame


################ KEY BOARD DEVOLVE O INPUT E MUDA O ESTADO
################## ESSA CLASSE DESENHA O MENU
################## ESSA CLASSE ATUALIZA OS ELEMENTOS E INICIA O JOGO
class Menu_States:
    def __init__(self, menu):
        self.__current_state = 0
        self.__menu = menu

    def update_keyboard(self, event: pygame.event.Event):
        type = event.type
        key = event.key
        if type == KEYDOWN:
            if key == K_d:
                return "w"
            elif key == K_a:
                return "s"
            elif key == K_ENTER:
                return "enter"


    def Menu_Loop(self):
        while True:
            self.__clock.tick(self.FPS)
            self.FPS += 0.01
            if self.__current_state == 0:
                self.State0()



            self.controller.update_char()
            self.world.update_world()
            self.__drawn.draw()
            pygame.display.update()
    
    def State0(self):
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
