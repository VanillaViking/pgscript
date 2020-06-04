import pygame


class scrolling_screen():
    def __init__(self, DISPLAY, vertical_size, v_scrollbar_pos):
        self.display = DISPLAY

        self.surface = pygame.Surface((self.display.get_width(), self.display.get_height() * vertical_size))
    
    def get_surface(self):
        return self.surface


