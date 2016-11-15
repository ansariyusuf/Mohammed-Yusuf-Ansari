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
ball=Circle(0,0)
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
    if int(velocity)<0:
        showinfo(title='ERROR',message='please enter a positive velocity')
        return
    if int(angle)<0 or int(angle)>90:
        showinfo(title='ERROR',message='please enter the angle value between 0 and 90 degrees')
        return
    window2=Toplevel()
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
    
    time_of_flight=(2*velocity*sin(radians(angle)))/9.8
    maximum_height=(velocity*sin(radians(angle)))**2/(2*9.8)
    range_of_projectile=((velocity**2)*sin(2*radians(angle)))/9.8

    i=0
    while i<=((range_of_projectile)):
        xcoordinate.append(round(i,2))
        i=i+0.1
        
    t=tan(radians(angle))
    c=cos(radians(angle))*cos(radians(angle))
    v=velocity*velocity
    
    for i in range(len(xcoordinate)):
        x=xcoordinate[i]
        y=550-(x*t-(9.8*(x*x))/(2*v*c))
        ycoordinate.append(round(y,2))
        
    canvas1.after(2000,animate)
    
    text_label2=Label(window2,text='Horizontal Range: '+str(round(range_of_projectile,2))+'m',relief=RAISED,font=("Helvetica", 16),bg='light green')
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
def animate():
    global canvas1
    global xcoordinate
    global ycoordinate
    global ball
    global index
    if index<len(xcoordinate):
        if index>len(xcoordinate)/4:
            ball.move(xcoordinate[index],ycoordinate[index])
            ball.draw(canvas1)
            index+=18
        else:
            ball.move(xcoordinate[index],ycoordinate[index])
            ball.draw(canvas1)
            index+=15
        canvas1.after(1,animate)
    else:
        for i in range(len(ycoordinate)-2):
            canvas1.create_line(xcoordinate[i],ycoordinate[i],xcoordinate[i+1],ycoordinate[i+1])
def setvelocity(e1):
    global velocity
    if askyesno(title='set velocity',message='Are you sure you want to set velocity to this value'):
        velocity=e1.get()
        velocity=float(velocity)
        if velocity<0.0:
            showinfo(title='ERROR',message='please enter a positive velocity')
    return (velocity)
def setangle(e2):
    global angle
    if askyesno(title='set angle',message='Are you sure you want to set angle to this value'):
        angle=e2.get()
        angle=float(angle)
        if int(angle)<0 or int(angle)>90:
            showinfo(title='ERROR',message='please enter the angle value between 0 and 90 degrees')
    return (angle)

def projectile_interface():
    global xcoordinate
    global ycoordinate
    xcoordinate=[]
    ycoordinate=[]
    window1=Tk()
    window1.title('Projectile Motion')
    window1.geometry('830x495')
    

    background= ImageTk.PhotoImage(Image.open("projectile_background.jpg"))
    background_label = Label(window1, image=background)
    background_label.pack()
    background_label.place(x=0,y=0)

    e1=Entry(window1,bg='red')
    e1.pack()
    e1.place(x=200,y=210)
    e2=Entry(window1,bg='red')
    e2.pack()
    e2.place(x=200,y=260)
    
    button1=Button(window1,text='set initial velocity',bg='light green',command=lambda x=e1:setvelocity(x))
    button1.pack()
    button1.place(x=340,y=210)


    button2=Button(window1,text='set initial angle',bg='light green',command=lambda x=e2:setangle(x))
    button2.pack()
    button2.place(x=340,y=260)

    button3=Button(window1,text='projectile trajectory',bg='light green',command=projectile)
    button3.pack()
    button3.place(x=250,y=300)
    window1.mainloop()
projectile_interface()
