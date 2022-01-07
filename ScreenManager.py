import pygame
import GridManager

pygame.init()
pygame.font.init()

# Images
board = pygame.image.load('Images/Frame.png')
tilepack = [pygame.image.load(f'Images/PFrame{i}.png') for i in range(1, 8)]
tick = 0

# Objects
grid = GridManager.GridStruc()
piece = GridManager.FallingPiece(grid.curtype())


def initialize(screen):         # Initial screen
    global grid, piece
    screen.blit(board, (0, 0))


def update():                   # Updates stuff
    global tick, piece, grid
    tick = (tick + 1) % 4
    if pygame.key.get_pressed()[pygame.K_a]:
        if piece.coord[0] > 0:
            piece.movehor(-1, grid.grid)
    if pygame.key.get_pressed()[pygame.K_d]:
        if piece.coordd[0] < 14:
            piece.movehor(1, grid.grid)
    if pygame.key.get_pressed()[pygame.K_r]:
        piece.rotate()
    if tick == 3 or pygame.key.get_pressed()[pygame.K_s]:
        if piece.godown(grid.grid):
            grid.setelement(piece.box, piece.type)
            piece.__init__(grid.curtype())


def setonscreen(screen):        # Puts stuff on the screen
    global piece, grid
    screen.blit(board, (0, 0))
    for k1, v1 in enumerate(grid.grid):
        for k2, v2 in enumerate(v1):
            if v2 != 0:
                screen.blit(tilepack[v2-1], acualpos([k1, k2]))
    for v in piece.box:
        screen.blit(tilepack[piece.type-1], acualpos(v))


def acualpos(pos):              # Transforms on-grid pos to on-screen pos
    if pos[0] < 0 or pos[1] < 0:
        return [-32, -32]
    return [(pos[0]*32)+16, (pos[1]*32)+16]
