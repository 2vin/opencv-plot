<a href="https://linkedin.com/in/2vin"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></img></a>
<a href="https://connect.vin"><img src="https://img.shields.io/badge/website-FF6A00?style=for-the-badge&logo=About.me&logoColor=white"></img></a>

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



## cvPLOT.py (use different label for each plot)   
Plot multiple values in reallime in multiwindows with a simple 

### Usage:    
### Create a plotter class object    
```
p = Plotter(400, 200, 100) #(plot_width, plot_height, sample_count)    
```

### Create dummy values using for loop    
```
p = Plotter(400, 200,sample_buffer=200)
    
    for v in range(1,3000):
        
        p.plot(int(math.sin(v*3.14/180)*100),label='sin') ## Add label 'sin' to show in a seperate window
        
        p.plot(int(math.cos(v*3.14/180)*50),label='cos')     
```   
![Results](https://github.com/Parrytoss/opencv-plot/blob/featurefull/cvPLOT_sin.gif)`       

