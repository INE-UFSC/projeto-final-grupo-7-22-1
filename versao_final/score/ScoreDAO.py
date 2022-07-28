

from score.DAO import DAO
from score.Score import Score
from PathSingleton import path_single


class ScoreDAO(DAO):
    def __init__(self):
        super().__init__(path_single.scores)

    def add(self, score):
        if ((score is not None) and isinstance(score, Score)
           and isinstance(score.points, int)):
            if score not in super().get_all():
                super().add(score.name, score)
            else:
                s = super().get(score.name)
                if s and s.points < score.points:
                    super().add(score.name, score)

            if len(super().get_all()) > 10:
                s = min([sc.points for sc in super().get_all()])
                super().remove(s.name)

    def get(self, name):
        if isinstance(name, str):
            super().get(name)

    def remove(self, name):
        if isinstance(name, str):
            super().remove(name)
