import matplotlib.pyplot as plt
import numpy as np
from copy import copy
from matplotlib.colors import Colormap
import matplotlib.patches as patches

def abline(slope, intercept,color,linewidth=8):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, color,linewidth=linewidth)
    
#start from left bottom
number=19
j=np.zeros((number,number))
num=number*number
direction="right"
threshold=number-1
x=threshold
y=-1
special=[20,23,128,139,148,152,171,219,239,283,297,339]
for i in range(num):

    if direction =="right":
        if y!=threshold and j[x][y+1]==0:
            y+=1
        else:
            direction="up"
            x-=1
    elif direction =="up":
        if x!=0 and j[x-1][y]==0:
            x-=1
        else:
            direction ="left"
            y-=1
    elif direction =="left":
        if y!=0 and j[x][y-1]==0:
            y-=1
        else:
             direction="down"
             x+=1
    elif direction =="down":
        if x!=threshold and j[x+1][y]==0:
            x+=1
        else:
             direction="right"
             y+=1
    j[x][y]=num-i
    if num-i in special:
        j[x][y]=num+1


size = number
data = j

# Limits for the extent
x_start = 0
x_end = number
y_start = 0
y_end = number

extent = [x_start, x_end, y_start, y_end]

#declare empty palette
#cmap=plt.cm.jet
#palette = copy(plt.get_cmap('viridis_r'))
#Colormap.set_under('gray', color='w')  # 1.0 represents not transparent
# The normal figure

fig = plt.figure()
ax = fig.add_subplot(111)
#fig, ax = plt.subplots(1, 1)
im = ax.imshow(data,vmin=num,extent=extent, cmap='gray_r')

# Add the text
jump_x = (x_end - x_start) / (2.0 * size)
jump_y = (y_end - y_start) / (2.0 * size)
x_positions = np.linspace(start=x_start, stop=x_end, num=size, endpoint=False)
y_positions = np.linspace(start=y_start, stop=y_end, num=size, endpoint=False)

for y_index, y in enumerate(y_positions):
    for x_index, x in enumerate(x_positions):
        label = data[threshold-y_index, x_index]
        text_x = x + jump_x
        text_y = y + jump_y
        label=int(label)
        ax.text(text_x, text_y, label, color='black', ha='center', va='center', fontsize=24,fontweight='bold')
#draw circle
circle_center=number/2
radius=(2*23.2*23.2)**(1/2)/2
circle2 = plt.Circle((circle_center, circle_center), radius, color='black',fill=False,linewidth=4)
ax.add_artist(circle2)

#draw circle
circle_center=number/2
radius=(2*number*number)**(1/2)/2
circle = plt.Circle((circle_center, circle_center), radius, color='black',fill=False,linewidth=4)
ax.add_artist(circle)

bound=int(circle_center-radius-1)
#print(circle_center)
#draw square
dia_square=((radius*radius*2)**(1/2))

ax.add_patch(
     patches.Rectangle(
        (circle_center, circle_center-radius),
        dia_square,
        dia_square,
        angle=45,
        color='#e32620',
        fill=True,
        alpha=0.2# remove background
     ) ) 
#------------tan 30 is 0.57735026919
ratio_of_triangle=0.57735026919*1.5
triangle=np.array([[-4,9.5],[-4+1.5*radius,9.5+ratio_of_triangle*radius],[-4+1.5*radius,9.5-ratio_of_triangle*radius]])
t1 = plt.Polygon(triangle[:3,:], color='#5abf5a',fill=True,alpha=0.4)
plt.gca().add_patch(t1)

major_ticks = np.arange(bound-3,bound+2*radius+4, 1)
#minor_ticks = np.arange(0, number, 5)

ax.set_xticks(major_ticks)
#ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks)
#ax.set_yticks(minor_ticks, minor=True)
#fig.colorbar(im)
abline(0, 9.5,'r-')
abline(0.183,16.05,'g-')
abline(-0.166,2.85,'g-')
#tan 60 is 1.73205080757
abline(1.73205080757,-6.9,'g-')
abline(-1.73205080757,25.9,'g-')
abline(-0.09,14.4,'g--')
abline(0.72,7.95,'g--')
abline(1.09,-7.3,'g--')
abline(1.4,-14.7,'r--')
abline(4.08,-77.5,'r')
abline(-8.8,194.5,'r')
plt.axvline(9.5, 0, 1,color='red',linewidth=8)
plt.plot([-6,-6], [15,4],'r--',linewidth=8)
plt.plot([7.7,-3], [26,-1],'m-',linewidth=8)
plt.plot([18.3,8.5], [23.4,-7],'m-',linewidth=8)
plt.plot([17.6,13.3], [23.6,-6.5],'m-',linewidth=8)
plt.plot([6.3,2.3], [25.6,-5.4],'m-',linewidth=8)
plt.axvline(19, 0, 1,color='#a3a10b',linewidth=4)
plt.axvline(0, 0, 1,color='#a3a10b',linewidth=4)
abline(0,0,'#a3a10b',linewidth=4)
abline(0,19,'#a3a10b',linewidth=4)
plt.grid()
#Graph max size
plt.xlim((-9,28))
plt.ylim((-9,28))
abline(0.61735026919,3.7,'b')
abline(-0.57735026919,15,'b')
#draw circle
circle_center=number/2
radius=0.5
circle3 = plt.Circle((8,17.6), radius, color='green')
ax.add_artist(circle3)
#draw circle
circle_center=number/2
radius=0.5
circle4 = plt.Circle((6.8,13), radius, color='green')
ax.add_artist(circle4)
#draw circle
circle_center=number/2
radius=0.5
circle5 = plt.Circle((9.9,13.6), radius, color='green')
ax.add_artist(circle5)
#draw circle
circle_center=number/2
radius=0.5
circle5 = plt.Circle((12.8,6.7), radius, color='green')
ax.add_artist(circle5)
#draw circle
circle_center=number/2
radius=0.5
circle6 = plt.Circle((8.2,1.5), radius, color='green')
ax.add_artist(circle6)
#draw circle
circle_center=number/2
radius=0.5
circle7 = plt.Circle((-6.1,9.9), radius, color='red')
ax.add_artist(circle7)
#draw circle
circle_center=number/2
radius=0.5
circle8 = plt.Circle((14.6,5.9), radius, color='red')
ax.add_artist(circle8)
#draw circle
circle_center=number/2
radius=0.5
circle9 = plt.Circle((20.8,10.8), radius, color='red')
ax.add_artist(circle9)
#draw circle
circle_center=number/2
radius=0.5
circle10 = plt.Circle((20.6,6.8), radius, color='red')
ax.add_artist(circle10)
from datetime import datetime
now = datetime.now()
a = datetime(2020,3,21,0,0,0)

import math
current_angle = (now.timestamp()-a.timestamp())/31600000*360
slope = -math.tan(math.radians(current_angle))
abline(slope,9.5-9.5*slope,'goldenrod',linewidth=16)
#now.date
#--------
plt.text(9.5, -8, "Dec 23", fontsize=48)
plt.text(18, -5.2, "Nov 22", fontsize=48)
plt.text(24,1.2, "Oct 22", fontsize=48)
plt.text(26,9.5, "Sep 21", fontsize=48)
plt.text(23.7,17.7, "Aug 21", fontsize=48)
plt.text(16.6,24.3, "Jul 22", fontsize=48)
plt.text(9.7,26, "Jun 21", fontsize=48)
plt.text(1,24.5, "May 21", fontsize=48)
plt.text(-5.4,18.2, "Apr 21", fontsize=48)
plt.text(-9,9.5, "Mar 21", fontsize=48)
plt.text(-6.4,0, "Feb 19", fontsize=48)
plt.text(-0.5,-5.6, "Jan 22", fontsize=48)
#-------
plt.text(9.5,-5, "270", fontsize=48)
plt.text(16,-3, "240", fontsize=48)
plt.text(20,2, "210", fontsize=48)
plt.text(23,9.5, "180", fontsize=48)
plt.text(20.5,17, "150", fontsize=48)
plt.text(16.5,21, "120", fontsize=48)
plt.text(9.5,23, "90", fontsize=48)
plt.text(2,22, "60", fontsize=48)
plt.text(-3.5,16, "30", fontsize=48)
plt.text(-4.5,9.5, "0", fontsize=48)
plt.text(1,-2.5, "300", fontsize=48)
plt.text(-3.5,2.5, "330", fontsize=48)
#----------------
plt.text(-7,23, now.strftime('%Y-%m-%d'),color='goldenrod', fontsize=48)
plt.text(-9,26, str(current_angle)+"°",color='goldenrod', fontsize=48)
fig.set_size_inches(60.,36.)
plt.savefig('100dpi.png', dpi=100)
#plt.savefig('200dpi.png', dpi=200)
#plt.show()
