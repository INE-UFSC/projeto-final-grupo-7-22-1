import pygame as pg
import os


# Contem paths e imagens utilizados no jogo
class Path_Singleton:
    def __init__(self):
        self.resources = os.path.dirname(__file__)
        self.assets = os.path.join(self.resources, "assets")

        self.background = pg.image.load(os.path.join(self.assets, "background.png"))
        self.background = pg.transform.scale(self.background, (800,600))

        self.scoreboard = pg.image.load(os.path.join(self.assets, "scoreboard_background.png"))
        self.scoreboard = pg.transform.scale(self.scoreboard, (440,440))

        self.character_idle = pg.image.load(os.path.join(self.assets, "character_idle.png"))
        self.character_idle = pg.transform.scale(self.character_idle, (40,80))
        
        self.character_run = pg.image.load(os.path.join(self.assets, "character_run.png"))
        self.character_run = pg.transform.scale(self.character_run, (60,80))
        self.character_run2 = pg.transform.flip(self.character_run, True, False)

        self.character_fall = pg.image.load(os.path.join(self.assets, "character_fall.png"))
        self.character_fall = pg.transform.scale(self.character_fall, (60,80))
        self.character_fall2 = pg.transform.flip(self.character_fall, True, False)

        self.character_preparing_jump = pg.image.load(os.path.join(self.assets, "character_preparing_jump.png"))
        self.character_preparing_jump = pg.transform.scale(self.character_preparing_jump, (60,80))

        self.character_jump = pg.image.load(os.path.join(self.assets, "character_jump.png"))
        self.character_jump = pg.transform.scale(self.character_jump, (60,80))
        self.character_jump2 = pg.transform.flip(self.character_jump, True, False)
        
        self.basic_plataform = pg.image.load(os.path.join(self.assets, "BasicPlataform.png"))
        self.basic_plataform = pg.transform.scale(self.basic_plataform, (150,50))
        
        self.ice_plataform = pg.image.load(os.path.join(self.assets, "IcePlataform.png"))
        self.ice_plataform = pg.transform.scale(self.ice_plataform, (150,50))

        self.button = pg.image.load(os.path.join(self.assets, "Button1.png"))
        self.button = pg.transform.scale(self.button, (150,50))
        self.button2 = pg.image.load(os.path.join(self.assets, "Button2.png"))
        self.button2 = pg.transform.scale(self.button2, (150,50))
        self.scores = os.path.join(self.resources, "score", "scores.pkl")

path_single = Path_Singleton()