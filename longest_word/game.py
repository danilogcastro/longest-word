# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import random
import string

class Game:
    """A class to create the longest word game"""
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = random.choices(string.ascii_uppercase,k=9)

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        for letter in word:
            if letter not in self.grid:
                return False

            self.grid.remove(letter)

        return True

if __name__ == "__main___":
    pass
