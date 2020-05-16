import pygame
import textwrap
from pgscript import animate

pygame.font.init()

class button():
  """class for simplifying the use of buttons"""
  def __init__(self, DISPLAY, real_col, change_col, x, y, w, h, text, text_col=(0,0,0), anim=False, font_size=(30), wrapping=0, text_center=True):
    arial = pygame.font.SysFont('Arial', font_size)

    self.display = DISPLAY
    self.real_col = real_col
    self.change_col = change_col
    self.active = False

    self.colour = self.real_col[:]

    self.rect = pygame.Rect(x,y,w,h)
    self.center = text_center
    self.plain_text = text
    self.pressed = False
    self.wrapping = wrapping
    self.wrapped_text = [] 
    self.anim = anim 

    self.anim_handler = animate.interrupt_anim()

    #text wrapping inside the button
    if self.wrapping:
      self.text = []
      self.wrapped_text = textwrap.wrap(text, self.wrapping)
      sliced = []

      for line in self.wrapped_text:
        line = line.split("%")
        for n in line:
            sliced.append(n)

      for n in sliced:
          self.text.append(arial.render(n, True, text_col))
    else:
        self.text = [arial.render(text, True, text_col).convert_alpha()]


  def draw(self):
    '''the button is drawn onto a display surface'''
    btn = pygame.Surface((self.rect.width,self.rect.height), pygame.SRCALPHA)
    btn.fill(self.colour)
    self.display.blit(btn, (self.rect.topleft))

    #centering the text in the middle of the button
    if self.center:
        ypos = self.rect.center[1] - (self.text[0].get_height()/2)
    else:
        ypos = self.rect.y + 15
    
    #printing the text in
    for line in self.text:
      self.display.blit(line, (self.rect.center[0] - (line.get_width()/2), ypos))
      ypos += 30

    if self.anim:
        if self.isOver(pygame.mouse.get_pos()) != self.active: #only calls animation function once when button state changes
            self.active = not self.active
            
            #interruptable animations are used in case the button state changes faster than the animations execute
            if self.active:
                self.anim_handler.interrupt() 
                self.anim_handler.int_animate(self.colour[:], self.change_col[:], self.anim_button, [],100)   
            else:
                self.anim_handler.interrupt()
                animate.animate(self.colour[:], self.real_col[:], self.anim_button, [],100)   

    else:
        if self.isOver(pygame.mouse.get_pos()):
            self.colour = self.change_col[:] 
        else:
            self.colour = self.real_col[:]

  def isOver(self, mouse_pos):
    '''determine if the mouse cursor is hovering over the button'''
    if self.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
      return True

    return False 

  def update(self, event):
    '''update the button given the coordinates of the mouse'''
    if event.type == pygame.MOUSEBUTTONDOWN:
        if self.isOver(pygame.mouse.get_pos()):
            self.pressed = True


  def anim_button(self, start): #function to be run with the animation tool
    self.colour = start

  def get_state(self):
      return self.pressed

  def reset_state(self):
      self.pressed = False


