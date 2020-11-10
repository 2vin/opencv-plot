import cv2
import numpy as np
import math
import time
from random import random

# Plot values in opencv program
class Plotter:
    def __init__(self, plot_width, plot_height,sample_buffer=None):
        self.width = plot_width
        self.height = plot_height
        self.color = (255, 0 ,0)
        self.plot_canvas = np.ones((self.height, self.width, 3))*255    
        self.ltime = 0
        self.plots = {}
        self.plot_t_last = {}
        self.margin_l = 10
        self.margin_r = 10
        self.margin_u = 10
        self.margin_d = 50
        self.sample_buffer = self.width if sample_buffer is None else sample_buffer


    # Update new values in plot
    def plot(self, val, label = "plot"):
        if not label in self.plots:
            self.plots[label] = []
            self.plot_t_last[label] = 0
            
        self.plots[label].append(int(val))
        while len(self.plots[label]) > self.sample_buffer:
            self.plots[label].pop(0)
            self.show_plot(label)    
    # Show plot using opencv imshow
    def show_plot(self, label):

        self.plot_canvas = np.zeros((self.height, self.width, 3))*255
        cv2.line(self.plot_canvas, (self.margin_l, int((self.height-self.margin_d-self.margin_u)/2)+self.margin_u ), (self.width-self.margin_r, int((self.height-self.margin_d-self.margin_u)/2)+self.margin_u), (0,0,255), 1)        

        # Scaling the graph in y within buffer
        scale_h_max = max(self.plots[label])
        scale_h_min = min(self.plots[label]) 
        scale_h_min = -scale_h_min if scale_h_min<0 else scale_h_min
        scale_h = scale_h_max if scale_h_max > scale_h_min else scale_h_min
        scale_h = ((self.height-self.margin_d-self.margin_u)/2)/scale_h if not scale_h == 0 else 0
        

        for j,i in enumerate(np.linspace(0,self.sample_buffer-2,self.width-self.margin_l-self.margin_r)):
            i = int(i)
            cv2.line(self.plot_canvas, (j+self.margin_l, int((self.height-self.margin_d-self.margin_u)/2 +self.margin_u- self.plots[label][i]*scale_h)), (j+self.margin_l, int((self.height-self.margin_d-self.margin_u)/2  +self.margin_u- self.plots[label][i+1]*scale_h)), self.color, 1)
        
        
        cv2.rectangle(self.plot_canvas, (self.margin_l,self.margin_u), (self.width-self.margin_r,self.height-self.margin_d), (255,255,255), 1) 
        cv2.putText(self.plot_canvas,f" {label} : {self.plots[label][-1]} , dt : {int((time.time() - self.plot_t_last[label])*1000)}ms",(int(0),self.height-20),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,255),2)
        cv2.circle(self.plot_canvas, (self.width-self.margin_r, int(self.margin_u + (self.height-self.margin_d-self.margin_u)/2 - self.plots[label][-1]*scale_h)), 2, (0,200,200), -1)
        
        self.plot_t_last[label] = time.time()
        cv2.imshow(label, self.plot_canvas)
        cv2.waitKey(1)


def single_sample():
    # Create dummy values using for loop 
    p = Plotter(400, 200,sample_buffer=200)

    for v in range(1,3000):
        
        p.plot(int(math.sin(v*3.14/180)*100),label='sin')
        
        p.plot(int(math.cos(v*3.14/180)*50),label='cos')



if '__main__' == __name__:
    single_sample()