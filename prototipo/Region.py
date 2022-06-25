

from Plataform import PLATAFORM_TYPE
from BasicPlataform import BasicPlataform


class Region:
    def __init__(self, filepath: str, width: int, height: int, offset: int):
        self.__layout = open(filepath, 'r').readlines()
        self.__offset = offset
        self.__plataforms = []

        self.init_plataforms(width, height)

    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, offset):
        self.__offset = offset

    @property
    def plataforms(self):
        return self.__plataforms

    def init_plataforms(self, width: int, height: int):
        ypos = self.offset
        
        for line in self.__layout:
            ypos += 150
            temp_plat = []
            for xpos in line.split(sep=','):
                temp_plat.append(BasicPlataform((width*(int(xpos)/100), ypos),(100,50), PLATAFORM_TYPE.BASIC, 'plataform.png'))
            self.plataforms.append(temp_plat)
    
    def update_region(self, vy):
        self.offset += vy
        for step in self.plataforms:
            for plataform in step:
                plataform.update_movement(0, vy)
                plataform.move()