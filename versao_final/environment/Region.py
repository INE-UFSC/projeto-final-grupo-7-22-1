

from entities.Plataform import PLATAFORM_TYPE
from entities.PlataformCreator import PlatafromCreator
from ConstantSingleton import const_single
from random import choices
class Region:
    def __init__(self, filepath: str, width: int, height: int, offset: int):
        self.__layout = open(filepath, 'r').readlines()
        self.__offset = offset
        self.__objects = []

        self.init_plataforms(width, height)

    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, offset):
        self.__offset = offset

    @property
    def objects(self):
        return self.__objects

    def init_plataforms(self, width: int, height: int):
        ypos = self.offset
        types = list(PLATAFORM_TYPE)
        for line in self.__layout:
            ypos += const_single.yoffset
            temp_plat = []
            for xpos in line.split(sep=','):
                temp_plat.append(PlatafromCreator.create_plataform((width*(int(xpos)/100), ypos), choices(types, [t.value for t in types], k= 1)[0]))
            self.objects.append(temp_plat)
    
    # Atualiza posição da região
    def update_region(self, vy):
        self.offset += vy
        for step in self.objects:
            for obj in step:
                obj.update_movement(0, vy)
                obj.move()