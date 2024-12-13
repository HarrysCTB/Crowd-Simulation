import pygame
from ..modules.crowd_simulation import CrowdSimulation


class GameScreen:
    def __init__(self, screen_manager, screen):
        self.layout = []
        self.screen_manager = screen_manager
        self.screen = screen
        self.crowd_simulation = None
        self.crowd_launch()

    def crowd_launch(self):
        self.crowd_simulation = CrowdSimulation(2, self.screen_manager.get_current_crowd(), self.screen)
        self.crowd_simulation.create_agents()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.restart()

            for element in self.layout:
                element.handle_event(event)

    def initialize(self, screen):
        self.layout = []

    def restart(self):
        self.crowd_simulation = None
        self.crowd_launch()

    def update(self):
        """Met à jour la simulation de foule."""
        if self.crowd_simulation:
            self.crowd_simulation.update()

    def draw(self, screen):
        """Dessine l'écran de jeu."""
        screen.fill((255, 255, 255))

        if self.crowd_simulation:
            self.crowd_simulation.draw(screen)

        for element in self.layout:
            element.draw(screen)