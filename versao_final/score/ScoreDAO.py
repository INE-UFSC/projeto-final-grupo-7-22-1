

from score.DAO import DAO
from score.Score import Score
from PathSingleton import path_single


class ScoreDAO(DAO):
    def __init__(self):
        super().__init__(path_single.scores)

    def add(self, score):
        if ((score is not None) and isinstance(score, Score)
            and isinstance(score.points, int)):
            if len(super().get_all()) > 10:
                min_score = score
                for sc in super().get_all():
                    if sc.points < min_score.points:
                        min_score = sc
                if min_score != score:
                    super().remove(id(min_score))
                    super().add(id(score), score)
            else:
                super().add(id(score), score)

    def get(self, name):
        if isinstance(name, str):
            super().get(name)

    def remove(self, name):
        if isinstance(name, str):
            super().remove(name)
