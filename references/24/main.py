import sys, pygame


def main():
    pygame.init()

    size = width, height = 1200, 900

    backgroundColor = 252,90,90

    screen = pygame.display.set_mode(size)
    screen.fill(backgroundColor)
    pygame.display.flip()

main()
