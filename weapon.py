import pygame

class Turret():
    def __init__(self, x, y, ammo_type):
        self.x = x
        self.y = y

        self.cooldown = 100

        self.ammo_type = ammo_type

    def draw(self, surface):
        pass

    def update(self, events):
        self.event_handler(events)

    def event_handler(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.shoot(self.ammo_type, mouse_pos[0], mouse_pos[1])