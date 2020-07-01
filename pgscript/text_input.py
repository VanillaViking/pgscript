import pygame

pygame.font.init()
#FONT = pygame.font.SysFont('Arial', 32)
#SFONT = pygame.font.SysFont('Arial', 20)

class text_input():
    """text input class"""
    def __init__(self, DISPLAY,x, y, w, h, text ='',text_col=(0,0,0), active_col=(100,100,100), passive_col=(200,200,200), font_size=30):
        pygame.key.set_repeat(200,30)
        self.display = DISPLAY
        self.rect = pygame.Rect(x, y, w, h)
        self.active = False
        self.active_col = active_col
        self.passive_col = passive_col
        self.colour = self.passive_col
        self.text = text
        self.FONT = pygame.font.SysFont('arial', font_size)
        self.text_offset = 0

        self.text_surface = self.FONT.render(text,True, text_col)
        self.text_col = text_col
        self.clicked = False
        self.count = 0
        self.frame_count = -10

        self.text_surface = self.FONT.render(self.text[self.text_offset:self.get_visible_len()+1], True,self.text_col)
        self.cursor_shift_val = 0
        self.cursor_rect = pygame.Rect(self.rect.x +4, self.rect.y + 5, 3, self.text_surface.get_height() - 5)
        self.cursor_pos = 0


    def update(self, event, mouse_pos=None):
        if not mouse_pos:
            mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(mouse_pos):
                self.active = True
                self.colour = self.active_col
            else:
                self.active = False
                self.colour = self.passive_col

        if event.type == pygame.KEYDOWN: #logic for keypresses when the text field is focused
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    if self.cursor_pos > 0:
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

                elif event.key == pygame.K_RIGHT:
                    if self.cursor_pos < len(self.text):
                        self.cursor_pos += 1

                else:
                    if event.unicode:
                        self.text = self.text[:self.cursor_pos] + event.unicode + self.text[self.cursor_pos:]
                        self.cursor_pos += 1
                
                self.cursor_rect.x = self.rect.x +5+ self.FONT.size(self.text[self.text_offset:self.cursor_pos])[0] #size is from start of text to position of cursor

                while self.cursor_rect.x >= self.rect.x +self.rect.width - 20:
                    self.text_offset += 1
                    self.cursor_rect.x = self.rect.x +5+ self.FONT.size(self.text[self.text_offset:self.cursor_pos])[0] #size is from start of text to position of cursor

                if self.cursor_rect.x < self.rect.x+20 and self.text_offset:
                    if self.text_offset:
                        self.text_offset -= 1

                self.cursor_rect.x = self.rect.x +5+ self.FONT.size(self.text[self.text_offset:self.cursor_pos])[0] #size is from start of text to position of cursor
                self.text_surface = self.FONT.render(self.text[self.text_offset:self.get_visible_len()+1], True,self.text_col)


    def draw(self): 
            
        self.display.blit(self.text_surface, (self.rect.x+5,self.rect.y+5)) #text inside the textfield
        pygame.draw.rect(self.display, (self.colour), self.rect, 2) #text box 


        #cursor
        if self.active: 
            pygame.draw.rect(self.display, self.text_col, self.cursor_rect)
           
    def get_text(self):
        return self.text

    def clear_text(self):
        self.text = ''

    def set_text(self, text):
        self.text = text
        self.cursor_pos = 0
        self.cursor_rect.x = self.rect.x +5+ self.FONT.size(self.text[self.text_offset:self.cursor_pos])[0] #size is from start of text to position of cursor

        while self.cursor_rect.x >= self.rect.x +self.rect.width - 20:
            self.text_offset += 1
            self.cursor_rect.x = self.rect.x +5+ self.FONT.size(self.text[self.text_offset:self.cursor_pos])[0] #size is from start of text to position of cursor

        if self.cursor_rect.x < self.rect.x+20 and self.text_offset:
            if self.text_offset:
                self.text_offset -= 1

        self.cursor_rect.x = self.rect.x +5+ self.FONT.size(self.text[self.text_offset:self.cursor_pos])[0] #size is from start of text to position of cursor
        self.text_surface = self.FONT.render(self.text[self.text_offset:self.get_visible_len()+1], True,self.text_col)


    def get_visible_len(self):
        n = 0
        for n in range(self.text_offset, len(self.text)):
            if self.FONT.size(self.text[self.text_offset:n])[0]+10 >= self.rect.width:
                n-=1
                break
        
        return n
