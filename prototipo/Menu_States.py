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
        elif type == KEYUP:
            return "stay"
    
    def Activation(self):
        if self.__current_state == 0:
            self.game_loop()    
    
    def next_State(self):
        if self.__current_state == 0:
            self.__current_state == 1 

    def previous_State(self):
        if self.__current_state == 0:
            self.__current_state == 2 
        elif self.__current_state == 1:
            self.__current_state == 0

    def event_treatment(self, event):
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return
            else:
                player_input = self.update_keyboard(event)
                if player_input == "enter":
                    self.Activation()
                elif player_input == 'w':
                    self.next_State()
                elif player_input == 's':
                    self.previous_State()
                else:
                    self.__current_state = self.__current_state
        else:
            self.__current_state = self.__current_state

    def Menu_Loop(self):
        while True:
            self.__clock.tick(self.FPS)
            self.FPS += 0.01
            if self.__current_state == 0:
                self.State0()

            self.__drawn.draw()
            pygame.display.update()
    

    def State0(self):
        self.controller.update_char()
        self.world.update_world()
        self.__drawn.draw()
        for event in pygame.event.get():
            self.event_treatment(event)
            


