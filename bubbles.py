import pygame
import sys
from pygame.locals import *
from random import randint, random
from math import sqrt

SIZE = 400, 400
FPS = 25

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Bubbles")
clock = pygame.time.Clock()


class Particle:
    def __init__(self, x, y, radius, color, xspeed, yspeed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.thickness = thickness = 1
        self.elasticity = elasticity = 0.95

    def draw(self, screen):
        pos = int(self.x), int(self.y)
        pygame.draw.circle(screen, self.color, pos, self.radius)
        pygame.draw.circle(screen, Color('black'), pos, self.radius, self.thickness)

    def move(self):
        if not self.radius < self.xspeed + self.x < SIZE[0] - self.radius:
            self.xspeed = -self.xspeed * self.elasticity
        if not self.radius < self.yspeed + self.y < SIZE[1] - self.radius:
            self.yspeed = -self.yspeed * self.elasticity
        self.x += self.xspeed
        self.y += self.yspeed

    def calculatedistanceto(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def collide(self, other):
        if self.calculatedistanceto(other) < self.radius + other.radius:
            self.xspeed, other.xspeed = other.xspeed * self.elasticity, self.xspeed * self.elasticity
            self.yspeed, other.yspeed, = other.yspeed * self.elasticity, self.yspeed * self.elasticity
        while self.calculatedistanceto(other) < self.radius + other.radius:
            self.move()
            other.move()


def reset(number=10):
    li = []
    for i in range(number):
        radius = randint(5, 20)
        li.append(Particle(
            x=randint(radius, SIZE[0] - radius),
            y=randint(radius, SIZE[1] - radius),
            radius=radius,
            xspeed=10 * random() - 5,
            yspeed=10 * random() - 5,
            color=tuple(randint(0, 255) for _ in range(3))
        ))
    return li


my_particles = reset()
done = False
pressed_g = False
while not done:
    for evt in pygame.event.get():
        if evt.type == QUIT:
            done = True
        elif evt.type == KEYDOWN:
            if evt.key == K_n:
                my_particles = reset()
            elif evt.key == K_a:
                for p in my_particles:
                    p.xspeed *= 1.10
                    p.yspeed *= 1.10
            elif evt.key == K_g:
                pressed_g = True
        elif evt.type == KEYUP:
            if evt.key == K_g:
                pressed_g = False

    screen.fill(Color('gray'))

    for p1 in my_particles:
        p1.move()
        p1.draw(screen)
        if pressed_g:
            p1.yspeed += 0.5
        for p2 in my_particles:
            if p1 == p2:
                continue
            p1.collide(p2)

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
sys.exit()
