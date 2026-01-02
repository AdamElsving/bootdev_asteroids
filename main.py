import pygame as pg
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pg.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pg.time.Clock()
    dt = 0

    while True:
        log_state()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        for i in range (1, 1000000):
            k = 5 / i

        screen.fill("black")
        pg.display.flip()

        dt = clock.tick(60) / 1000 

if __name__ == "__main__":
    main()
