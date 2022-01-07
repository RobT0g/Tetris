import pygame.key
from random import randint


grid = [[0 for v in range(0, 20)] for i in range(0, 15)]
lastp = 0  # Last piece
acp = 0  # Current falling piece
lpp = []  # Current falling piece last pos
cpp = []  # Current falling piece pos
lp = []
cp = []
tmm = 0  # Time multiplier for going down

def initialize():  # Initialize certain variables
    setnextp()


def update():  # Update pieces positions
    global grid, lpp, cpp, tmm
    instup = [0, 0]
    tmm = (tmm + 1) % 4
    if pygame.key.get_pressed()[pygame.K_a]:
        instup[0] -= 1
    if pygame.key.get_pressed()[pygame.K_d]:
        instup[0] += 1
    if pygame.key.get_pressed()[pygame.K_s] or tmm == 3:
        instup[1] += 1
    lpp = cpp[:]
    cpp[0] += instup[0]
    cpp[1] += instup[1]
    setpongrid()


def setpongrid():
    global grid, acp, lpp, cpp, lp, cp
    lp = []
    cp = []
    if acp == 1:  # Square 2x2
        lp = [[lpp[0] + i, lpp[1] + v] for v in range(0, 2) for i in range(0, 2)]
        cp = [[cpp[0] + i, cpp[1] + v] for v in range(0, 2) for i in range(0, 2)]
    elif acp == 2:  # Line 1x4
        lp = [[lpp[0], lpp[1] + v] for v in range(0, 4)]
        cp = [[cpp[0], cpp[1] + v] for v in range(0, 4)]
    elif acp == 3:  # S 3x2
        lp = [[lpp[0] + v, lpp[1] + 1] for v in range(0, 2)] + [[lpp[0] + v, lpp[1]] for v in range(1, 3)]
        cp = [[cpp[0] + v, cpp[1] + 1] for v in range(0, 2)] + [[cpp[0] + v, cpp[1]] for v in range(1, 3)]
    elif acp == 4:  # Z 3x2
        lp = [[lpp[0] + v, lpp[1]] for v in range(0, 2)] + [[lpp[0] + v, lpp[1] + 1] for v in range(1, 3)]
        cp = [[cpp[0] + v, cpp[1]] for v in range(0, 2)] + [[cpp[0] + v, cpp[1] + 1] for v in range(1, 3)]
    elif acp == 5:  # L 2x3
        lp = [[lpp[0], lpp[1] + v] for v in range(0, 3)] + [lpp[0] + 1, lpp[1] + 2]
        cp = [[cpp[0], cpp[1] + v] for v in range(0, 3)] + [cpp[0] + 1, cpp[1] + 2]
    elif acp == 6:  # J 2x3
        lp = [[lpp[0], lpp[1] + v] for v in range(0, 3)] + [lpp[0] - 1, lpp[1] + 2]
        cp = [[cpp[0], cpp[1] + v] for v in range(0, 3)] + [cpp[0] - 1, cpp[1] + 2]
    else:  # T 3x2
        lp = [[lpp[0] + v, lpp[1]] for v in range(0, 3)] + [lpp[0] + 1, lpp[1] + 1]
        cp = [[cpp[0] + v, cpp[1]] for v in range(0, 3)] + [cpp[0] + 1, cpp[1] + 1]


def getgrid():  # Return the current grid
    global grid
    return grid


def setnextp():  # Next piece to fall
    global lastp, acp, lpp, cpp
    aux = randint(1, 7)
    if aux == lastp:
        aux = ((aux + 1) % 7) + 1
    lastp = acp
    acp = aux
    acp = 1
    lpp = []
    if acp == 1:  # Square 2x2
        cpp = [7, -2]
    elif acp == 2:  # Line 1x4
        cpp = [7, -4]
    elif acp == 3:  # S 3x2
        cpp = [7, -2]
    elif acp == 4:  # Z 3x2
        cpp = [7, -2]
    elif acp == 5:  # L 2x3
        cpp = [7, -3]
    elif acp == 6:  # J 2x3
        cpp = [7, -3]
    else:  # T 3x2
        cpp = [6, -2]

