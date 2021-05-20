import pygame as pg
from random import choice, randrange
from os import path
vec = pg.math.Vector2
from settings import *
# class Player(pg.sprite.Sprite):
#     def __init__(self, game, x, y, spawn_loc):
#         self.groups = game.all_sprites
#         pg.sprite.Sprite.__init__(self, self.groups)
#         self.game = game
#         self.image = pg.Surface((25, 25))
#         self.image.fill(RED)
#         self.rect = self.image.get_rect()
#         self.rect.center = spawn_loc
#         self.vel = vec(0, 0)
#         self.vx, self.vy = 0, 0
#         self.x = x * TILE_SIZE
#         self.y = y * TILE_SIZE
#
#     def get_keys(self):
#         self.vx, self.vy = 0, 0
#         keys = pg.key.get_pressed()
#         if keys[pg.K_LEFT] or keys[pg.K_a]:
#             self.vx = -PLAYER_SPEED
#         if keys[pg.K_RIGHT] or keys[pg.K_d]:
#             self.vx = PLAYER_SPEED
#         if keys[pg.K_UP] or keys[pg.K_w]:
#             self.vy = -PLAYER_SPEED
#         if keys[pg.K_DOWN] or keys[pg.K_s]:
#             self.vy = PLAYER_SPEED
#         if self.vx != 0 and self.vy != 0:
#             self.vx *= 0.7071
#             self.vy *= 0.7071
#
#     def collide_with_walls(self, dir):
#         if dir == "x":
#             hits = pg.sprite.spritecollide(self, self.game.walls, False)
#             if hits:
#                 if self.vx > 0:
#                     self.x = hits[0].rect.left - self.rect.width
#                 if self.vx < 0:
#                     self.x = hits[0].rect.right
#                 self.vx = 0
#                 self.rect.x = self.x
#         if dir == "y":
#             hits = pg.sprite.spritecollide(self, self.game.walls, False)
#             if hits:
#                 if self.vy > 0:
#                     self.y = hits[0].rect.top - self.rect.height
#                 if self.vy < 0:
#                     self.y = hits[0].rect.bottom
#                 self.vy = 0
#                 self.rect.y = self.y
#     def update(self):
#         hits = pg.sprite.spritecollide(self, self.game.checkpoints, False)
#         if hits:
#             self.game.player_spawn_points[self.game.level_index] = hits[0].rect.center
#             self.game.coin_prev = []
#             if hits[0].end and not len(self.game.coin):
#                 self.game.reset_object()
#                 self.game.load_level()
#         coin_hits = pg.sprite.spritecollide(self, self.game.coin, False)
#         if coin_hits:
#             self.game.coin_prev.append((coin_hits[0].x, coin_hits[0].y))
#             coin_hits[0].kill()
class Player(pg.sprite.Sprite):
    def __init__(self,game, spawn_loc):

        self.groups = game.all_sprites,game.players_group
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = pg.Surface((25,25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = spawn_loc
        self.speedx = 4
        self.speedy = 4
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def update(self):


        if self.move_right:
            self.rect.x+= self.speedx
        if self.move_left:
            self.rect.x-= self.speedx
        if self.move_up:
            self.rect.y-= self.speedy
        if self.move_down:
            self.rect.y+= self.speedy
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        if self.rect.bottom >= HEIGHT:
             self.rect.bottom = HEIGHT
        if self.rect.left < 0:
             self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        hits = pg.sprite.spritecollide(self, self.game.checkpoints, False)
        if hits:
            self.game.player_spawn_points[self.game.level_index] = hits[0].rect.center
            self.game.coin_prev = []
            if hits[0].end and not len(self.game.coin):
                self.game.reset_object()
                self.game.load_level()
        coin_hits = pg.sprite.spritecollide(self, self.game.coin, False)
        if coin_hits:
            self.game.coin_prev.append((coin_hits[0].x, coin_hits[0].y))
            coin_hits[0].kill()


class Mob(pg.sprite.Sprite):
    def __init__(self, game, d, x, y, speed=7):
        self.groups = game.all_sprites, game.mobs
        self.game = game
        super(Mob, self).__init__(self.groups)
        self.image = pg.Surface((15, 15))
        self.color = BLUE
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (x+TILE_SIZE//2, y+TILE_SIZE//2)
        self.speed = speed
        self.dir = d
        # circling
        self.center_x = self.rect.centerx
        self.center_y = self.rect.centery
        if self.dir == 1:
            self.vel = vec(self.speed, 0)
        else:
            self.vel = vec(0, self.speed)

    def update(self):
        self.rect.center += self.vel
        mob_wall_hits = pg.sprite.spritecollide(self, self.game.walls, False)
        if mob_wall_hits:
            self.vel.x *= -1
            self.vel.y *= -1
        mob_checkpoint_hits = pg.sprite.spritecollide(self, self.game.checkpoints, False)
        if mob_checkpoint_hits:
            self.vel.x *= -1
            self.vel.y *= -1


class Walls(pg.sprite.Sprite):
    def __init__(self,game,x,y,w,h):
        self.groups = game.all_sprites,game.walls
        pg.sprite.Sprite.__init__(self,self.groups)
        self.image = pg.Surface((w, h))
        self.color = PURPLE
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (x+TILE_SIZE//2, y+TILE_SIZE//2)

class Checkpoint(pg.sprite.Sprite):
    def __init__(self,game,x,y,w,h,end):
        self.groups = game.all_sprites, game.checkpoints
        pg.sprite.Sprite.__init__(self,self.groups)
        self.image = pg.Surface((w, h))
        self.game = game
        self.color = GREEN
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (x + TILE_SIZE // 2, y + TILE_SIZE // 2)
        self.end = end

class Coin(pg.sprite.Sprite):
    def __init__(self,game,x,y,w,h):
        self.groups = game.all_sprites,game.coin
        pg.sprite.Sprite.__init__(self,self.groups)
        self.image = pg.Surface((w, h))
        self.color = YELLOW
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x+TILE_SIZE//2, y+TILE_SIZE//2)

class Player_walls(pg.sprite.Sprite):
    def __init__(self,game,x,y,w,h):
        self.groups = game.all_sprites,game.player_walls
        pg.sprite.Sprite.__init__(self,self.groups)
        self.image = pg.Surface((w, h))
        self.color = PURPLE
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (x+TILE_SIZE//2, y+TILE_SIZE//2)

