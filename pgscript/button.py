import pygame
import textwrap
pygame.font.init()


class button():
  """class for simplifying the use of buttons"""
  def __init__(self, real_col, change_col, x, y, w, h, text, text_col=(0,0,0), anim=True, font_size=(30), wrapping=0, center=True):
    arial = pygame.font.SysFont('Arial', font_size)
    self.real_col = real_col
    self.change_col = change_col
    if anim:
        self.colour = [self.real_col[0],self.real_col[1],self.real_col[2],self.real_col[3]]
    else:
        self.colour = [self.real_col[0],self.real_col[1],self.real_col[2]]

    self.rect = pygame.Rect(x,y,w,h)
    self.center = center
    self.plain_text = text
    self.pressed = False
    self.wrapping = wrapping
    self.wrapped = [] 
    self.anim = anim 
    #text wrapping inside the button
    if self.wrapping:
      self.text = []
      self.wrapped = textwrap.wrap(text, self.wrapping)
      sliced = []
      for line in self.wrapped:
        line = line.split("%")
        for n in line:
            sliced.append(n)

      for n in sliced:
          self.text.append(arial.render(n, True, text_col))
    else:
        self.text = [arial.render(text, True, text_col).convert_alpha()]
  def draw(self, DISPLAY):
    btn = pygame.Surface((self.rect.width,self.rect.height), pygame.SRCALPHA)
    btn.fill(self.colour)
    DISPLAY.blit(btn, (self.rect.topleft))
    #pygame.draw.rect(DISPLAY, self.colour, self.rect)

    #centering the text in the middle of the button
    if self.center:
        ypos = self.rect.center[1] - (self.text[0].get_height()/2)
    else:
        ypos = self.rect.y + 15
    
    #printing the text in
    for line in self.text:
      DISPLAY.blit(line, (self.rect.center[0] - (line.get_width()/2), ypos))
      ypos += 30
    if self.anim:
        if self.isOver(pygame.mouse.get_pos()):
           if self.colour[3] < self.change_col[3]:
               self.colour[3] += 10
        else:
            if self.colour[3] > self.real_col[3]: #using 100 because self.real_col did not work
                self.colour[3] -= 5 
    else:
        if self.isOver(pygame.mouse.get_pos()):
            self.colour = self.change_col 
        else:
            self.colour = self.real_col

  def isOver(self, mouse_pos):
    if self.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
      return True

    return False 
  

  def update(self, event):
    #if event.type == pygame.MOUSEMOTION:
    if event.type == pygame.MOUSEBUTTONDOWN:
        if self.isOver(pygame.mouse.get_pos()):
            self.pressed = True
    
