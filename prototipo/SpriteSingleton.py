import pygame as pg
import os

class Sprite_Singleton:
    def __init__(self):
        self.resources = os.path.dirname(__file__)
        self.assets = os.path.join(self.resources, "assets")
        self.player = pg.image.load(os.path.join(self.assets, "hitbox.png"))
        self.plataform = pg.image.load(os.path.join(self.assets, "Plataform.png"))

Sprite_Single = Sprite_Singleton()