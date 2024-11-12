from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class Character"""

    def __init__(self, name, is_alive=True):
        """docstring for Constructor"""
        self.name = name
        self.is_alive = is_alive

    @abstractmethod
    def alive(self):
        """docstring for Abstract Method"""
        pass

    @abstractmethod
    def die(self):
        """docstring for Abstract Method"""
        pass



class Stark(Character):
    """inherite from Class Character"""
    def __init__(self, name, is_alive=True):
        """docstring for constructor"""
        # super method alows the girl class to call the mother class init function
        # if not called youhave to define yourself the value name and is_alive
        super().__init__(name, is_alive)

    def alive(self):
        """docstring for Abstract method alive"""
        if self.is_alive == False:
            return self.is_alive
        else:
            self.is_alive = True
        return self.is_alive

    def die(self):
        '''docstring for die function'''
        self.is_alive = False
        return self.is_alive

