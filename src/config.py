class Config:
    """
    This class represents the configuration for a game board.
    It defines the colors and dimensions of the game board.

    Attributes:
        Colors are defined as tuple parameters with RGB values:
            BLUE  : values for the color blue.
            BLACK : color black is represented as zeros.
            RED   : RGB values for the color red.
            YELLOW: RGB values for the color yellow (combination of values for red and green).
        row_count (integer)   : The number of rows for our game board.
        column_count (integer): The number of columns for our game board.
    """
    
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    SQUARESIZE = 100
    RADIUS = int(SQUARESIZE/2 - 5)

    row_count = 6
    column_count = 7