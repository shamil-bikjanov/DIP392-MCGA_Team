import pygame
import sys
from board import Board  # Importing the Board class from the board module
from config import Config  # Importing the Config class from the config module

class UIManager:
    def __init__(self):
        """
        Initializes the game board with zeros.
        """
        self.board = Board(Config.row_count, Config.column_count)

    def calculate_size(self):
        width = Config.column_count * Config.SQUARESIZE
        height = (Config.row_count+1) * Config.SQUARESIZE
        return (width, height)

    def draw_board(self):
        size = self.calculate_size()
        screen = pygame.display.set_mode(size)
        SQUARESIZE = Config.SQUARESIZE
        RADIUS = Config.RADIUS
        for c in range(Config.column_count):
            for r in range(Config.row_count):
                pygame.draw.rect(screen, Config.BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(screen, Config.BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
        
        for c in range(Config.column_count):
            for r in range(Config.row_count):		
                if self.board.matrix[r][c] == 1:
                    pygame.draw.circle(screen, Config.RED, (int(c*SQUARESIZE+SQUARESIZE/2), size[1]-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                elif self.board.matrix[r][c] == 2: 
                    pygame.draw.circle(screen, Config.YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), size[2]-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
        pygame.display.update()
    
    def start(self):
        pygame.init()
        self.draw_board()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()