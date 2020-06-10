import pygame

class scrolling_screen():
    def __init__(self, DISPLAY, vertical_size, v_scrollbar_pos, v_scrollbar_width, scroll_step):
        self.display = DISPLAY
        self.v_scroll_pos = 0
        self.scroll_step = scroll_step

        if v_scrollbar_pos == 'l':
            self.scrollbar_border = pygame.Rect(self.display.get_width() - v_scrollbar_width -1, 0, v_scrollbar_width +1, self.display.get_height())
        elif v_scrollbar_pos == 'r':
            self.scrollbar_border = pygame.Rect(0,0, v_scrollbar_width+1, self.display.get_height())

        self.surface = pygame.Surface((self.display.get_width(), self.display.get_height() * vertical_size)) #users need to draw onto this surfacce instead of display
    
    def draw(self):
        self.display.blit(self.surface, (self.v_scroll_pos, 0))

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 5 and (self.v_scroll_pos + self.surface.get_height()) > self.DISPLAY.get_height():   #SCROLL DOWN
                self.v_scroll_pos -= self.scroll_step 

            elif event.button == 4 and self.v_scroll_pos < 0:   #SCROLL UP
                self.v_scroll_pos += self.scroll_step


