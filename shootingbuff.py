import pygame
import random

from circleshape import CircleShape
from constants import BUFFER_RADIUS
from constants import LINE_WIDTH
from constants import BUFFER_SPAWN_RATE_SECONDS
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


class ShootingBuffer(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, BUFFER_RADIUS)
        self.rotation = 0
        self.spawn_timer = 0

    def star(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward / 2 * self.radius - right
        c = self.position - forward / 2 * self.radius + right
        d = self.position + forward * -self.radius 
        e = self.position - forward / 2 * -self.radius + right
        f = self.position - forward / 2 * -self.radius - right
        g = self.position + right * 1.5
        h = self.position - right * 1.5
        i = self.position
        j = self.position + forward * self.radius
        k = self.position - forward * self.radius
        return [j, i, a, i, h, i, f, i, k, i, b, i, d, i, g, i, c, i, e, i]
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.star(), LINE_WIDTH)

    def spawn(
        self, position: pygame.Vector2, radius: float) -> None:
        buff = ShootingBuffer(position, radius)

    def update(self, dt: float) -> None:
        self.spawn_timer += dt
        if self.spawn_timer > BUFFER_SPAWN_RATE_SECONDS:
            self.spawn_timer = 0

            position = (random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT))
            self.spawn(position, BUFFER_RADIUS)