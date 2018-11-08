import time
import random
from tkinter import *

HEIGHT = 600
WIDTH = 800

tk = Tk()
canvas = Canvas(tk,width=WIDTH,height=HEIGHT)
tk.title = ('Bouncing Balls')
canvas.pack()

class Ball:
    def __init__(self,color):
        self.xspeed=random.randrange(-10,10)
        self.yspeed=random.randrange(-10,10)
        if self.xspeed > -2 and self.xspeed < 2:
            self.xspeed = 5
        if self.yspeed > -2 and self.yspeed < 2:
            self.yspeed = 5
        if self.xspeed == 5:
            color='green'
        if self.yspeed == 5:
            color = 'blue'
        self.shape=canvas.create_oval(10,10,30,30,fill=color)
        

    def move(self):
        canvas.move(self.shape,self.xspeed,self.yspeed)
        pos=canvas.coords(self.shape)
        if 275 < pos[3] < 325 and 375 < pos[2] < 425:
            self.xspeed=0
            self.yspeed=0
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.yspeed=-self.yspeed
        if pos[2] >=WIDTH or pos[0] <= 0:
            self.xspeed = -self.xspeed

balls = []
for i in range(200):
    balls.append(Ball('red'))

while True:
    for ball in balls:
        ball.move()
    tk.update()
    time.sleep(0.01)
        
