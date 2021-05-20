import pygame as pg
import random as r
from os import path

TITLE = "Test"


# game settings
WIDTH = 512
HEIGHT = 448
FPS = 60
TILE_SIZE = 32
PLAYER_SPEED = 4



# strating platforms
WALLS_LIST = [(0, HEIGHT - 60)]

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (175, 0, 175)
CORNFLOWER_BLUE = (100, 145, 245)
BGCOLOR = CORNFLOWER_BLUE
