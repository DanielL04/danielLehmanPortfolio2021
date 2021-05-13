# Pygame template
import pygame as pg
import random as r
from os import path

TITLE = "Jumper"

game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, "img")
snd_folder = path.join(game_folder, "img")

# game settings
WIDTH = 480
HEIGHT = 600
FPS = 60
FONT_NAME = "arial"
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"

# player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20

# Game properties
BOOST_POWER = 60
POW_SPAWN_PCT = 7
MOB_FREQ = 5000
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POW_LAYER = 1
MOB_LAYER = 2
CLOUD_LAYER = 0

# strating platforms
PLATFORM_LIST = [(0, HEIGHT - 60),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4),
                 (125, HEIGHT - 350),
                 (350, 200),
                 (175, 100)]

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




# class Walls(pg.sprite.Sprite):
#     def __init__(self):
#         super(Walls, self).__init__()
#         self.image = pg.Surface((WIDTH, 50))
#         self.color = BLUE
#         self.image.fill(self.color)
#         self.rect = self.image.get_rect()
#         self.rect.center = (WIDTH / 2, HEIGHT - 25)

