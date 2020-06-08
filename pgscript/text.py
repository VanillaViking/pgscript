import pygame
import threading

pygame.font.init()


def draw_surface(DISPLAY, surface, pos, frames=1):
    for n in frames:
        DISPLAY.blit(surface, pos)



def message(DISPLAY, text, font, color, pos, frames):
    text_surf = font.render(text, True, color)
    msg_handler = threading.Thread(target=draw_surface, args=(DISPLAY, text_surf, pos, frames,)) 
    msg_handler.start()

class text():
    def __init__(self, DISPLAY):
        pass
