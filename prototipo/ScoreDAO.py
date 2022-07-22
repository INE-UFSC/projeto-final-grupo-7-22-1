

from DAO import DAO
from Score import Score
from PathSingleton import path_single


class ScoreDAO(DAO):
    def __init__(self):
        super().__init__(path_single.scores)

    def add(self, score):
        if ((score is not None) and isinstance(score, Score)
           and isinstance(score.points, int)):
            scores = super().get_all()
            if len(scores) < 10:
                super().add(score.name, score)
            else:
                s = min([sc.points for sc in scores])
                if score.points >= s:
                    super().add(score.name, score)
                    super().remove(s.name)

    def get(self, name):
        if isinstance(name, str):
            super().get(name)

    def remove(self, name):
        if isinstance(name, str):
            super().remove(name)
