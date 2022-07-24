import pygame as pg
import os

class Path_Singleton:
    def __init__(self):
        self.resources = os.path.dirname(__file__)
        self.assets = os.path.join(self.resources, "assets")

        self.player_idle = pg.image.load(os.path.join(self.assets, "character_idle.png"))
        self.player_idle = pg.transform.scale(self.player_idle, (40,80))
        
        self.player_run = pg.image.load(os.path.join(self.assets, "character_run.png"))
        self.player_run = pg.transform.scale(self.player_run, (2560,80))
        
        self.plataform = pg.image.load(os.path.join(self.assets, "Plataform1.png"))
        self.plataform = pg.transform.scale(self.plataform, (150,50))
        self.plataform2 = pg.image.load(os.path.join(self.assets, "Plataform2.png"))
        self.button = pg.image.load(os.path.join(self.assets, "Button1.png"))
        self.button = pg.transform.scale(self.button, (150,50))
        self.button2 = pg.image.load(os.path.join(self.assets, "Button2.png"))
        self.button2 = pg.transform.scale(self.button2, (150,50))
        self.scores = os.path.join(self.resources, "scores", "scores.pkl")
        

path_single = Path_Singleton()