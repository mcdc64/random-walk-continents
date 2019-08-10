import matplotlib.pyplot as plt
from ipywidgets import interact
import ipywidgets as widgets
import random
point_num = 50000
factor = 20
x_vals =[0]
y_vals =[0]
for i in range(0,point_num):
    x_vals.append(x_vals[-1]+random.randint(-1,1))
    y_vals.append(y_vals[-1]+random.randint(-1,1))
    if((x_vals[i]==0)and(y_vals[i]==0))and(i!=0):
        print("Returns home at n = "+str(i))

@interact(n=widgets.IntSlider(min=0, max=point_num, step=1, value=0))
def plots(n):
    plt.xlim(min(x_vals)-1,max(x_vals)+1)
    plt.ylim(min(y_vals)-1,max(y_vals)+1)
    plt.plot(x_vals[0:n],y_vals[0:n],color="#22b14c")
    
    ax = plt.gca()
    ax.set_facecolor('#0077bb')
    
    plt.plot(0,0,"ro") #plot the particle's initial position with a red dot
    plt.show()
