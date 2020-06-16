import pygame
import threading
import time
import textwrap

pygame.font.init()

class text():
    def __init__(self, DISPLAY, font, color):
        self.display = DISPLAY
        self.font = font
        self.color = color
        self.draw_group = []
        self.wrapped_text_end = None
        
    def message(self, text, pos, duration=0, center=False):
        """displays a single message on screen. can have a duration"""
        text_surf = self.font.render(text, True, self.color)

        if center: #center the text at the given position?
            pos = (pos[0] - text_surf.get_width()/2, pos[1] - text_surf.get_height()/2) 
        text_obj = (text_surf,pos)

        exist = False
        for s,p in self.draw_group: #checking whether object already exists in the draw list
            if text_obj[1] == p:
                exist = True
                break

        if not exist:
            self.draw_group.append(text_obj)

            self.text_end = pos[1] + self.font.size(text)[1]

            if duration: #if a duration is given, start the wait timer on a different thread
                message_wait_thread = threading.Thread(target=self.message_timer, args=(text_obj, duration))
                message_wait_thread.start()

       
    def draw(self):
        for surface,pos in self.draw_group:
            self.display.blit(surface, pos)

    def message_timer(self, obj, duration): #function to be run on separate thread
       time.sleep(duration) 
       self.draw_group.remove(obj)
    
    def wrapped_text(self, text, pos, length_limit, line_spacing):
        wrapped = False
        for n in range(len(text)):
            if self.font.size(text[:n])[0] >= length_limit:
                lines = textwrap.wrap(text, n)
                wrapped = True
                break

        if not wrapped:
            lines = [text]

        y_offset = 0
        for line in lines:
            text_obj = [self.font.render(line, True, (self.color)), (pos[0], pos[1] + y_offset)]
            self.draw_group.append(text_obj)
            y_offset += self.font.size(line)[1] + line_spacing

        self.text_end = pos[1] + y_offset

        
