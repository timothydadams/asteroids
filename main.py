import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS,ASTEROID_SPAWN_RATE
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidField import AsteroidField

def main():
    pygame.init()
    collision = pygame.event.custom_type()
    clock = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], display=2)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == collision:
                    print(event.data)
                    return
            
            updatable.update(dt)
            screen.fill("black")
            
            for asteroid in asteroids:
                if asteroid.is_colliding(player):
                    event = pygame.event.Event(collision, data="Game Over! You hit an asteroid...")
                    pygame.event.post(event)

                for shot in shots:
                    if shot.is_colliding(asteroid):
                        shot.kill()
                        asteroid.split()

            for item in drawable:
                item.draw(screen)
            
            pygame.display.flip()

            # 60 FPS limitation
            dt = clock.tick(60) / 1000      
    except KeyboardInterrupt:
        print("Exited loop form keyboard interrupt")
    finally:
        print("Program ended")
    

if __name__ == "__main__":
    main()