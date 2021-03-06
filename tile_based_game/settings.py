import pygame as pg
vec = pg.math.Vector2

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)

# game options
TITLE = "Tile Map Demo"
WIDTH = 1024
HEIGHT = 768
FPS = 60
BGCOLOR = BROWN

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG = "tile_15.png"
GRASS_IMG = "tile_01.png"
# player settings
PLAYER_HEALTH = 100
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'manBlue_gun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(30, 10)

# gun settings
BULLET_IMG = "tile_187.png"
BULLET_SPEED = 500
BULLET_LIFTIME = 1000
BULLET_RATE = 150
KICKBACK = 200
GUN_SPREAD = 5
BULLET_DMG = 10


# mob settings
MOB_IMG = "zoimbie1_hold.png"
MOB_SPEED = [150, 100, 125, 75, 150, 175]
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
MOB_HEALTH = 100
MOB_DMG = 10
MOB_KNOCKBACK = 20
AVOID_RADIUS = 50
DETECT_RADIUS = 500
