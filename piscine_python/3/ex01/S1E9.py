from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class Character"""
    @abstractmethod
    def __init__(self, name, is_alive, family_name, eyes, hairs):
        """docstring for Constructor"""
        self.name = name
        self.is_alive = is_alive
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

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
        super().__init__(name, is_alive)

    def alive(self):
        """docstring for Abstract method alive"""
        return self.is_alive

    def die(self):
        '''docstring for die function'''
        self.is_alive = False
        return self.is_alive

