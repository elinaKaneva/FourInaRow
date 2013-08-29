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
NICE_BLUE = (202,202,255)

# Coordinates:
BOARD = (190, 240)
COLUMNS = [190, 250, 310, 370, 430, 490, 550]
ROWS = [0, 0, 0, 0, 0, 0]

# Sizes:
STEP = 60

class Starter(PygameHelper):
    def __init__(self):
        self.w, self.h = 800, 600
        self.over_the_board = 0
        self.head_column = -1
        self.col = -1
        self.row = -1
        self.turn = 9
        self.move = 0
        self.free_space = 0
        self.pulls = [[0 for y in range(len(COLUMNS))] for x in range(len(ROWS))]

        self.Surface = pygame.display.set_mode((self.w, self.h))

        PygameHelper.__init__(self, size=(self.w, self.h), fill=(LIGHT_BLUE))
        self.background = pygame.image.load(os.path.join("pics", "background.png"))
        self.below_board = pygame.image.load(os.path.join("pics", "below_board.png"))
        self.board = pygame.image.load(os.path.join("pics", "board.png"))
        self.red_pull = pygame.image.load(os.path.join("pics", "red_pull.png"))
        self.yellow_pull = pygame.image.load(os.path.join("pics", "yellow_pull.png"))
        
    def update(self):
        pass

    def keyUp(self, key):
        pass
        
    def mouseUp(self, button, pos):
        x, y = pos[0], pos[1]
        self.free_space = 0
        self.move = 0

        if button == 1:
            for column in COLUMNS:
                if column < x < column + STEP:
                    self.col = COLUMNS.index(column)
                    print("click col index:", self.col)
                    self.move = 1
                    break
            if self.move == 1:
                for each_row in self.pulls:
                    if each_row[self.col] == 0:
                        self.free_space += 1
                print("free space: ", self.free_space)
                if self.free_space > 0:
                    self.row = self.free_space - 1
                    print("click row index:", self.row)
                    self.pulls[self.row][self.col] = 1
                    print("Board:")
                    print(self.pulls)
                    
                    

    def mouseMotion(self, buttons, pos, rel):
        x, y = pos[0], pos[1]
        
        if x in range(BOARD[0],BOARD[0] + len(COLUMNS) * STEP):
            self.over_the_board = 1
            for column in COLUMNS:
                if column < x < column + STEP:
                    self.head_column = COLUMNS.index(column)
        else:
            self.over_the_board = 0


    def draw(self):
        self.screen.fill(color=NICE_BLUE)
        self.screen.blit(self.below_board, dest=BOARD)
        if self.over_the_board == 1:
            if self.move == 1:
                self.screen.blit(self.red_pull, dest=(BOARD[0] + self.col * STEP, BOARD[1] - STEP))
            else:
                self.screen.blit(self.red_pull, dest=(BOARD[0] + self.head_column * STEP, BOARD[1] - STEP))
        self.screen.blit(self.board, dest=BOARD)
        
s = Starter()
s.mainLoop(FPS)
