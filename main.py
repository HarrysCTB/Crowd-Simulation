from app.config import settings
from app.models.welcom_screen import WelcomeScreen


def main():
    screen = settings.open_window()
    settings.initialize_screen_manager()
    welcome_screen = WelcomeScreen()
    welcome_screen.initialize()
    settings.game_loop(screen, welcome_screen)


if __name__ == "__main__":
    main()
