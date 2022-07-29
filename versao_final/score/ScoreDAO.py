

from score.DAO import DAO
from score.Score import Score
from PathSingleton import path_single


class ScoreDAO(DAO):
    def __init__(self):
        super().__init__(path_single.scores)

    def add(self, score):
        if ((score is not None) and isinstance(score, Score)
            and isinstance(score.points, int)):
            # Verifica se há mais de 10 pontuações salvas
            if len(super().get_all()) > 10:
                # Determina menor pontução
                min_score = score
                for sc in super().get_all():
                    if sc.points < min_score.points:
                        min_score = sc
                # Se a pontuação estiver entre as 10 melhores a adciona e remove a pior
                if min_score != score:
                    super().remove(id(min_score))
                    super().add(id(score), score)
            else:
                super().add(id(score), score) # Adciona diretamente se houver menos de 10 pontuações salvas

    def get(self, name):
        if isinstance(name, str):
            super().get(name)

    def remove(self, name):
        if isinstance(name, str):
            super().remove(name)
