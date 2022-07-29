

from abc import ABC, abstractmethod


# Representa estado atual
class State(ABC):
    def __init__(self, controller):
        self.__controller = controller
    
    @property
    def controller(self):
        return self.__controller

    # Determina rotina a ser executada pelo controller
    @abstractmethod
    def execute(self):
        pass

