import pygame
import threading
import time

pygame.font.init()

def draw_wait(event, duration):
    time.sleep(duration)
    event.set()


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
