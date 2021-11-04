import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import animation

v1 = 1.1
v2 = 1
w = 1.3
h = 1.0

x1 = np.arange(-10, 10, v1)
len1 = len(x1)
y1 = np.zeros(len1)
x2 = np.zeros(len1)
y2 = np.arange(-10, -10+v2*len1, v2)
#yaw = [0.0, 0.5, 1.3, 1.7, 2.1]
fig = plt.figure()
fig.set_size_inches(9, 8)
plt.axis('equal')
#plt.grid()
ax = fig.add_subplot(111)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

car1 = patches.Rectangle((0, 0), 0, 0, fc='r')
car2 = patches.Rectangle((0, 0), 0, 0, fc='b')
road1 = patches.Rectangle((-10, -0.5*w), 20, 3*w, fc='grey')
road2 = patches.Rectangle((-1.5*w-0.2, -10), 3*w+0.2, 20, fc='grey')
car1.set_width(w)
car1.set_height(h)
car2.set_width(h)
car2.set_height(w)
line1, = ax.plot((-10,-1.5*w),(w,w),'w')
line2, = ax.plot((1.5*w,10),(w,w),'w')
line3, = ax.plot((-0.2,-0.2),(-10,-0.5*w),'w')
line4, = ax.plot((-0.2,-0.2),(3*w-0.5,10),'w')
def pointInRect(point,rect):
    x1, y1, w, h = rect
    x2, y2 = x1+w, y1+h
    x, y = point
    if (x1 < x and x < x2):
        if (y1 < y and y < y2):
            return True
    return False
def check_collision(c1, c2):
    c1_vertex = ((c1[0], c1[1]),(c1[0]+c1[2], c1[1]),(c1[0], c1[1]+c1[3]),(c1[0]+c1[2], c1[1]+c1[3]))
    c2_vertex = ((c2[0], c2[1]),(c2[0]+c2[2], c2[1]),(c2[0], c2[1]+c2[3]),(c2[0]+c2[2], c2[1]+c2[3]))
    for point in c1_vertex:
        if pointInRect(point, c2):
            return True
    for point in c2_vertex:
        if pointInRect(point, c1):
            return True
    return False
t = 0
for i in range(0, len1):
    c1 = (x1[i], y1[i], w, h)
    c2 = (x2[i], y2[i], h, w)
    if check_collision(c1, c2):
        t = i
        break
msg1 = "Collision will happen"
msg_text1 = ax.text(2.5, -6, msg1, fontsize=16, color='red')
msg2 = "in  seconds."
msg_text2 = ax.text(2.5, -7, msg2, fontsize=16, color='red')


def init():
    ax.add_patch(car1)
    ax.add_patch(car2)
    ax.add_artist(msg_text1)
    ax.add_artist(msg_text2)
    ax.add_patch(road1)
    ax.add_patch(road2)
    line1.set_ydata(w)
    line2.set_ydata(w)
    line3.set_xdata(-0.2)
    line4.set_xdata(-0.2)
    return car1,car2,line1,line2,line3,line4,road1,road2,msg_text1,msg_text2

def animate(i):
    car1.set_xy([x1[i], y1[i]])
    car2.set_xy([x2[i], y2[i]])
    if t!=0 and t>=i:
        msg = "in "+str(t-i)+" seconds."
        msg_text2.set_text(msg)
    if t!=0 and t==i:
        anim.event_source.stop()
    return road1,road2,line1,line2,line3,line4,car1,car2,msg_text1,msg_text2,

anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=len(x1),
                               interval=500,
                               blit=True)
ax.axis('off')
plt.show()