

from Plataform import Plataform, PLATAFORM_TYPE


class Region:
    def __init__(self, filepath: str, width: int, height: int, offset: int):
        self.__layout = open(filepath, 'r').readlines()
        self.__offset = offset
        self.__plataforms = []

        self.init_plataforms(width, height)

    @property
    def offset(self):
        return self.__offset

    @property
    def plataforms(self):
        return self.__plataforms

    def init_plataforms(self, width: int, height: int):
        ypos = self.offset
        for line in self.__layout:
            ypos += 100
            temp_plat = []
            for xpos in line:
                temp_plat.append(Plataform((width*(xpos/100), ypos),(100,50), PLATAFORM_TYPE.BASIC, 'plataform.png'))
            self.plataforms.append(temp_plat)
    
    def update_region(self, vy):
        for step in self.plataforms:
            for plataform in step:
                plataform.update_movement(0, vy)
                plataform.move()