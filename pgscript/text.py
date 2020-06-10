import pygame
import threading
import time

pygame.font.init()

def draw_wait(event, duration):
    time.sleep(duration)
    event.set()

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

def message(DISPLAY, text, font, color, pos, duration):
    text_surf = font.render(text, True, color)

    kill_message = threading.Event() #event is set to true when message needs to stop being drawn
    waiting_thread = threading.Thread(target=draw_wait, args=(kill_message,duration,))#kills message after waiting for the specified amount of time
    waiting_thread.start()

    while not kill_message.isSet():
        DISPLAY.blit(text_surf, pos)

    
    
class text():
    def __init__(self, DISPLAY ):
        pass
