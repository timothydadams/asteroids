from pygame import event as e, display, Surface, QUIT
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS,ASTEROID_SPAWN_RATE

def main():
    # pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    try:
        while True:
            for event in e.get():
                if event.type == QUIT:
                    return
                
            Surface.fill(screen, (0,0,0))
            display.flip()
    except KeyboardInterrupt:
        print("Exited loop form keyboard interrupt")
    finally:
        print("Program ended")
    

if __name__ == "__main__":
    main()