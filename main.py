from app.config import settings
from app.models.welcom_screen import WelcomeScreen
from app.models.select_screen import SelectScreen
from app.models.select_map import SelectMap


def main():
    screen = settings.open_window()
    screen_manager = settings.initialize_screen_manager(screen)
    welcome_screen = WelcomeScreen(screen_manager, screen)
    select_screen = SelectScreen(screen_manager, screen)
    select_map = SelectMap(screen_manager, screen)
    screen_manager.add_screen('select_crowd', select_screen)
    screen_manager.add_screen('select_map', select_map)
    screen_manager.add_screen('welcome', welcome_screen)
    screen_manager.switch_to('welcome', screen)
    settings.game_loop(screen, screen_manager)


if __name__ == "__main__":
    main()
