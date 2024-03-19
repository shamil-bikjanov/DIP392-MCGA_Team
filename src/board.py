import numpy as np
from config import Config

class Board:
    """
    Class representing the game board.

    Attributes:
        board (numpy.ndarray): The game board represented as a 2D numpy array.

    Methods:
        __init__(): Initializes the game board with zeros.
        print(): Prints the game board, flipping it vertically.
    """

    def __init__(self):
        """
        Initializes the game board with zeros.
        """
        self.board = np.zeros((Config.row_count, Config.column_count))
    
    def print(self):
        """
        Prints the game board, flipping it vertically.
        Currently it does not affect the view perspective (since only zeroes are present), 
        but this will be useful to create an actual image of game board
        along the game progression (tokens are 'dropped' to the bottom of the board)
        """
        print(np.flip(self.board, 0))
