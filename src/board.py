import numpy as np

class Board:
    """
    Class representing the game board.

    Attributes:
        matrix (numpy.ndarray): The game board represented as a 2D numpy array.

    Methods:
        __init__(): Initializes the game board with zeros.
        print(): Prints the game board, flipping it vertically.
    """

    def __init__(self, row_count, col_count):
        """
        Initializes the game board with zeros.
        """
        self.row_count = row_count
        self.col_count = col_count
        self.matrix = np.zeros((self.row_count, self.col_count))
    
    def print(self):
        """
        Prints the game board, flipping it vertically.
        Currently it does not affect the view perspective (since only zeroes are present), 
        but this will be useful to create an actual image of game board
        along the game progression (tokens are 'dropped' to the bottom of the board)
        """
        print(np.flip(self.matrix, 0))
    
    def drop_piece(self, row: int, col: int, piece):
        self.matrix[row][col] = piece

    def can_drop_in_column(self, col: int):
        return self.matrix[self.rows-1][col] == 0

    def get_row_to_drop(self, col):
        for r in range(self.rows):
            if self.matrix[r][col] == 0:
                return r
