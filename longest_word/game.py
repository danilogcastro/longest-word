# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import random
import string
import requests
import json

class Game:
    """A class to create the longest word game"""
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = random.choices(string.ascii_uppercase,k=9)

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if not self.is_in_dictionary(word):
            return False

        for letter in word:
            if letter not in self.grid:
                return False

            self.grid.remove(letter)

        return True

    @staticmethod
    def is_in_dictionary(word):
        api_response = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}").json()

        return api_response['found']

if __name__ == "__main___":
    pass
