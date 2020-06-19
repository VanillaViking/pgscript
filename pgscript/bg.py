import pygame
import threading
import random
import time

class scrolling_bg():
    def __init__(self, DISPLAY, bg_color, image_paths, objects):
        self.bg_color = bg_color
        self.images = []
        self.display = DISPLAY
        self.objects_a = [] #[image, [x,y], speed]
        self.stop = False
        
        for n in image_paths:
            self.images.append(pygame.image.load(n).convert_alpha())
        for n in range(objects):
            self.objects_a.append([random.randint(0,len(image_paths)-1), [random.randint(15,self.display.get_width() - 15),random.randint(15, self.display.get_height() - 15)], random.randint(4,20)/10])

    def draw(self):
        self.display.fill(self.bg_color)

        for n in self.objects_a:
            self.display.blit(self.images[n[0]], (n[1][0],int(n[1][1])))
        
    def update(self):
        while not self.stop:
            for c,n in enumerate(self.objects_a):
                if n[1][1] < (0 - self.images[n[0]].get_height()): #if off screen:
                    self.objects_a[c][1][1] = self.display.get_height() #reset height to bottom
                    self.objects_a[c][1][0] = random.randint(15,self.display.get_width() - 15) #change x position
                else:
                    self.objects_a[c][1][1] -= self.objects_a[c][2] #move up scren
            time.sleep(0.02)

            #print("height",self.objects_a[0][1][1])

    def anim_start(self):
        thr_a = threading.Thread(target=self.update)
        thr_a.setDaemon(True)
        thr_a.start()


    def kill(self):
        self.stop = True
        print("kil")           


class parallax_bg():
    def __init__(self, DISPLAY, image_path):
        self.display = DISPLAY
        self.ratio = 1.02 #scales the background 1.2 times the display for parallax purposes

 
        self.image = pygame.transform.scale(pygame.image.load(image_path), (int(DISPLAY.get_width() * self.ratio), int(DISPLAY.get_height() * self.ratio))).convert_alpha()
 
    
    def draw(self):
        '''In order to acheive a parallax illusion, the bg needs to move slightly in the opposite direction of the mouse. this can be done by firstly scaling up the background slightly bigger than the screen, so that we have room to move. Secondly, we can divide the mouse position by the same amount that we multiplied the bg. This ensures that the bg only moves very slightly. Lastly, we multiply the mouse position by -1 so that the bg moves in the opposite direction'''
        self.display.blit(self.image, (int(pygame.mouse.get_pos()[0] * (1-self.ratio)),int(pygame.mouse.get_pos()[1] * (1-self.ratio))))
        #print((int(pygame.mouse.get_pos()[0] * (1-self.ratio)),int(pygame.mouse.get_pos()[1] * (1-self.ratio))))



        









