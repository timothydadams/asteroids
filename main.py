import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS,ASTEROID_SPAWN_RATE

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
            screen.fill("black")
            pygame.display.flip()
    except KeyboardInterrupt:
        print("Exited loop form keyboard interrupt")
    finally:
        print("Program ended")
    

if __name__ == "__main__":
    main()