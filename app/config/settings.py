import pygame
from ..models.welcom_screen import WelcomeScreen
from ..models.screen_manager import ScreenManager


def open_window():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Crowd Simulation')
    return screen


def initialize_screen_manager(screen):
    screen_manager = ScreenManager()
    screen_manager.add_screen('welcome', WelcomeScreen(screen_manager, screen))
    screen_manager.switch_to('welcome', screen)
    return screen_manager


def game_loop(screen, screen_manager):
    while True:
        events = pygame.event.get()
        current_screen = screen_manager.get_current_screen()

        # Gestion des événements
        current_screen.handle_events(events)

        # Mise à jour conditionnelle
        if hasattr(current_screen, 'update') and callable(getattr(current_screen, 'update')):
            current_screen.update()

        # Dessin de l'écran
        current_screen.draw(screen)
        pygame.display.flip()
