

from DAO import DAO
from Score import Score
from PathSingleton import path_single


class ScoreDAO(DAO):
    def __init__(self):
        super().__init__(path_single.scores)

    def add(self, score):
        if ((score is not None) and isinstance(score, Score)
           and isinstance(score.score, int)):
            super().add(score.name, score)

    def get(self, name):
        if isinstance(name, str):
            super().get(name)

    def remove(self, name):
        if isinstance(name, str):
            super().remove(name)
