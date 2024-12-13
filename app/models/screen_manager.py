class ScreenManager:
    def __init__(self):
        self.screens = {}
        self.current_screen = None
        self.current_crowd = None

    def add_screen(self, name, screen):
        self.screens[name] = screen

    def switch_to(self, name, screen):
        self.current_screen = self.screens[name]
        self.current_screen.initialize(screen)

    def get_current_screen(self):
        return self.current_screen

    def set_crowd(self, crowd):
        self.current_crowd = crowd

    def get_current_crowd(self):
        return self.current_crowd

    def handle_events(self, events):
        self.current_screen.handle_events(events)

    def update(self, delta_time):
        self.current_screen.update(delta_time)

    def render(self, screen):
        self.current_screen.render(screen)
