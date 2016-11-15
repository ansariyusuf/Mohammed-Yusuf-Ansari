# Code designed and written by: Mohammed Yusuf Ansari
# Andrew ID: ma1
# File Created: October 28, 12:45pm
# Modification History:
# Start              End

# 28/10 12:45pm  28/10 1:00pm
# 28/10 1:15pm   28/10 2:30pm
# 28/10 3:00pm   28/10 3:45pm
# 28/10 3:50pm   28/10 4:00pm
# 28/10 11:30pm  29/10 12:15am
# 29/10 5:30pm   29/10 6:00pm

from Tkinter import *
from tkMessageBox import *
from PIL import ImageTk, Image
import random
from math import *

'''we import Tkinter PIL and tkmessagebox to create a good GUI'''
# code for projectile
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
        for i in range(len(ycoordinate)-1):
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
    global ball
    global index
    global window1
    del ball
    index=0
    ball=Circle(0,0)
    xcoordinate=[]
    ycoordinate=[]
    window1=Toplevel()
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
#___________________________collision code_______________________________________
ball1=Circle(0,600)
ball2=Circle(800,600)
def collision():
    global res
    global velocity1
    global velocity2
    global mass1
    global mass2
    global ball1
    global ball2
    global canvas2
    global velocity1_final
    global velocity2_final
    if res==1:
        velocity1_final=(((mass1-mass2)/(mass1+mass2))*velocity1)+(((2*mass2)/(mass1+mass2))*velocity2)
        velocity2_final=(((mass1-mass2)/(mass1+mass2))*velocity2)+(((2*mass2)/(mass1+mass2))*velocity1)
    elif res==0:
        velocity1_final=((mass1*velocity1)+(mass2*velocity2))/(mass1+mass2)
        velocity2_final=velocity1_final
    else:
        velocity1_final=((velocity1*mass1*(1+res))/(mass1+mass2))+((velocity2*mass2*(1+res))/(mass1+mass2))
        velocity2_final=velocity1_final-(res*(velocity2-velocity1))
    print velocity1
    print velocity2
    print velocity1_final
    print velocity2_final
    window4=Toplevel()
    window4.title('collision')
    window4.geometry('1200x700')

    background1= ImageTk.PhotoImage(Image.open("green background.png"))
    background_label1 = Label(window4, image=background1)
    background_label1.pack()
    background_label1.place(x=0,y=0)
    
    background= ImageTk.PhotoImage(Image.open("collision background.jpg"))
    canvas2=Canvas(window4,bg='light green',width=800,height=600)
    canvas2.create_image(400,300,image=background)
    canvas2.pack()
    canvas2.place(x=100,y=0)
    
    canvas2.after(2000,animate)
    window4.mainloop()
    
count=0
def animate():
    global canvas2
    global ball1
    global ball2
    global velocity1
    global velocity2
    global velocity1_final
    global velocity2_final
    global count
    global time
    time=800/(abs(velocity1)+abs(velocity2))
    ball1.move(ball1.x,500)
    ball1.draw(canvas2)
    if ball1.x<(abs(velocity1)*time)-20 and count==0:
        ball1.x=ball1.x+(velocity1/3)
    else:
        ball1.x=ball1.x+(velocity1_final/3)
        count=1
    ball2.move(ball2.x,500)
    ball2.draw(canvas2)
    if ball2.x>810-(abs(velocity1)*time) and count==0:
       ball2.x=ball2.x+((velocity2)/3)
    else:
        ball2.x=ball2.x+((velocity2_final)/3)
        count=1
    canvas2.after(100,animate)    
def setvelocity1(e1):
    global velocity1
    if askyesno(title='set velocity',message='Are you sure you want to set velocity to this value'):
        velocity1=e1.get()
        velocity1=float(velocity1)
        if velocity1<0.0:
            showinfo(title='ERROR',message='please enter a non negative velocity')
    if velocity1:
        return (velocity1)
def setvelocity2(e2):
    global velocity2
    if askyesno(title='set velocity',message='Are you sure you want to set velocity to this value'):
        velocity2=e2.get()
        velocity2=float(velocity2)
    if velocity2<0.0:
            showinfo(title='ERROR',message='please enter a non negative velocity')    
    velocity2=velocity2*(-1)
    if velocity2:
        return (velocity2)
def setmass1(e3):
    global mass1
    if askyesno(title='set mass',message='Are you sure you want to set mass of ball 1 to this value'):
        mass1=e3.get()
        mass1=float(mass1)
        if mass1<0.0:
            showinfo(title='ERROR',message='please enter a non negative mass')
    if mass1:
        return (mass1)
def setmass2(e4):
    global mass2
    if askyesno(title='set mass',message='Are you sure you want to set mass of ball 2 to this value'):
        mass2=e4.get()
        mass2=float(mass2)
        if mass2<0.0:
            showinfo(title='ERROR',message='please enter a non negative mass')
    if mass2:
        return (mass2)
def restitution(e5):
    global res
    if askyesno(title='set cefficient of restitution',message='Are you sure you want to set coefficientof restitution to this value'):
        res=e5.get()
        res=float(res)
        if res<0.0 or res>1.0:
            showinfo(title='ERROR',message='please enter a value between 0 and 1')
    if res:
        return (res)    
    
def collision_interface():
    global ball1 
    global ball2
    del ball1
    del ball2
    ball1=Circle(0,600)
    ball2=Circle(800,600)
    window3=Tk()
    window3.title('Projectile Motion')
    window3.geometry('1100x412')
    

    background= ImageTk.PhotoImage(Image.open("collision_background1.jpg"))
    background_label = Label(window3, image=background)
    background_label.pack()
    background_label.place(x=0,y=0)
    background1= ImageTk.PhotoImage(Image.open("collision_background2.jpg"))
    background_label1 = Label(window3, image=background1)
    background_label1.pack()
    background_label1.place(x=550,y=0)

    e1=Entry(window3,bg='red')
    e1.pack()
    e1.place(x=400,y=110)
    e2=Entry(window3,bg='red')
    e2.pack()
    e2.place(x=400,y=150)
    e3=Entry(window3,bg='red')
    e3.pack()
    e3.place(x=400,y=200)
    e4=Entry(window3,bg='red')
    e4.pack()
    e4.place(x=400,y=250)
    e5=Entry(window3,bg='red')
    e5.pack()
    e5.place(x=400,y=70)
    
    button1=Button(window3,text='velocity of ball 1',bg='light green',command=lambda x=e1:setvelocity1(x))
    button1.pack()
    button1.place(x=550,y=110)


    button2=Button(window3,text='velocity of ball 2',bg='light green',command=lambda x=e2:setvelocity2(x))
    button2.pack()
    button2.place(x=550,y=150)

    button3=Button(window3,text='mass of ball 1',bg='light green',command=lambda x=e3:setmass1(x))
    button3.pack()
    button3.place(x=550,y=200)
    
    button4=Button(window3,text='mass of ball 2',bg='light green',command=lambda x=e4:setmass2(x))
    button4.pack()
    button4.place(x=550,y=250)
    
    button6=Button(window3,text='coefficient of restitution',bg='light green',command=lambda x=e5:restitution(x))
    button6.pack()
    button6.place(x=550,y=70)

    button5=Button(window3,text='collision simulation',bg='light green',command=collision)
    button5.pack()
    button5.place(x=470,y=300)

    window3.mainloop()
# main interface    
window=Tk()
window.title('physics Simulator')
window.geometry('1100x800')

background= ImageTk.PhotoImage(Image.open("background.jpg"))
background_label = Label(window, image=background)
background_label.pack()
background_label.place(x=0,y=0)

background1= ImageTk.PhotoImage(Image.open("physics.jpg"))
background_label1 = Label(window, image=background1)
background_label1.pack()
background_label1.place(x=100,y=0)

background2= ImageTk.PhotoImage(Image.open("projectile.jpg"))
background_label2 = Label(window, image=background2)
background_label2.pack()
background_label2.place(x=50,y=200)

background3= ImageTk.PhotoImage(Image.open("projectile2.jpg"))
background_label3 = Label(window, image=background3)
background_label3.pack()
background_label3.place(x=700,y=200)

background4= ImageTk.PhotoImage(Image.open("collison.gif"))
background_label4 = Label(window, image=background4)
background_label4.pack()
background_label4.place(x=700,y=400)

background7= ImageTk.PhotoImage(Image.open("collison2.gif"))
background_label7 = Label(window, image=background7)
background_label7.pack()
background_label7.place(x=100,y=400)

background5= ImageTk.PhotoImage(Image.open("convex lens.png"))
background_label5 = Label(window, image=background5)
background_label5.pack()
background_label5.place(x=700,y=600)

background6= ImageTk.PhotoImage(Image.open("motion in a verticle circle.png"))
background_label6 = Label(window, image=background6)
background_label6.pack()
background_label6.place(x=100,y=600)

background8= ImageTk.PhotoImage(Image.open("simulator.jpg"))
background_label8 = Label(window, image=background8)
background_label8.pack()
background_label8.place(x=510,y=0)

#buttons

button1=Button(window,text='Projectile Motion',background='yellow',relief=RAISED,width='15',height='3',font=("Brush Script Std", 16),activebackground='light green',command=projectile_interface)
button1.pack()
button1.place(x=410,y=250)


button2=Button(window,text='Collision',background='yellow',relief=RAISED,width='10',height='3',font=("Brush Script Std", 16),activebackground='light green')
button2.pack()
button2.place(x=440,y=380)


button3=Button(window,text='Image by a Convex Lens',background='yellow',relief=RAISED,width='18',height='4',font=("Brush Script Std", 16),activebackground='light green')
button3.pack()
button3.place(x=400,y=500)

button4=Button(window,text='Motion in a Verticle Circle',background='yellow',relief=RAISED,width='20',height='4',font=("Brush Script Std", 16),activebackground='light green')
button4.pack()
button4.place(x=390,y=650)

window.mainloop()
