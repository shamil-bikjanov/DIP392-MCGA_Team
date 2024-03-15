import numpy as np

class Board:
    def __init__(self, row: int, col: int):
        self.row: int = row
        self.col: int = col
        
        self.board = np.zeros((row, col))
        
    def print(self):
        print(np.flip(self.board, 0))
