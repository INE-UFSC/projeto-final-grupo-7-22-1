

from Plataform import PLATAFORM_TYPE
from BasicPlataform import BasicPlataform


class Region:
    def __init__(self, filepath: str, width: int, height: int, offset: int, img):
        self.__layout = open(filepath, 'r').readlines()
        self.__offset = offset
        self.__objects = []

        self.init_plataforms(width, height, img)

    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, offset):
        self.__offset = offset

    @property
    def objects(self):
        return self.__objects

    def init_plataforms(self, width: int, height: int, img):
        ypos = self.offset
        for line in self.__layout:
            ypos += 150
            temp_plat = []
            for xpos in line.split(sep=','):
                temp_plat.append(BasicPlataform((width*(int(xpos)/100), ypos),(100,50), PLATAFORM_TYPE.BASIC, img))
            self.objects.append(temp_plat)
    
    def update_region(self, vy):
        self.offset += vy
        for step in self.objects:
            for obj in step:
                obj.update_movement(0, vy)
                obj.move()