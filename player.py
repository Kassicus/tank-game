import pygame
import color

class Player():
    def __init__(self):
        self.x = 100
        self.y = 100

        self.move_x = 0
        self.move_y = 0

        self.speed = 8

    def draw(self, surface):
        pygame.draw.rect(surface, color.WHITE, (self.x, self.y, 30, 30))

    def update(self, events):
        self.x += self.move_x
        self.y += self.move_y

        self.movement_handler(events)

    def movement_handler(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.move_x = self.speed
                if event.key == pygame.K_a:
                    self.move_x = -self.speed

                if event.key == pygame.K_w:
                    self.move_y = -self.speed
                if event.key == pygame.K_s:
                    self.move_y = self.speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_a:
                    self.move_x = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    self.move_y = 0