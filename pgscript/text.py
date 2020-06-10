import pygame
import threading
import time

pygame.font.init()


class text():
    def __init__(self, DISPLAY, font, color):
        self.display = DISPLAY
        self.font = font
        self.color = color
        self.draw_group = []
        
    def message(self, text, pos, duration=0):
        text_surf = self.font.render(text, True, self.color)
        text_obj = [text_surf,pos]
        self.draw_group.append(text_obj)

        if duration:
            message_wait_thread = threading.Thread(target=self.message_timer, args=(text_obj, duration))
            message_wait_thread.start()

       
    def draw(self):
        for surface,pos in self.draw_group:
            self.display.blit(surface, pos)

    def message_timer(self, obj, duration):
       time.sleep(duration) 
       self.draw_group.remove(obj)
