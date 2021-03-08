import pygame, sys
from random import randint, randrange
from pygame.locals import *
from math import sqrt, dist

SIZE = WIDTH, HEIGHT = 500, 600
FPS = 60


class Alien:
    def __init__(self, v=0):
        self.x = randint(12, 487)
        self.y = -12
        self.color = Color((randint(128, 255), randint(0, 255), 0))
        self.v = v = v or randint(100, 199)
        self.vy = vy = randrange(20, self.v)
        self.vx = sqrt(v ** 2 - vy ** 2)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 12)

    def move(self):
        self.x += self.vx / FPS
        self.y += self.vy / FPS
        if int(self.x) not in range(WIDTH):
            self.vx *= -1
        if self.y > HEIGHT:
            self.y = -12

    def collision(self, starship):
        return Rect(self.x - 6, self.y - 6, 24, 24).colliderect(Rect(starship.x, starship.y, 41, 41))

    def hit(self, torpedo):
        return Rect(self.x - 6, self.y - 6, 24, 24).colliderect(Rect(torpedo.x - 1, torpedo.y - 5, 3, 11))


class Starship:
    def __init__(self):
        self.x = WIDTH / 2 - 20
        self.y = HEIGHT - 30 - 20

    def draw(self, screen):
        pygame.draw.rect(screen, Color('white'), (self.x, self.y, 41, 41))

    def move(self, dx):
        self.x = max(0, min(WIDTH - 41, self.x + dx))


class Torpedo:
    def __init__(self, starship):
        self.x = starship.x + 20
        self.y = starship.y

    def draw(self, screen):
        pygame.draw.rect(screen, Color('cyan'), (self.x - 1, self.y - 5, 3, 11))

    def move(self):
        self.y -= 400 / FPS


def final_message(msg):
    pygame.display.set_caption(msg)
    while True:
        for evt in pygame.event.get():
            if evt.type == QUIT:
                return
            elif evt.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed(3)[0]:
                return


pygame.init()
screen = pygame.display.set_mode(SIZE)
pressed = {K_LEFT: False, K_RIGHT: False}
starship = Starship()
aliens = [Alien() for _ in range(10)]
torpedos = []
clock = pygame.time.Clock()
damage = score = 0

done = False

while not done:
    screen.fill('black')
    for evt in pygame.event.get():
        if evt.type == QUIT:
            done = True
        elif evt.type in (KEYDOWN, KEYUP) and evt.key in (K_LEFT, K_RIGHT):
            pressed[evt.key] = evt.type == KEYDOWN
        elif evt.type == KEYDOWN and evt.key == K_SPACE:
            torpedos.append(Torpedo(starship))

    if pressed[K_LEFT]:
        starship.move(-200 / FPS)
    if pressed[K_RIGHT]:
        starship.move(200 / FPS)

    starship.draw(screen)

    for i in range(len(aliens) - 1, -1, -1):
        alien = aliens[i]
        alien.move()
        alien.draw(screen)
        for j in range(len(torpedos) - 1, -1, -1):
            if alien.hit(torpedos[j]):
                del torpedos[j]
                del aliens[i]
                aliens.append(Alien(int(alien.v * 1.1)))
                score += 1
                break
        if alien.collision(starship):
            del aliens[i]
            damage += 1

    for i in range(len(torpedos) - 1, -1, -1):
        t = torpedos[i]
        t.move()
        if t.y < 0:
            del torpedos[i]
        t.draw(screen)
    pygame.display.set_caption(f'Damage: {damage} - Score: {score}')

    if damage >= 3:
        final_message(f'GAME OVER - Score: {score}')
        done = True
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
