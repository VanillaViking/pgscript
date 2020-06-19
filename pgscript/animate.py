import threading
import time

def anim(start, end, func, args, frames, time_interval=0):
    '''runs a function with each specified value in the given range'''

    diff = []
    inc = []

    for f in range(len(start)):
        diff.append(end[f] - start[f])  #difference between end and start values (used to calculate the value of the increment)

    for i in diff:
        inc.append(i/frames)            #increment is the difference divided by the number of frames that the animation lasts.

    for l in range(frames):
        
        for c,i in enumerate(start):    #increment the start value
            start[c] = i + inc[c]
        
        func(*args, start)              #run the function with the current start value
        time.sleep(time_interval)

    func(*args, end)                    #to make sure the animation ends at desired value


def animate(start, end, func, args, frames, time_interval=0):
    
    #animate on a separate thread
    anim_handler = threading.Thread(target=anim, args=(start, end, func, args, frames, time_interval))
    anim_handler.start() 


class interrupt_anim():
    '''class for animations that need to be stopped before they finish executing'''
    def __init__(self): 
        self.stop = False
        self.anim_handler = None

    def int_anim(self, start, end, func, args, frames, time_interval=0):
        diff = []
        inc = []

        for f in range(len(start)):
            diff.append(end[f] - start[f])  #difference between end and start values (used to calculate the value of the increment)

        for i in diff:
            inc.append(i/frames)            #increment is the difference divided by the number of frames that the animation lasts.

        for l in range(frames):
                
            for c,i in enumerate(start):    #increment the start value
                start[c] = i + inc[c]
            
            func(*args, start)              #run the function with the current start value
            time.sleep(time_interval)

            if self.stop:
                break
        if not self.stop:
            func(*args, end)                    #to make sure the animation ends at desired value


    def int_animate(self, start, end, func, args, frames, time_interval=0):
        self.stop = False
        self.anim_handler = threading.Thread(target=self.int_anim, args=(start, end, func, args, frames, time_interval))
        self.anim_handler.start()


    def interrupt(self):
        self.stop = True
        self.anim_handler = None
