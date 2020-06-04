import pygame

class draggable_surface():
    def __init__(self, DISPLAY, surface, start_pos):
        self.display = DISPLAY
        self.surface = surface
        self.pos = start_pos
        self.offset = None #how far away the mouse is from the top left corner of the surface
        self.active = False

        
    
    def draw(self):
        self.display.blit(self.surface, self.pos)


    def update(self, event):
        mouse = pygame.mouse.get_pos()
        if self.isOver(mouse):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.active = True
                self.offset = (mouse[0] - self.pos[0], mouse[1] - self.pos[1])
            if event.type == pygame.MOUSEBUTTONUP:
                self.active = False
                self.offset = None

        if self.active:
            self.pos = (mouse[0] - self.offset[0], mouse[1] - self.offset[1])


    def isOver(self, mouse_pos):
        '''determine if the mouse cursor is hovering over'''
        if pygame.Rect(self.pos[0],self.pos[1],self.surface.get_width(),self.surface.get_height()).collidepoint(mouse_pos[0], mouse_pos[1]):
            return True

        return False 

    
    def get_pos(self):
       return self.pos

    def set_pos(self, new_pos):
       self.pos = new_pos
