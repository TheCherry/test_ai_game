A = 0 ## AIR                    - Movable field, no actions
P = 1 ## PLAYER                 - The Player
W = 2 ## WALL                   - A Wall, player cant pass
F = 3 ## FIRE                   - Kills the player if he havent a Fire protection
P = 4 ## FPROTECT               - Fire protection
R = 5 ## ALLOW_DIRECTION_RIGHT  - only moveable to right
L = 6 ## ALLOW_DIRECTION_LEFT   - only moveable to left
D = 7 ## ALLOW_DIRECTION_DOWN   - only moveable to down
U = 8 ## ALLOW_DIRECTION_UP     - only moveable to up
K = 9 ## KEY                    - key, needed for doors
D = 10 ## DOOR                  - door, only passable with a key
G = 11 ## GOAL                  - the end

levels = [
    ###
    [{ "best_steps": 2, "matrix": [
       # 0  1  2  3  4  5  6  7  8  9 10 11
        [W, W, W, W, W, W, W, W, W, W, W, W], # 0
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 1
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 2
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 3
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 4
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 5
        [W, 0, 0, 0, 0, P, 0, G, 0, 0, 0, W], # 6
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 7
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 8
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 9
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 10
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 11
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 12
        [W, W, W, W, W, W, W, W, W, W, W, W]  # 13
    ]},{ "best_steps": 8, "matrix": [
       # 0  1  2  3  4  5  6  7  8  9 10 11
        [W, W, W, W, W, W, W, W, W, W, W, W], # 0
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 1
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 2
        [W, 0, 0, 0, 0, 0, W, W, W, 0, 0, W], # 3
        [W, 0, 0, 0, 0, W, G, 0, W, 0, 0, W], # 4
        [W, 0, 0, 0, W, P, W, 0, W, 0, 0, W], # 5
        [W, 0, 0, 0, W, 0, W, D, W, 0, 0, W], # 6
        [W, 0, 0, 0, W, 0, 0, K, W, 0, 0, W], # 7
        [W, 0, 0, 0, W, W, W, W, 0, 0, 0, W], # 8
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 9
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 10
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 11
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 12
        [W, W, W, W, W, W, W, W, W, W, W, W]  # 13
    ]},{ "best_steps": 12, "matrix": [
       # 0  1  2  3  4  5  6  7  8  9 10 11
        [W, W, W, W, W, W, W, W, W, W, W, W], # 0
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 1
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 2
        [W, 0, 0, 0, W, W, W, W, W, 0, 0, W], # 3
        [W, 0, 0, 0, W, P, W, G, W, 0, 0, W], # 4
        [W, 0, 0, 0, W, 0, W, 0, W, 0, 0, W], # 5
        [W, 0, 0, 0, W, 0, W, 0, W, 0, 0, W], # 6
        [W, 0, 0, 0, W, 0, D, 0, W, 0, 0, W], # 7
        [W, 0, 0, 0, W, 0, W, W, 0, 0, 0, W], # 8
        [W, 0, 0, 0, W, K, W, 0, 0, 0, 0, W], # 9
        [W, 0, 0, 0, 0, W, 0, 0, 0, 0, 0, W], # 10
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 11
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 12
        [W, W, W, W, W, W, W, W, W, W, W, W]  # 13
    ]},{ "best_steps": 10, "matrix": [
       # 0  1  2  3  4  5  6  7  8  9 10 11
        [W, W, W, W, W, W, W, W, W, W, W, W], # 0
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 1
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 2
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 3
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 4
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 5
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 6
        [W, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, W], # 7
        [W, 0, 0, G, 0, 0, 0, 0, 0, 0, 0, W], # 8
        [W, W, W, D, W, 0, 0, 0, 0, 0, 0, W], # 9
        [W, 0, 0, 0, W, 0, 0, 0, 0, 0, 0, W], # 10
        [W, 0, W, 0, W, 0, 0, 0, 0, 0, 0, W], # 11
        [W, P, W, K, W, 0, 0, 0, 0, 0, 0, W], # 12
        [W, W, W, W, W, W, W, W, W, W, W, W]  # 13
    ]}
]
