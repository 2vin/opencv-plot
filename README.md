# opencv-plot   
Plotting real time data in opencv using python   

This repo can be used to plot single as well as multiple values in OpenCV python.    
## opencv-plot.py   
Plot single integer values in realtime using this file.     

### Usage:        
### Create a plotter class object  
```
p = Plotter(400, 200) #(plot_width, plot_height)   
```   

### Create dummy values using for loop     
```
for v in range(500):    
	# call 'plot' method for realtime plot    
	p.plot(v/5)     
```     
![Results](https://github.com/2vin/opencv-plot/blob/master/opencv_plot.gif)`       
  
## opencv-multiplot.py  (Maximum: 9 values at a time)     
Plot multiple values in reallime  using this file.    

### Usage:    
### Create a plotter class object    
```
p = Plotter(400, 200, 3) #(plot_width, plot_height)    
```

### Create dummy values using for loop    
```
for v in range(500):    
	# call 'plot' method for realtime plot    
	v1 = random.randint(0,200) - 100       
	v2 = int(math.sin(v*3.14/180)*100)      
	v3 = int(math.cos(v*3.14/180)*100)        
	p.multiplot([v1, v2, v3]) #List of all values to be plotted        
```   
![Results](https://github.com/2vin/opencv-plot/blob/master/opencv_multiplot.gif)`       



