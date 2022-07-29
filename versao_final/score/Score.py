

class Score:
    def __init__(self, name: str, points = 0):
        self.__name = name
        self.__points = points
    
    def string(self):
        return f"{self.__name}: {self.__points}"

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def points(self):
        return self.__points

    # Aumenta pontuação
    # @param inc -> Determina aumento da pontuação
    def increase_score(self, inc: int):
        self.__points += inc