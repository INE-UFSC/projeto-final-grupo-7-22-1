

from entities.BasicPlataform import BasicPlataform
from entities.IcePlataform import IcePlataform
from entities.Plataform import PLATAFORM_TYPE
from PathSingleton import path_single

# Retorna plataforma de acordo com o tipo informado
class PlatafromCreator:
    def create_plataform(pos: tuple, type: PLATAFORM_TYPE):
        w = {
            PLATAFORM_TYPE.BASIC : BasicPlataform(pos, type, path_single.basic_plataform),
            PLATAFORM_TYPE.ICE : IcePlataform(pos, type, path_single.ice_plataform)
        }
        return w[type]