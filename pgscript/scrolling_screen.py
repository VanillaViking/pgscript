import pygame
import pgscript

class scrolling_screen():
    def __init__(self, DISPLAY, vertical_size, v_scrollbar_pos, v_scrollbar_width, scroll_step, scrollbar_color):
        self.display = DISPLAY
        self.v_scroll_pos = 0
        self.scroll_step = scroll_step
        self.scrollbar_color = scrollbar_color
        self.objects = []
        self.vertical_size = vertical_size

        self.scroll_active = False
        self.scrollbar_offset = None
        
        if v_scrollbar_pos == 'l':
            self.scrollbar_border = pygame.Rect(self.display.get_width() - v_scrollbar_width -1, 0, v_scrollbar_width +1, self.display.get_height())
        elif v_scrollbar_pos == 'r':
            self.scrollbar_border = pygame.Rect(0,0, v_scrollbar_width+1, self.display.get_height())

        self.scrollbar = pygame.Rect(self.scrollbar_border.x + 1, 0, v_scrollbar_width, self.display.get_height()/vertical_size)

        self.surface = pygame.Surface((self.display.get_width(), self.display.get_height() * vertical_size), pygame.SRCALPHA) #users need to draw onto this surfacce instead of display
    
    def draw(self):
        self.surface.fill((255,255,255,0))
        for obj in self.objects:
            if type(obj) is pgscript.text.text:
                obj.draw()
            elif (obj.rect.y + obj.rect.height + self.v_scroll_pos) > 0 and (obj.rect.y + self.v_scroll_pos) < self.display.get_height():   #checking whether object is on the screen
                obj.draw()
        self.display.blit(self.surface, (0, self.v_scroll_pos))

        pygame.draw.rect(self.display, self.scrollbar_color, self.scrollbar_border, 1)
        pygame.draw.rect(self.display, self.scrollbar_color, self.scrollbar)


    def update(self, event):
        mouse_pos = pygame.mouse.get_pos()
        for i in self.objects:
            if type(i) is not pgscript.text.text:
                i.update(event, (mouse_pos[0],mouse_pos[1] - self.v_scroll_pos)) #adjusting mouse coordinates according to scrolled position

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 5 and (self.v_scroll_pos + self.surface.get_height()) > self.display.get_height():   #SCROLL DOWN
                self.scrollbar.y += int(self.scroll_step/self.vertical_size)

            elif event.button == 4 and self.v_scroll_pos < 0:   #SCROLL UP
                self.scrollbar.y -= int(self.scroll_step/self.vertical_size)


        #SCROLLBAR
        if self.scrollbar.collidepoint(mouse_pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.scroll_active = True
                self.scrollbar_offset = (mouse_pos[1] - self.scrollbar.y)

        elif event.type == pygame.MOUSEBUTTONUP:
            self.scroll_active = False
            self.offset = None

        if self.scroll_active:
            self.scrollbar.y = mouse_pos[1] - self.scrollbar_offset

            #bounds to prevent scrollbar going offscreen
        if self.scrollbar.y < 0:
            self.scrollbar.y = 0
        
        if self.scrollbar.y + self.scrollbar.height > self.display.get_height():
            self.scrollbar.y = self.display.get_height() - self.scrollbar.height

        self.v_scroll_pos = -1*(self.vertical_size)*(self.scrollbar.y)

    def add_objects(self, obj_list):
        self.objects = obj_list

