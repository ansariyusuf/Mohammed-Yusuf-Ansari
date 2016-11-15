from Tkinter import *
from tkMessageBox import *
from PIL import ImageTk, Image
import random
from math import *
#http://vlab.amrita.edu/?sub=1&brch=74&sim=189&cnt=1
class Circle:
        colors = ["red","blue","green","yellow","orange","purple","black","pink","white","cyan"]
        def __init__(self,x,y):
            self.r = 20
            self.color = random.choice(Circle.colors)
            self.x = x
            self.y = y
            self.me = None
        def move(self,xoffset,yoffset):
            self.x = xoffset
            self.y = yoffset
        def reset(self):
            self.x=0
            self.y=0
        def draw(self,c):
            if self.me != None:
                c.delete(self.me)
            self.me = c.create_oval(self.x,self.y,self.x+(self.r*2),self.y+(self.r*2),fill=self.color)
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

collision_interface()
