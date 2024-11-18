import pygame
from ..models.welcom_screen import WelcomeScreen
from ..models.screen_manager import ScreenManager


def open_window():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Crowd Simulation')
    return screen


def initialize_screen_manager():
    screen_manager = ScreenManager()
    screen_manager.add_screen('welcome', WelcomeScreen())
    screen_manager.switch_to('welcome')
    return screen_manager


def game_loop(screen, current_screen):
    while True:
        events = pygame.event.get()
        current_screen.handle_events(events)
        current_screen.draw(screen)
        pygame.display.flip()
