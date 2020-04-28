import pygame

pygame.font.init()
FONT = pygame.font.SysFont('Arial', 32)
SFONT = pygame.font.SysFont('Arial', 20)

class text_input():
    """text input class"""
    def __init__(self, DISPLAY,x, y, w, h, text ='',text_col=(0,0,0), active_col=(100,100,100), passive_col=(200,200,200)):
        self.display = DISPLAY
        self.rect = pygame.Rect(x, y, w, h)
        self.active = False
        self.active_col = active_col
        self.passive_col = passive_col
        self.colour = self.passive_col
        self.text = text
        self.text_surface = FONT.render(text,True, text_col)
        self.text_col = text_col
        self.anim = anim 
        self.clicked = False
        self.count = 0
        self.anim_x = -10

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
                self.colour = self.active_col
            else:
                self.active = False
                self.colour = self.passive_col
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == pygame.K_RETURN:
                    self.active = False
                    self.colour = self.passive_col
                elif event.key == pygame.K_TAB:
                    self.active = False
                    self.colour = self.passive_col
                else:
                    self.text += event.unicode
                self.text_surface = FONT.render(self.text, True,self.text_col)

    def draw(self): 
            
        self.display.blit(self.text_surface, (self.rect.x+5,self.rect.y+5))
        pygame.draw.rect(self.display, (self.colour), self.rect, 2)
        if self.active: 
            if self.count <= 200 and self.count >= 100:
                pygame.draw.rect(self.display, (self.count, self.count, self.count), pygame.Rect(self.rect.x+10+self.text_surface.get_width(), self.rect.y + 5, 3, self.text_surface.get_height() - 5)) 
           
            self.count = (-(1/25) * ((self.anim_x - 50)**2)) + 200

        self.anim_x += 1
        if self.anim_x >= 100:
            self.anim_x = -40
