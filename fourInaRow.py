from pygame import *
from pygamehelper import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform
import os

FPS = 40
STEP = 60
BOARD_CAPACITY = 63

WHITE = (255,255,255)
YELLOW = (235,235,0)
RED = (214,71,0)
BLUE = (0,102,153)
DARK_BLUE = (0,49,101)
LIGHT_BLUE = (185,231,255)
NICE_BLUE = (202,202,255)

BOARD = (190, 240)
COLUMNS = [190, 250, 310, 370, 430, 490, 550]
ROWS = [240, 300, 360, 420, 480, 540]

class Starter(PygameHelper):
    def __init__(self):
        self.w, self.h = 800, 600
        self.col = -1
        self.row = -1

        self.move = 0
        self.done = 0
        self.header = 0
        
        self.head_column = -1
        self.turn = 0
        self.free_space = 0
        self.moving_Y = 0

        self.winner = 0
        self.game_status = 1
        
        self.pulls = [[0 for y in range(len(COLUMNS))] for x in range(len(ROWS))]
        self.Surface = pygame.display.set_mode((self.w, self.h))

        PygameHelper.__init__(self, size=(self.w, self.h), fill=(LIGHT_BLUE))
        self.background = pygame.image.load(os.path.join("pics", "background.png"))
        self.below_board = pygame.image.load(os.path.join("pics", "below_board.png"))
        self.board = pygame.image.load(os.path.join("pics", "board.png"))
        self.red_pull = pygame.image.load(os.path.join("pics", "red_pull.png"))
        self.yellow_pull = pygame.image.load(os.path.join("pics", "yellow_pull.png"))
        self.empty = pygame.image.load(os.path.join("pics", "empty.png"))

        self.player_header = [self.red_pull, self.yellow_pull]
        self.player_falling = [self.yellow_pull, self.red_pull]
        self.player = [self.empty, self.red_pull, self.yellow_pull]

    def check_win(self):
        '''
        for c in range(len(ROWS)):
            self.result_red = 0
            self.result_yellow = 0
            for x in range(2,9):
                y = x - 2 + c
                if self.pulls[x][y] == 1:
                    self.result_red += 1
                elif self.pulls[x][y] == 2:
                    self.result_yellow += 1
        '''
        for each_row in self.pulls:
            if self.winner == 0:
                for i, pull in enumerate(each_row[:4]):
                    if pull > 0:
                        if pull == each_row[i + 1] == each_row[i + 2] == each_row[i + 3]:
                            self.winner = pull
                            break

        for row in range(3):
            if self.winner == 0:
                for col in range(7):
                    if self.pulls[row][col] > 0:
                        if self.pulls[row][col] == self.pulls[row + 1][col] == self.pulls[row + 2][col] == self.pulls[row + 3][col]:
                            self.winner = self.pulls[row][col]
                            break

        for c in range(6):
            if self.winner == 0:
                for x in range(3):
                    if self.winner == 0:
                        for y in range(4):
                            if y == x + 2 - c:
                                if self.pulls[x][y] and (self.pulls[x][y] == self.pulls[x + 1][y + 1] == self.pulls[x + 2][y + 2] == self.pulls[x + 3][y + 3]):
                                    self.winner = self.pulls[x][y]
                                    break

        for c in range(6):
            if self.winner == 0:
                for x in range(3,6):
                    if self.winner == 0:
                        for y in range(4):
                            if y == 8 - x - c:
                                if self.pulls[x][y] and (self.pulls[x][y] == self.pulls[x - 1][y + 1] == self.pulls[x - 2][y + 2] == self.pulls[x - 3][y + 3]):
                                    self.winner = self.pulls[x][y]
                                    break

        print("winner: ", self.winner)
        print("_____________________")

    def update(self):
        while self.moving_Y < ROWS[self.row]:
            self.moving_Y += 1

    def keyUp(self, key):
        pass
        
    def mouseUp(self, button, pos):
        x, y = pos[0], pos[1]

        if button == 1 and self.game_status == 1:
            self.moving_Y = BOARD[1] - STEP
            self.move = 0
            self.free_space = 0
            for column in COLUMNS:
                if column < x < column + STEP:
                    self.col = COLUMNS.index(column)
                    print("col index:", self.col)
                    self.move = 1
                    break
            if self.move == 1:
                for each_row in self.pulls:
                    if each_row[self.col] == 0:
                        self.free_space += 1
                print("free space: ", self.free_space)
                if self.free_space > 0:
                    self.row = self.free_space - 1
                    print("row index:", self.row)
                    self.pulls[self.row][self.col] = 1 + self.turn
                    print("Board:")
                    print(self.pulls)
                    print("_____________________")
                    self.turn = not(self.turn)
                    self.done = 1
                self.check_win()
                if self.winner:
                    self.game_status = 2

    def mouseMotion(self, buttons, pos, rel):
        x, y = pos[0], pos[1]
        
        if self.game_status == 1 and x in range(BOARD[0],BOARD[0] + len(COLUMNS) * STEP):
            self.header = 1
            for column in COLUMNS:
                if column < x < column + STEP:
                    self.head_column = COLUMNS.index(column)
        else:
            self.header = 0


    def draw(self):
        self.screen.fill(NICE_BLUE)
        self.screen.blit(self.below_board, BOARD)

        if self.game_status == 1:
            if self.header == 1 and sum([sum(pull) for pull in self.pulls]) < BOARD_CAPACITY:
                self.screen.blit(self.player_header[self.turn], (BOARD[0] + self.head_column * STEP, BOARD[1] - STEP))

            if self.move == 1:
                self.screen.blit(self.player_falling[self.turn], (BOARD[0] + self.col * STEP, self.moving_Y))

        for col in range(len(COLUMNS)):
            for row in range(len(ROWS)):
                if self.pulls[row][col] > 0:
                    self.screen.blit(self.player[self.pulls[row][col]], (COLUMNS[col], ROWS[row]))

        if self.game_status == 2:
            pass

        self.screen.blit(self.board, BOARD)
        
s = Starter()
s.mainLoop(FPS)
