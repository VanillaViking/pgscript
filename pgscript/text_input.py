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
        self.clicked = False
        self.count = 0
        self.anim_x = -10

        self.cursor_shift_val = 0
        self.cursor_rect = pygame.Rect(self.rect.x +4, self.rect.y + 5, 3, self.text_surface.get_height() - 5)
        if self.text:
            self.cursor_pos = len(self.text) -1
        else:
            self.cursor_pos = 0


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
                    if self.cursor_pos > 0:
                        self.cursor_rect.x -= FONT.size(self.text[self.cursor_pos-1])[0]
                        self.text = self.text[:self.cursor_pos-1] + self.text[self.cursor_pos:] 
                        self.cursor_pos -= 1
                elif event.key == pygame.K_RETURN:
                    self.active = False
                    self.colour = self.passive_col

                elif event.key == pygame.K_TAB:
                    self.active = False
                    self.colour = self.passive_col

                elif event.key == pygame.K_LEFT:
                    if self.cursor_pos > 0:
                        self.cursor_pos -= 1
                        self.cursor_rect.x -= FONT.size(self.text[self.cursor_pos])[0]

                elif event.key == pygame.K_RIGHT:
                    if self.cursor_pos < len(self.text):
                        self.cursor_rect.x += FONT.size(self.text[self.cursor_pos])[0]
                        self.cursor_pos += 1

                else:
                    self.text = self.text[:self.cursor_pos] + event.unicode + self.text[self.cursor_pos:]
                    self.cursor_rect.x += FONT.size(self.text[self.cursor_pos])[0] #add the size of the individual character, since the sizes vary
                    self.cursor_pos += 1
                self.text_surface = FONT.render(self.text, True,self.text_col)

    def draw(self): 
            
        self.display.blit(self.text_surface, (self.rect.x+5,self.rect.y+5))
        pygame.draw.rect(self.display, (self.colour), self.rect, 2)

        if self.active: 
            if self.count <= 200 and self.count >= 100:
                #pygame.draw.rect(self.display, (self.count, self.count, self.count), pygame.Rect(self.rect.x+10+self.text_surface.get_width(), self.rect.y + 5, 3, self.text_surface.get_height() - 5)) 
                pygame.draw.rect(self.display, (self.count, self.count, self.count), self.cursor_rect)
           
            self.count = (-(1/25) * ((self.anim_x - 50)**2)) + 200
            #self.cursor_rect.x = (self.rect.x + 10) + (self.cursor_pos * )

        self.anim_x += 1
        if self.anim_x >= 100:
            self.anim_x = -40
