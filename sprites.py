
# Sprite classes for platform game
# © 2019 KidsCanCode LLC / All rights reserved.
import pygame
import pygame as pg
from pygame.sprite import Sprite
from settings import *
vec = pg.math.Vector2
screen = pygame.display.set_mode((WIDTH,HEIGHT))
#class and superclass with game image and player variables
class Player(Sprite):
    # include game parameter to pass game class as argument in main...
    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((50, 40))
        #color of player
        self.image.fill(LIGHTBLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.hitpoints = 100
    def pew(self):
        lazer = Pewpew(self.game, self.pos.x + self.rect.width/2, self.pos.y, 10, 10)
        # print("trying to pewpewpew")
        self.game.all_sprites.add(lazer)
        # self.game.platforms.add(lazer)
        self.game.projectiles.add(lazer)
    #nothing much here yet...
    def myMethod(self):
        pass
    #jump fn with self, makes the player travel vertically upwards.
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        self.game.screen.fill(BLUE)
        
        if hits: 
            self.vel.y = -10
    #updates self when keys pressed
    def update(self):
        self.acc = vec(0, 0.5)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_d]:
            self.acc.x = PLAYER_ACC
        if keys[pg.K_w]:
            self.acc.y = -PLAYER_ACC
        if keys[pg.K_s]:
            self.acc.y = PLAYER_ACC
        # ALERT - Mr. Cozort did this WAY differently than Mr. Bradfield...
        #thats ok Mr. Cozort
        #calls jump fn when we hit spacebar
        if keys[pg.K_SPACE]:
            self.jump()
            
        if keys[pg.K_w]:
            self.jump()

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # self.acc.y += self.vel.y * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        #if player runs outside of the screen, it teleports it to the other side.

        #doesn't work really, other than moving the player.
        if self.pos.x > WIDTH:
            self.pos.x = 0
            screen.fill(WHITE)
            #pygame.display.flip()
        if self.pos.x < 0:
            self.pos.x = WIDTH
            #screen.fill(WHITE)
            #pygame.display.flip()
        if self.pos.y < 0:
            self.pos.y = HEIGHT
            #screen.fill(WHITE)
            #pygame.display.flip()
        if self.pos.y > HEIGHT:
            self.pos.y = 0
            #screen.fill(WHITE)
            #pygame.display.flip()

        self.rect.midbottom = self.pos
#platform sprite. has settings like the self init and color and w and h
class Platform(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    #making the class for bullets
class Pewpew(Sprite):
    #defines the init (self init)
    def __init__(self, game, x, y, w, h):
        Sprite.__init__(self)
        #defining some self attributes for pewpew
        self.game = game
        self.image = pg.Surface((w, h))
        #color
        self.image.fill(LIGHTBLUE)
        #shape
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.birth = time.perf_counter_ns()
        #how long it stays on screen (1 sec)
        self.lifespan = 1000000000
    #updating for pewpews, shooting moves bullet
    def update(self):
        #changed to lower jump magnitude.
        self.rect.y -= 5
        self.now = time.perf_counter_ns()
        if self.now - self.birth > self.lifespan:
            self.kill()
