class ScreenManager:
    def __init__(self):
        self.screens = {}
        self.current_screen = None

    def add_screen(self, name, screen):
        self.screens[name] = screen

    def switch_to(self, name):
        self.current_screen = self.screens[name]
        self.current_screen.initialize()

    def handle_events(self, events):
        self.current_screen.handle_events(events)

    def update(self, delta_time):
        self.current_screen.update(delta_time)

    def render(self, screen):
        self.current_screen.render(screen)
