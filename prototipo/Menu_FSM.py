import enum
import pygame

class State(enum.Enum):
    MAIN_MENU = 0
    GAME_LOOP = 1
    GAME_OVER = 2
    SCORE_MENU = 3

# ESSA CLASSE ATUALIZA OS ELEMENTOS E INICIA O JOGO
class Menu_FSM:
    def __init__(self, game_controller):
        self.__current_state = State.MAIN_MENU
        self.__status = ''
        self.__game_controller = game_controller

    @property
    def current_state(self):
        return self.__current_state

    @current_state.setter
    def current_state(self, state):
        self.__current_state = state

    def run_FSM(self):
        while True:
            self.execute_state()
            self.next_state()

    def next_state(self):
        if self.current_state == State.MAIN_MENU:
            if self.__status == "start":
                self.current_state = State.GAME_LOOP
            if self.__status == "score":
                self.current_state = State.SCORE_MENU
        if self.current_state == State.SCORE_MENU:
            if self.__status == "menu":
                self.current_state = State.MAIN_MENU
        elif self.current_state == State.GAME_LOOP:
            if self.__status == "game-over":
                self.current_state = State.GAME_OVER
            elif self.__status == "pause":
                self.current_state = State.MAIN_MENU
        elif self.current_state == State.GAME_OVER:
            if self.__status == "menu":
                self.current_state = State.MAIN_MENU         
            if self.__status == "restart":
                self.current_state = State.GAME_LOOP

    def execute_state(self):
        if self.current_state == State.MAIN_MENU:
            self.__status = self.__game_controller.main_menu_loop()
        elif self.current_state == State.GAME_LOOP:
            self.__status = self.__game_controller.game_loop()
        elif self.current_state == State.GAME_OVER:
            self.__status = self.__game_controller.game_over_loop()
        elif self.current_state == State.SCORE_MENU:
            self.__status = self.__game_controller.score_loop()

    def Menu_Loop(self):
        while True:
            self.__clock.tick(self.FPS)
            self.FPS += 0.01
            if self.__current_state == 0:
                self.State0()
            self.__drawn.draw()
            pygame.display.update()
    

 