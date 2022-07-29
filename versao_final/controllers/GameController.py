import pygame
from controllers.PlayerController import PlayerCharacter
from environment.World import World
from menu_elements.MainMenu import MainMenu
from menu_elements.ScoreMenu import ScoreMenu
from menu_elements.GameOverMenu import GameOverMenu
from states.MainMenuState import MainMenuState
from states.ScoreMenuState import ScoreMenuState
from states.GameLoopState import GameLoopState
from states.GameOverState import GameOverState

class GameController:
    def __init__(self, width: int, height: int):
        pygame.init()
        self.__states = {
            "menu" : MainMenuState(self),
            "score": ScoreMenuState(self),
            "start": GameLoopState(self),
            "game-over": GameOverState(self)
        }
        self.__current_state = self.__states["menu"]
        self.__world = World(width, height)
        self.__main_menu = MainMenu(width, height)
        self.__score_menu = ScoreMenu(width, height)
        self.__game_over_menu = GameOverMenu(width, height)
        self.__screen = pygame.display.set_mode((width, height))
        self.__player_controller = PlayerCharacter(self.__world.player)
        self.__clock = pygame.time.Clock()
        self.FPS = 60
    
    def run(self):
        while True:
            nextState = self.__current_state.execute()
            if nextState != None:
                self.__current_state = self.__states[nextState]

    def game_loop(self):
        self.__clock.tick(self.FPS)
        self.FPS += 0.005

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"
                else:
                    self.player_controller.update_keyboard(event)
            elif event.type == pygame.KEYUP:
                self.player_controller.update_keyboard(event)

        self.player_controller.update_char()
        self.world.update_world()
        self.__world.draw(self.__screen)
        pygame.display.update()
        if self.world.check_defeat_conditions():
            return "game-over"

    def game_over_loop(self):
        self.__clock.tick(self.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.world.reset(self.__game_over_menu.input_text())
                    self.player_controller.char = self.world.player
                    self.player_controller.init_keyboard()
                    self.FPS = 60
                    return "start"
                elif event.key == pygame.K_BACKSPACE:
                    self.__game_over_menu.change_text('del')
                else:
                    self.__game_over_menu.change_text(event.unicode)
        self.__game_over_menu.draw(self.__screen)
        pygame.display.update()


    def main_menu_loop(self):
        self.__main_menu.update_buttons
        self.__main_menu.draw(self.__screen)
        self.__clock.tick(self.FPS)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.__main_menu.update(1)
                elif event.key == pygame.K_w:
                    self.__main_menu.update(-1)
                elif event.key == pygame.K_RETURN:
                    if self.__main_menu.state == 0:
                        return "start"
                    elif self.__main_menu.state == 1:
                        return "score"
                    elif self.__main_menu.state == 2:
                        pygame.display.quit()
                        pygame.quit()
                        exit()

    def score_menu_loop(self):
        self.__score_menu.update_score_text(self.__world.scoreDAO.get_all())
        self.__score_menu.draw(self.__screen)
        self.__clock.tick(self.FPS)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                return "menu"

    @property
    def world(self):
        return self.__world

    @property
    def player_controller(self):
        return self.__player_controller
