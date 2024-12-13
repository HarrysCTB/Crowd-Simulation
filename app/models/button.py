import pygame


class Button:
    def __init__(self, text, rect, color, action):
        self.text = text
        self.rect = pygame.Rect(rect)
        self.color = color
        self.action = action

    def draw(self, screen):
        # Crée une surface transparente pour le bouton
        button_surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)

        # Dessine le rectangle sur la surface transparente
        pygame.draw.rect(button_surface, (0, 0, 255, 128), button_surface.get_rect())

        # Crée une police
        font = pygame.font.Font("assets/Roboto-Regular.ttf", 36)

        # Transforme le texte en surface
        text_surface = font.render(self.text, True, self.color)

        # Calcule la position pour centrer le texte
        text_rect = text_surface.get_rect(center=button_surface.get_rect().center)

        # Blitte le texte sur la surface du bouton
        button_surface.blit(text_surface, text_rect)

        # Dessine la surface transparente (avec texte) sur l'écran principal
        screen.blit(button_surface, self.rect.topleft)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()