import pygame
import ScreenManager

pygame.init()

screen_width = 16*32                                                    # Screen width
screen_height = 21*32                                                   # Screen Height

screen = pygame.display.set_mode((screen_width, screen_height))         # Screen defined
pygame.display.set_caption('Tetris')                                    # Screen name

walktime = 125                                                          # 125ms for each half tile walked
clock = pygame.time.Clock()                                             # Internal timer
move_event = pygame.USEREVENT + 1                                       # Move event defined
pygame.time.set_timer(move_event, walktime)                             # New event called each 125ms

ScreenManager.initialize(screen)                                        # Initial screen
pygame.display.flip()
orient = 0                                                              # Movement orientation aux
ori = 0                                                                 # Orientation aux
restart = False

running = True                                                          # Flux variable
while running:
    for e in pygame.event.get():
        if e.type == move_event:
            ScreenManager.update()
            ScreenManager.setonscreen(screen)
            pygame.display.flip()
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        running = False
