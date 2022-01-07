import pygame


def getdir():
    direct = [pygame.key.get_pressed()[i] for i in (pygame.K_d, pygame.K_s, pygame.K_a)]
    r = 0
    if (x := direct.count(True)) == 1:
        return direct.index(True) + 1
    elif x == 2 and direct[1]:
        return
    return 0
