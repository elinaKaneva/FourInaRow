from pygame import *
from pygamehelper import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform
import os

FPS = 40

# Colors:
WHITE = (255,255,255)
YELLOW = (235,235,0)
RED = (214,71,0)
BLUE = (0,102,153)
DARK_BLUE = (0,49,101)
LIGHT_BLUE = (185,231,255)

# Coordinates:
BOARD = (190, 240)
COLUMNS = [(190, 180), (250, 180), (310, 180), (370, 180), (430, 180), (490, 180), (550, 180)]
ROWS = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]

# Sizes:
STEP = 60

class Starter(PygameHelper):
    def __init__(self):
        self.w, self.h = 800, 600
        self.above_the_board = 0
        self.column = -1
        self.turn = 0
        self.pulls = [[[0,0]]*len(COLUMNS)]*len(ROWS)

        self.Surface = pygame.display.set_mode((self.w, self.h))

        PygameHelper.__init__(self, size=(self.w, self.h), fill=(LIGHT_BLUE))
        self.background = pygame.image.load(os.path.join("pics", "background.png"))
        self.cells = pygame.image.load(os.path.join("pics", "cells.png"))
        self.red_pull = pygame.image.load(os.path.join("pics", "red_pull.png"))
        self.yellow_pull = pygame.image.load(os.path.join("pics", "yellow_pull.png"))
        
    def update(self):
        pass
        
    def keyUp(self, key):
        pass
        
    def mouseUp(self, button, pos):
        x, y = pos[0], pos[1]
        
        for col in COLUMNS:
            if col[0] < x < col[0] + STEP:
                self.column = COLUMNS.index(col)
        else:
            self.above_the_board = 0
        
        
    def mouseMotion(self, buttons, pos, rel):
        x, y = pos[0], pos[1]
        
        if x in range(BOARD[0],BOARD[0] + len(COLUMNS) * STEP) and y in range(0,BOARD[1] + 1):
            self.above_the_board = 1
            for col in COLUMNS:
                if col[0] < x < col[0] + STEP:
                    self.column = COLUMNS.index(col)
        else:
            self.above_the_board = 0
        
    def draw(self):
        self.screen.fill(color=LIGHT_BLUE)
        if self.above_the_board == 1:
            self.screen.blit(self.red_pull, dest=COLUMNS[self.column])
            #self.screen.blit(self.yellow_pull, dest=COLUMNS[self.column])
        self.screen.blit(self.cells, dest=BOARD)
        
s = Starter()
s.mainLoop(FPS)
