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
        self.player_pos = tuple(np.resize(np.where(self.matrix == GObj.PLAYER.value), new_shape=2))
        self.steps = 0 ## for rewards
        self.keys = 0
        self.anti_fire = 0
        self.finish = False
        self.gameover = False

    def move(self, direction):
        new_pos = tuple(np.add(self.player_pos, direction))
        self.steps += 1
        if(self.logic_move(new_pos, direction)):
            self.matrix[self.player_pos] = GObj.AIR.value ## remove player
            self.matrix[new_pos] = GObj.PLAYER.value ## set player to new location
            self.player_pos = new_pos
            return True
        return False


    def logic_move(self, pos, direction):
        ## set gamestats by specific fields
        ## returns True if the player was able to move
        gobj = GObj(self.matrix.item(pos))
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
        elif(gobj is GObj.ALLOW_DIRECTION_DOWN and direction is Direction.DOWN):
            return True
        elif(gobj is GObj.ALLOW_DIRECTION_UP and direction is Direction.UP):
            return True
        elif(gobj is GObj.ALLOW_DIRECTION_RIGHT and direction is Direction.RIGHT):
            return True
        elif(gobj is GObj.ALLOW_DIRECTION_LEFT and direction is Direction.LEFT):
            return True
        return False



gf = GameField(example_level)
### HARD TEST:
print("{:<10} - {}".format("DOWN", gf.move(Direction.DOWN)))
print("{:<10} - {}".format("UP", gf.move(Direction.UP)))
print("{:<10} - {}".format("UP", gf.move(Direction.UP)))
print("{:<10} - {}".format("RIGHT", gf.move(Direction.RIGHT)))
print("{:<10} - {}".format("RIGHT", gf.move(Direction.RIGHT)))
print("{:<10} - {}".format("UP", gf.move(Direction.UP)))
print("{:<10} - {}".format("DOWN", gf.move(Direction.DOWN)))
print("{:<10} - {}".format("DOWN", gf.move(Direction.DOWN)))
print("{:<10} - {}".format("UP", gf.move(Direction.UP)))
print("{:<10} - {}".format("UP", gf.move(Direction.UP)))
print("{:<10} - {}".format("UP", gf.move(Direction.UP)))
print("{:<10} - {}".format("UP", gf.move(Direction.UP)))
print(gf.finish)

##
