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


# Gerencia eventos e chama handlers corretos
class GameController:
    def __init__(self, width: int, height: int):
        pygame.init()

        # Estados
        self.__states = {
            "menu" : MainMenuState(self),
            "score": ScoreMenuState(self),
            "start": GameLoopState(self),
            "game-over": GameOverState(self)
        }
        self.__current_state = self.__states["menu"]

        # Mundo contendo objetos fisicos
        self.__world = World(width, height)

        # Menus
        self.__main_menu = MainMenu(width, height)
        self.__score_menu = ScoreMenu(width, height)
        self.__game_over_menu = GameOverMenu(width, height)
        
        # Tela
        self.__screen = pygame.display.set_mode((width, height))
        
        # Controle do jogador
        self.__player_controller = PlayerCharacter(self.__world.player)
        
        # Tempo
        self.__clock = pygame.time.Clock()
        self.FPS = 60
    
    # Loop principal
    def run(self):
        while True:
            #Executa rotina do estado atual e recebe key para o proximo estado se mudar
            nextState = self.__current_state.execute()
            if nextState != None:
                #Atualiza o estado atual
                self.__current_state = self.__states[nextState]

    # Loop do jogo principal
    def game_loop(self):
        self.__clock.tick(self.FPS)
        self.FPS += 0.005

        # Le ultimo evento
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"
                else:
                    self.player_controller.update_keyboard(event) # Atualiza o keyboard do controle
            elif event.type == pygame.KEYUP:
                self.player_controller.update_keyboard(event) # Atualiza o keyboard do controle

        self.player_controller.update_char() # Atualiza movimento do personagem de acordo com o controle
        self.world.update_world() # Atualiza os elementos do mundo
        self.__world.draw(self.__screen) # Desenha o mundo na tela
        pygame.display.update() # Atualiza tela
        # Verifica condição de derrota
        if self.world.check_defeat_conditions():
            return "game-over"

    # Recebe nome para salvar pontuação e reinicia jogo
    def game_over_loop(self):
        self.__clock.tick(self.FPS)
        # Le ultimo evento
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.world.reset(self.__game_over_menu.input_text()) # Reinicia elementos do mundo
                    self.player_controller.char = self.world.player # Reconfigura jogador associado ao controle
                    self.player_controller.init_keyboard() # Reinicia teclado
                    self.FPS = 60
                    return "start"
                elif event.key == pygame.K_BACKSPACE:
                    self.__game_over_menu.change_text('del') # Deleta ultimo caractere digitado
                elif event.unicode.isalpha() or event.unicode.isnumeric():
                    self.__game_over_menu.change_text(event.unicode) # Digita caractere digitado
        self.__game_over_menu.draw(self.__screen) # Desenha tela de game over
        pygame.display.update() # Atualiza a tela

    # Controla o menu principal
    def main_menu_loop(self):
        self.__main_menu.update_buttons() # Atualiza botões
        self.__main_menu.draw(self.__screen) # Desenha menu
        self.__clock.tick(self.FPS)
        pygame.display.update()

        # Le ultimo evento
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                # Navegacao do botões 
                if event.key == pygame.K_s:
                    self.__main_menu.update(1)
                elif event.key == pygame.K_w:
                    self.__main_menu.update(-1)
                elif event.key == pygame.K_RETURN:
                    # Verifica qual botão foi pressionado
                    if self.__main_menu.state == 0:
                        return "start"
                    elif self.__main_menu.state == 1:
                        return "score"
                    elif self.__main_menu.state == 2:
                        pygame.display.quit()
                        pygame.quit()
                        exit()

    # Controla vizualização da tela de pontuação
    def score_menu_loop(self):
        self.__score_menu.update_score_text(self.__world.scoreDAO.get_all()) # Recupera valores do DAO e carrega no jogo
        self.__score_menu.draw(self.__screen) # Desenha tela
        self.__clock.tick(self.FPS)
        pygame.display.update()
        # Verifica interação
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
