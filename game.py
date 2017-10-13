import numpy as np
from enum import Enum

class Direction():
    RIGHT   = [0, 1]
    LEFT    = [0, -1]
    DOWN    = [1, 0]
    UP      = [-1, 0]

class GObj(Enum):
    AIR                      = 0 ## Movable field, no actions
    PLAYER                   = 1 ## The Player
    WALL                     = 2 ## A Wall, player cant pass
    FIRE                     = 3 ## Kills the player if he havent a Fire protection
    FPROTECT                 = 4 ## Fire protection
    ALLOW_DIRECTION_RIGHT    = 5 ## only moveable to right
    ALLOW_DIRECTION_LEFT     = 6 ## only moveable to left
    ALLOW_DIRECTION_DOWN     = 7 ## only moveable to down
    ALLOW_DIRECTION_UP       = 8 ## only moveable to up
    KEY                      = 9 ## key, needed for doors
    DOOR                     = 10 ## door, only passable with a key
    GOAL                     = 11 ## the end

    def one_hot(self):
        ret = np.zeros(len(GObj), dtype=np.int)
        ret[self.value] = 1
        return ret

    def nn_value(self):
        return self.value/100

## test one_hot
for gobj in GObj:
    print(gobj.one_hot())


example_level = np.array([
   # 0  1  2  3  4  5  6  7  8  9 10 11
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], # 0
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], # 1
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], # 2
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], # 3
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], # 4
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], # 5
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], # 6
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], # 7
    [2, 0, 0,11, 0, 0, 0, 0, 0, 0, 0, 2], # 8
    [2, 2, 2,10, 2, 0, 0, 0, 0, 0, 0, 2], # 9
    [2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2], # 10
    [2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2], # 11
    [2, 1, 2, 9, 2, 0, 0, 0, 0, 0, 0, 2], # 12
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]  # 13
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
            self.matrix[tuple(self.player_pos)] = GObj.AIR.nn_value
            self.matrix[tuple(new_pos)] = GObj.PLAYER.nn_value
        print(self.matrix)

    def logic_move(self, pos):
        ## set gamestats by specific fields
        ## returns True if the player was able to move
        gobj = GObj(self.matrix.item(tuple(pos)))
        if(gobj is GObj.AIR):
            return True
        elif(gobj is GObj.FPROTECT):
            self.anti_fire += 1
            return True
        elif(gobj is GObj.FIRE):
            if(self.anti_fire > 0):
                self.anti_fire -= 1
                return True
            else:
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
