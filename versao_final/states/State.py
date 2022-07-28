

from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self, controller):
        self.__controller = controller
    
    @property
    def controller(self):
        return self.__controller

    @abstractmethod
    def execute(self):
        pass

