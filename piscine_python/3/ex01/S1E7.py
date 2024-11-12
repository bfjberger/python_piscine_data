from S1E9 import Character


class Baratheon(Character):
    '''Class Baratheon docstring'''
    def __init__(self, name, is_alive=True):
        """docstring for constructor"""
        super().__init__(name, is_alive, "Baratheon", "brown", "dark")

    def alive(self):
        """docstring for Abstract method alive"""
        return self.is_alive

    def die(self):
        '''docstring for die function'''
        self.is_alive = False
        return self.is_alive

    def __str__(self):
        """Readable string for the object"""
        return f"Vector: ({self.name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        """Unambiguous representation of the object"""
        return f"Vector: ({self.name}, {self.eyes}, {self.hairs})"

class Lannister(Character):
    '''Class Lannister docstring'''
    def __init__(self, name, is_alive=True):
        """docstring for constructor"""
        super().__init__(name, is_alive, "Lannister", "blue", "light")

    def alive(self):
        """docstring for Abstract method alive"""
        return self.is_alive

    def die(self):
        '''docstring for die function'''
        self.is_alive = False
        return self.is_alive

    def __str__(self):
        """Readable string for the object"""
        return f"Vector: ({self.name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        """Unambiguous representation of the object"""
        return f"Vector: ({self.name}, {self.eyes}, {self.hairs})"

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """
        Create a Lannister character instance with custom is_alive status.

        Parameters:
            first_name (str): The first name of the character.
            is_alive (bool): The status of the character's life.
            cls refers to the class itself, a method that is defined on a
            class and can be called on the class itself,
            without creating an instance of the class.

        Returns:
            Lannister: An instance of the Lannister character.
        """
        instance = cls(first_name)
        instance.is_alive = is_alive
        return instance