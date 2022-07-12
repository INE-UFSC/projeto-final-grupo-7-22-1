

class Score:
    def __init__(self, name: str, score = 0):
        self.__name = name
        self.__score = score
    
    def string(self):
        return f"{self.__name}: {self.__score}"

    @property
    def name(self):
        return self.__name

    @property
    def score(self):
        return self.__score

    def increase_score(self, inc: int):
        self.__score += inc