import pygame
from .button import Button


class SelectScreen:
    def __init__(self, srceen_manager, screen):
        self.layout = []
        self.screen_manager = srceen_manager
        self.screen = screen

    def start_game(self, crowd_type):
        print(crowd_type)
        self.screen_manager.set_crowd(crowd_type)
        self.screen_manager.switch_to('select_map', self.screen)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            for element in self.layout:
                element.handle_event(event)

    def side_menu(self):
        rect = pygame.Rect(0, 0, 250, 720)
        pygame.draw.rect(self.screen, (0, 0, 0), rect)

    def initialize(self, screen):
        self.layout = []
        self.layout.append(
            Button('Birds', (0, 400, 250, 50),
                   (255, 255, 255),
                   lambda: self.start_game('birds')))

    def draw(self, screen):
        screen.fill((255, 255, 255))
        self.side_menu()
        for element in self.layout:
            element.draw(screen)