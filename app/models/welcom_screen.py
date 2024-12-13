import pygame
from .button import Button
from .screen_manager import ScreenManager


class WelcomeScreen:
    def __init__(self, screen_manager, screen):
        self.layout = []
        self.screen_manager = screen_manager
        self.screen = screen

    def start_game(self):
        self.screen_manager.switch_to('select_crowd', self.screen)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            for element in self.layout:
                element.handle_event(event)

    def initialize(self, screen):
        self.layout = []
        self.layout.append(
            Button('Start', (((screen.get_width() / 2) - 100), ((screen.get_height() / 2) - 25), 200, 50), (255, 255, 255),
                   self.start_game))

    def draw(self, screen):
        screen.fill((255, 255, 255))
        for element in self.layout:
            element.draw(screen)
