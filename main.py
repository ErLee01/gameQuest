# KidsCanCode - Game Development with Pygame video series
# Jumpy! (a platform game) - Part 2
# Video link: https://www.youtube.com/watch?v=8LRI0RLKyt0
# Player movement
# © 2019 KidsCanCode LLC / All rights reserved.

# Week of march 23 - Lore
# Modules, Github, import as, 


#Imports
import pygame
import pygame as pg
from pygame.sprite import Group
# from pg.sprite import Group
import random
from settings import *
from sprites import *

#screen = pygame.display.set_mode((w,h))

#Class for game (init self and makes platforms/sprites)
class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        #sets screen to width and height
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
#superclass with the new class to spawn in sprites and player etc..
    def new(self):
        # start a new game
        self.all_sprites = Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        ground = Platform(0, HEIGHT-40, WIDTH, 40)
        #variables for platorms, specs
        plat1 = Platform(200, 400, 150, 20)
        plat2 = Platform(150, 300, 150, 20)
        #adding in the ground, and platforms.
        self.all_sprites.add(ground)
        self.platforms.add(ground)
        self.all_sprites.add(plat1)
        self.platforms.add(plat1)
        self.all_sprites.add(plat2)
        self.platforms.add(plat2)
        #spawns in a number of platforms from the given range.
        for plat in range(1,5):
            plat = Platform(random.randint(0, WIDTH), random.randint(0, HEIGHT), 200, 20)
            self.all_sprites.add(plat)
            self.platforms.add(plat)
        self.run()
    #fn for the game to auto run
    def run(self):
        # Game Loop
        self.playing = True
        #while loop, calls self to do things, like draw in the game and update.
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            self.screen.fill(WHITE)
    #use this later to have the sprite not hit platforms from x 
    def update(self):
        #Game Loop - Update
        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        #teleports player above the platform if it hits the platform.
        if hits:
            self.player.pos.y = hits[0].rect.top+1
            self.player.vel.y = 0

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

#background
background = pygame.image.load('background1.jpg')

def draw(self):
    # Game Loop - draw
    self.screen.blit (background, (0,0))
    self.all_sprites.draw(self.screen)
    #*after* drawing everything, flip the display
    pg.display.flip()

def show_start_screen(self):
    #game splash/start screen
    pass

def show_go_screen(self):
    #game over/continue
    pass

#more global variables, game for showing screens.
g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
