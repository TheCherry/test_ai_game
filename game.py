import numpy as np
from enum import Enum

class Direction():
    RIGHT   = [0, 1]
    LEFT    = [0, -1]
    DOWN    = [1, 0]
    UP      = [-1, 0]

class GObj(Enum):
    AIR     = 0
    PLAYER  = 1
    WALL    = 2
    FIRE    = 3
    KEY     = 4
    DOOR    = 5
    GOAL    = 6

example_level = np.array([
   # 0  1  2  3  4  5  6  7  8  9 10 11
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 0
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 1
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0], # 2
    [0, 0, 0, 0, 0, 0, 0, 1, 5, 9, 0, 0], # 3
    [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0], # 4
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 5
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 6
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 7
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 8
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 9
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 10
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 11
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 12
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 13
])

class GameField:
    def __init__(self, level_matrix):
        self.matrix = level_matrix
        self.player_pos = np.resize(np.where(self.matrix == GObj.PLAYER.value), new_shape=2)
        self.steps = 0
        self.keys = 0
        self.gameover = False

    def move(self, direction):
        new_pos = np.add(self.player_pos, direction)
        self.steps += 1
        if(self.logic_move(new_pos)):
            self.matrix[tuple(self.player_pos)] = GObj.AIR.value
            self.matrix[tuple(new_pos)] = GObj.PLAYER.value
        print(self.matrix)

    def logic_move(self, pos):
        ## set gamestats by specific fields
        ## returns True if the player was able to move
        gobj = GObj(self.matrix.item(tuple(pos)))
        if(gobj is GObj.AIR):
            return True
        if(gobj is GObj.FIRE):
            self.gameover = True
            return True
        elif(gobj is GObj.WALL):
            return False
        elif(gobj is GObj.KEY):
            self.keys += 1
            return True
        elif(gobj is GObj.GOAL):
            self.finish = True
            return True
        elif(gobj is GObj.DOOR):
            if(self.keys > 0):
                self.keys -= 1
                return True
            else:
                return False



gf = GameField(example_level)
gf.move(Direction.DOWN)



##
