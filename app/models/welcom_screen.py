import pygame


class WelcomeScreen:
    def __init__(self):
        self.layout = []

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            for element in self.layout:
                element.handle_event(event)

    def initialize(self):
        self.layout = []

    def draw(self, screen):
        screen.fill((0, 0, 0))
        for element in self.layout:
            element.draw(screen)
        screen.fill((200, 200, 200))
