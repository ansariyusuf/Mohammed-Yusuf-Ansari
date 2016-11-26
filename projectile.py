from Tkinter import *
from math import *
from tkMessageBox import *
from PIL import ImageTk, Image
import random
velocity=0
angle=0
y=0
x=0
xcoordinate=[]
ycoordinate=[]
index=0
''' the class circle creates a circle object of a given radius on a particular coordinate of the canvas.
the class has functions such as move and draw which are resposible for changing the circle's coordinate and redrawing the circle
at the new ocation. the reset function set the x coordinate and the y coordinate to (0,0)''' 
class Circle:
        colors = ["red","blue","green","yellow","orange","purple","black","pink","white","cyan"]
        def __init__(self,x,y):
            self.r = 10
            self.color = random.choice(Circle.colors)
            self.x = x
            self.y = y
            self.me = None
        def move(self,xoffset,yoffset):
            self.x = xoffset-10
            self.y = yoffset-10
        def reset(self):
            self.x=0
            self.y=0
        def draw(self,c):
            if self.me != None:
                c.delete(self.me)
            self.me = c.create_oval(self.x,self.y,self.x+(self.r*2),self.y+(self.r*2),fill=self.color)
''' the function takes in the the velocity and the angle as the global variable it then genrates the horizontal velocity which is always constant
in the projectile motion. it then uses the x coordinate of the ball, time and the velocity of the ball to genrate the vertical velocity. the function then displays the
horizontal and vertical velocities as a text label on the window.'''
def data():
    global velocity
    global angle
    global xcod
    global window2
    vx=velocity*cos(radians(angle))
    t=xcod/vx
    vy=(velocity*sin(radians(angle)))-(9.8*t)
    text_label1=Label(window2,text='Horizontal Velocity: '+str(round(vx,2))+' \n Vertical velocity: '+str(round(vy,2)),relief=RAISED,font=("Helvetica", 16),bg='light green')
    text_label1.pack()
    text_label1.place(x=920,y=500)

'''this is the most important function of this program. the function takes in two list as global variables and fills the xcoordiante list with the values from zero to the
maximum range of the projectile. the values differ by an offset of 0.1. the function then uses the equation of trajectory to gereate the y values for every x value
in the the xccordinate list and then it appends the y values in the ycoordinate list. the function also generates time of flight, range , maximum height as text labels
and diplays it on a window.the window is also created by the function. the window also has a canvas which is used to display the simulation. the projectile function
calls the animate function which is responsible for the producing a simulation. this function also has an another cool feature which based on mouse clicks. the function detects
the mouse clickks and moves the ball on to that point on the trajectory to dispaly the horizontal and the vertical velocities at that point.'''

def projectile():
    global velocity
    global angle
    global x
    global y
    global xcoordinate
    global ycoordinate
    global canvas1
    global window2
    global range_of_projectile
    global ball
    global index
    index=0
    xcoordinate=[]
    ycoordinate=[]
    ball=Circle(0,0)
    print velocity
    print angle
    if int(velocity)<0:
        showinfo(title='ERROR',message='please enter a positive velocity')
        return
    if int(angle)<0 or int(angle)>90:
        showinfo(title='ERROR',message='please enter the angle value between 0 and 90 degrees')
        return
    window2=Toplevel()                                 # window and canvas for the simulation
    window2.title('Projectile Motion')
    window2.geometry('1200x700')

    background1= ImageTk.PhotoImage(Image.open("green background.png"))
    background_label1 = Label(window2, image=background1)
    background_label1.pack()
    background_label1.place(x=0,y=0)
    
    background= ImageTk.PhotoImage(Image.open("ptb.jpg"))
    canvas1=Canvas(window2,bg='light green',width=800,height=600)
    canvas1.create_image(400,300,image=background)
    canvas1.pack()
    canvas1.place(x=100,y=0)
    
    time_of_flight=(2*velocity*sin(radians(angle)))/9.8                         #time of flight, range , maximum height
    maximum_height=(velocity*sin(radians(angle)))**2/(2*9.8)
    range_of_projectile=((velocity**2)*sin(2*radians(angle)))/9.8

    i=0
    while i<=((range_of_projectile)):           # xcoordinate and ycoordiante lists
        xcoordinate.append(round(i,2))
        i=i+0.1
        
    t=tan(radians(angle))
    c=cos(radians(angle))*cos(radians(angle))
    v=velocity*velocity
    
    for i in range(len(xcoordinate)):
        x=xcoordinate[i]
        y=550-(x*t-(9.8*(x*x))/(2*v*c))     #equation of trajectory
        ycoordinate.append(round(y,2))
        
    canvas1.after(2000,animate)
    
    text_label2=Label(window2,text='Horizontal Range: '+str(round(range_of_projectile,2))+'m',relief=RAISED,font=("Helvetica", 16),bg='light green')# text labels for the information
    text_label2.pack()
    text_label2.place(x=920,y=200)
    text_label3=Label(window2,text='Time of Flight: '+str(round(time_of_flight,2))+'s',relief=RAISED,font=("Helvetica", 16),bg='light green')
    text_label3.pack()
    text_label3.place(x=920,y=400)
    text_label4=Label(window2,text='Maximum Hieght: '+str(round(maximum_height,2))+'m',relief=RAISED,font=("Helvetica", 16),bg='light green')
    text_label4.pack()
    text_label4.place(x=920,y=300)
    
    canvas1.bind("<Button-1>",LeftClicked)
    window2.mainloop()
''' the function detects the mouse click on the canvas and and recieves the x coordinate of the click. it uses this xcod and the data function to generate the horizontal 
and the vertical velocities of the ball. if the click is within the range then the ball is moved the position of the click and the text label displays the horizonatal
and vertical velocities at that point.'''
def LeftClicked(e):
    global ball
    global angle
    global velocity
    global canvas1
    global xcod
    global range_of_projectile
    t=tan(radians(angle))
    c=cos(radians(angle))*cos(radians(angle))
    v=velocity*velocity
    xcod=e.x
    ycod=550-(xcod*t-(9.8*(xcod*xcod))/(2*v*c))
    ball.reset()
    if xcod<=range_of_projectile:
            ball.move(xcod,ycod)
            ball.draw(canvas1)
            data()
''' the animate function is responsible for showing the simulation on the canvas. the function takes the xcoordiante and ycoordinate list along
with the index variable as globals. the function moves through the xcoordinate and ycoordinate list simulatneoulsy and moves the ball to the right
coordinate as per the list. while the index value is less than the length of the list the process is repeated. this process is repeated every 1 milli second
which gives us a visual effect of the prokectile motion. once the index reaches the end of the list then the animate function generates the trajectory path
by joining the coordinates present in the xcoordinate and the ycoordinate list.''' 

def animate():
    global canvas1
    global xcoordinate
    global ycoordinate
    global ball
    global index
    if index<len(xcoordinate):
        if index>len(xcoordinate)/4:
            ball.move(xcoordinate[index],ycoordinate[index]) #the function takes the xcoordiante and ycoordinate list along
                                                             #with the index variable as globals. the function moves through the xcoordinate
                                                             #and ycoordinate list simulatneoulsy and moves the ball to the right
                                                             #coordinate as per the list.
            ball.draw(canvas1)
            index+=18    # incrementing index
        else:
            ball.move(xcoordinate[index],ycoordinate[index])
            ball.draw(canvas1)
            index+=15      # incrementing index
        canvas1.after(1,animate)
    else:
        for i in range(len(ycoordinate)-2):
            canvas1.create_line(xcoordinate[i],ycoordinate[i],xcoordinate[i+1],ycoordinate[i+1])
'''the function is responsible for getting the velocity in the correct format from the user and then returns the velocity back'''
def setvelocity(e1):
    global velocity
    if askyesno(title='set velocity',message='Are you sure you want to set velocity to this value'):
        velocity=e1.get()
        velocity=float(velocity)
        if velocity<0.0:
            showinfo(title='ERROR',message='please enter a positive velocity')
    return (velocity)
'''the function is responsible for getting the angle in the correct format from the user and then returns the angle back'''
def setangle(e2):
    global angle
    if askyesno(title='set angle',message='Are you sure you want to set angle to this value'):
        angle=e2.get()
        angle=float(angle)
        if int(angle)<0 or int(angle)>90:
            showinfo(title='ERROR',message='please enter the angle value between 0 and 90 degrees')
    return (angle)
''' the function creates a window with background and entery widgets to recieve the values. it also has the buttons to set these values to the variables.
the function also has the simulation button on the window which when clicked after entering the other values runs the simulation'''
def projectile_interface():
    global xcoordinate
    global ycoordinate
    xcoordinate=[]
    ycoordinate=[]
    # window and canvas
    window1=Toplevel()
    window1.title('Projectile Motion')
    window1.geometry('830x495')
    

    background= ImageTk.PhotoImage(Image.open("projectile_background.jpg"))
    background_label = Label(window1, image=background)
    background_label.pack()
    background_label.place(x=0,y=0)
    #entry widgets
    e1=Entry(window1,bg='red')
    e1.pack()
    e1.place(x=200,y=210)
    e2=Entry(window1,bg='red')
    e2.pack()
    e2.place(x=200,y=260)
    #buttons
    button1=Button(window1,text='set initial velocity in m/s',bg='light green',command=lambda x=e1:setvelocity(x))
    button1.pack()
    button1.place(x=340,y=210)


    button2=Button(window1,text='set initial angle in degrees',bg='light green',command=lambda x=e2:setangle(x))
    button2.pack()
    button2.place(x=340,y=260)

    button3=Button(window1,text='projectile trajectory',bg='light green',command=projectile)
    button3.pack()
    button3.place(x=250,y=300)
    window1.mainloop()

''' the entire file is linked to the project file because the project file has the main interface'''
