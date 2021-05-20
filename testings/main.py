import pygame as pg
import random as r

from sprites import *
from settings import *
vec = pg.math.Vector2
from os import path

class Game(object):

    def __init__(self):
        self.running = True
        # initialize pygame and create window
        pg.init()
        pg.mixer.init()   # for sound
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()

    def reset_object(self):
        for sprite in self.all_sprites:
            sprite.kill()

    def load_level(self):
        self.level_index += 1
        level_dir = path.join(self.game_dir, "maps")
        file = open(path.join(level_dir, f"level{self.level_index}.txt"), 'r')
        level = file.read()
        game = level.split('\n')
        game_map = []
        for i in range(len(game)):
            game_map.append([])
            for letter in game[i]:
                game_map[i].append(letter)
        file.close()
        for i in range(len(game_map)):
            for j in range(len(game_map[i])):
                if game_map[i][j] == 'w':
                    Walls(self, j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                elif game_map[i][j] == 'm':
                    Mob(self, 1, j * TILE_SIZE, i * TILE_SIZE)
                elif game_map[i][j] == "M":
                    Mob(self, -1, j * TILE_SIZE, i * TILE_SIZE)
                elif game_map[i][j] == 's':
                    Checkpoint(self, j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE, False)
                elif game_map[i][j] == 'S':
                    Checkpoint(self, j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE, True)
                elif game_map[i][j] == 'c':
                    Coin(self, j * TILE_SIZE, i * TILE_SIZE, 15, 15)
                elif game_map[i][j] == '!':
                    Mob(self, 1, j * TILE_SIZE, i * TILE_SIZE, 3)
                elif game_map[i][j] == 'W':
                    Player_walls(self, j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        self.player = Player(self, self.player_spawn_points[self.level_index])

    def new(self):
        # create sprite groups
        self.game_dir = path.dirname(__file__)
        self.level_index = -1
        self.player_spawn_points = [(WIDTH//30, HEIGHT*41//50), (WIDTH*2//13, HEIGHT*1//2), (WIDTH//30, HEIGHT*41//50),
                                    (WIDTH//30, HEIGHT*3//5), (WIDTH//30, HEIGHT*4//5), (WIDTH//30, HEIGHT*11//50),
                                    (WIDTH//30, HEIGHT//2)]
        self.coin_prev = []
        self.all_sprites = pg.sprite.Group()
        self.coin = pg.sprite.Group()
        self.checkpoints = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.players_group = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.player_walls = pg.sprite.Group()
        self.load_level()

        # create game objects
        # self.mob = Mob(1, WIDTH//2, HEIGHT//4)

        # add game objects to groups
        # self.all_sprites.add(self.mob)
        #
        #
        # self.mobs.add(self.mob)


        # start running game loop


        self.run()

    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    self.player.move_right = True
                if event.key == pg.K_LEFT:
                    self.player.move_left = True
                if event.key == pg.K_UP:
                    self.player.move_up = True
                if event.key == pg.K_DOWN:
                    self.player.move_down = True
            if event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT:
                    self.player.move_right = False
                if event.key == pg.K_LEFT:
                    self.player.move_left = False
                if event.key == pg.K_UP:
                    self.player.move_up = False
                if event.key == pg.K_DOWN:
                    self.player.move_down = False



    def update(self):
        self.all_sprites.update()

        # hit mobs?
        mob_hits = pg.sprite.spritecollide(self.player, self.mobs, False)
        if mob_hits:
            self.player.rect.center = self.player_spawn_points[self.level_index]
            if self.coin_prev:
                for coin in self.coin_prev:
                    Coin(self, coin[0], coin[1], 15, 15)

        # collide with walls
        # if dir == 'x':
        wall_hits = pg.sprite.spritecollide(self.player, self.walls, False)
        player_wall_hits = pg.sprite.spritecollide(self.player, self.player_walls, False)
        #     if wall_hits:
        #         if self.vx > 0:
        #             self.x = wall_hits[0].rect.left - self.rect.width
        #         if self.vx < 0:
        #             self.x = wall_hits[0].rect.right
        #         self.vx = 0
        #         self.rect.x = self.x
        # if dir == 'y':
        #     wall_hits = pg.sprite.spritecollide(self.player, self.walls, False)
        #     if wall_hits:
        #         if self.vy > 0:
        #             self.y = wall_hits[0].rect.left - self.rect.width
        #         if self.vy < 0:
        #             self.y = wall_hits[0].rect.right
        #         self.vy = 0
        #         self.rect.y = self.y


        if wall_hits and self.player.move_up:
            self.player.move_up = False
            self.player.rect.top = wall_hits[0].rect.bottom
        if wall_hits and self.player.move_down:
            self.player.move_down = False
            self.player.rect.bottom = wall_hits[0].rect.top
        if wall_hits and self.player.move_left:
            self.player.move_left = False
            self.player.rect.left = wall_hits[0].rect.right
        if wall_hits and self.player.move_right:
            self.player.move_right = False
            self.player.rect.right = wall_hits[0].rect.left

        if player_wall_hits and self.player.move_up:
            self.player.move_up = False
            self.player.rect.top = player_wall_hits[0].rect.bottom
        if player_wall_hits and self.player.move_down:
            self.player.move_down = False
            self.player.rect.bottom = player_wall_hits[0].rect.top
        if player_wall_hits and self.player.move_left:
            self.player.move_left = False
            self.player.rect.left = player_wall_hits[0].rect.right
        if player_wall_hits and self.player.move_right:
            self.player.move_right = False
            self.player.rect.right = player_wall_hits[0].rect.left

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)

        pg.display.flip()

    def show_start_screen(self):
        # show start screen
        pass

    def show_GO_screen(self):
        pass


g = Game()
g.show_start_screen()
while g.running:
    g.new()

    g.show_GO_screen()

pg.quit()