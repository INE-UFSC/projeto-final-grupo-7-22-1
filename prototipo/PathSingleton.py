import pygame as pg
import os

class Path_Singleton:
    def __init__(self):
        self.resources = os.path.dirname(__file__)
        self.assets = os.path.join(self.resources, "assets")
        self.player = pg.image.load(os.path.join(self.assets, "hitbox.png"))
        self.plataform = pg.image.load(os.path.join(self.assets, "Plataform.png"))
        self.scores = os.path.join(self.resources, "scores", "scores.pkl")

path_single = Path_Singleton()