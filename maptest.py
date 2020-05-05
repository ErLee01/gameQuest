#Ethan Lee
'''
Basically for the map design:
We need rooms with an entrance and an exit (but the entrance must close so the player cannot return (way too much code) 
Every time a player enters a room, it calls a "random" function (probably with numbers EX: 1849 which then moves into if statements saying if the first digit is 1 then spawn in a monster, if the 2nd digit is 8 don't spawn a fountain, etc...
(where each of the digits determine one quality (prob a toggle so either it spawns in something or it doesnt)
sooooo (0 or 1 or 1 or 2 or something)
'''
import pygame
import os
import math
import random
from random import *
class Seed:
    for x in range(10):
        print random.randint(1,101)
Seed()