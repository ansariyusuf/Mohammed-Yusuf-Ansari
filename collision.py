from Tkinter import *
from tkMessageBox import *
from PIL import ImageTk, Image
import random
from math import *
#http://vlab.amrita.edu/?sub=1&brch=74&sim=189&cnt=1
''' the class circle creates a circle object of a given radius on a particular coordinate of the canvas.
the class has functions such as move and draw which are resposible for changing the circle's coordinate and redrawing the circle
at the new ocation. the reset function set the x coordinate and the y coordinate to (0,0)''' 
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
'''the function has list of facts about momentum and collision. it selects on of the facts randomly and displays it on the window
as text label'''
def facts():
    global text_label3
    l=['A change in momentum\n is called impulse','An elastic collision\n is one in which\n no kinetic energy\n is lost',
           'An inelastic collision\n is one in which\n some of the kinetic\n energy of the colliding\n bodies is lost.\nThis is because \nthe energy is converted\n into another type\n of energy like\n heat or sound',
           'The recoil of a\n gun is because of\n the conservation of\n momentum. The gun\n moves back at a\n lower velocity than the\n bullet because of\n its greater mass']
    text_label3=Label(window4,text='Facts on Momentum & Collision\n'+random.choice(l),relief=RAISED,font=("Helvetica", 16),bg='light green',width=25)
    text_label3.pack()
    text_label3.place(x=910,y=50)
'''the function takes in the initial veocities of the two balls and their final velocities. it then finds the difference in initial
and the final Kinetic energy of the two balls and displays it as a label on the window as a text label''' 
def kinetic_energy():
    global velocity1
    global velocity2
    global window4
    global velocity1_final
    global velocity2_final
    global mass1
    global mass2
    loss_of_KE=0.5*(mass1*velocity1*velocity1+mass2*velocity2*velocity2)-0.5*(mass1*velocity1_final*velocity1_final+mass2*velocity2_final*velocity2_final)
    text_label2=Label(window4,text='Loss of Kinetic Energy: '+str(round(loss_of_KE,2))+'J',relief=RAISED,font=("Helvetica", 16),bg='light green')
    text_label2.pack()
    text_label2.place(x=920,y=450)

'''the function takes the velocities of the ball1 and ball2 as input and displays their velocities on the screen. the function also
displays their final velocities after the collision takes place. the function does this by creating a text label on the window'''
def data(vx,vy):
    global velocity1
    global velocity2
    global window4
    global velocity1_final
    global velocity2_final
    text_label1=Label(window4,text='Velocity of ball 1: '+str(round(vx,2))+'m/s'+' \nVelocity of ball 2: '+str(round(vy,2))+'m/s',relief=RAISED,font=("Helvetica", 16),bg='light green')
    text_label1.pack()
    text_label1.place(x=920,y=350)
'''this function has the most important role toplay in this program.it takes the initial velocities of the balls and the coefficient of restitution
in the form of global variables and then generates the final velocities considering the three values. the function creates window with a canvas
which will be later used to show the simulations. the function calls the above defined functions to show text labels and the animate function to show the simulation'''
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
    global window4
    global count
    count=0
    ball1=Circle(0,600)
    ball2=Circle(800,600)
    if res==1:
        velocity1_final=(((mass1-mass2)/(mass1+mass2))*velocity1)+(((2*mass2)/(mass1+mass2))*velocity2)     #elastic collison
        velocity2_final=(((mass2-mass1)/(mass1+mass2))*velocity2)+(((2*mass1)/(mass1+mass2))*velocity1)
    elif res==0:
        velocity1_final=((mass1*velocity1)+(mass2*velocity2))/(mass1+mass2)    #inelastic collision
        velocity2_final=velocity1_final
    else:
        velocity1_final=(velocity1*(mass1-(mass2*res))/(mass1+mass2))+((velocity2*mass2*(1+res))/(mass1+mass2))    #collison with e between 0 and 1
    window4=Toplevel()   # window and canvas for the simlation
    window4.title('collision')
    window4.geometry('1220x700')

    background1= ImageTk.PhotoImage(Image.open("green background.png"))
    background_label1 = Label(window4, image=background1)
    background_label1.pack()
    background_label1.place(x=0,y=0)
    
    background= ImageTk.PhotoImage(Image.open("collision background.jpg"))
    canvas2=Canvas(window4,bg='light green',width=800,height=600)
    canvas2.create_image(400,300,image=background)
    canvas2.pack()
    canvas2.place(x=100,y=0)
    data(velocity1,velocity2)  # labels for the information
    facts()
    canvas2.after(2000,animate) # calling animate for the simulation
    window4.mainloop()
    
count=0
''' the animate function is responsible for showing the simulation on the canvas.it uses the velocities of the balls to calculate the
coordinates where the balls would collide. every time the function executes the balls are moved by their respective initial velocities.
once the balls reach the coordinate for the collision then the balls are moved with respect to their final velocities. this process is
repeated every 0.1 s'''
def animate():
    global text_label3
    global canvas2
    global ball1
    global ball2
    global velocity1
    global velocity2
    global velocity1_final
    global velocity2_final
    global count
    global time
    
    time=800/(abs(velocity1)+abs(velocity2))    #it uses the velocities of the balls to calculate the
                                                #coordinates where the balls would collide
    ball1.move(ball1.x,500)
    ball1.draw(canvas2)
    if ball1.x<(abs(velocity1)*time)-20 and count==0:
        ball1.x=ball1.x+(velocity1/3)
    else:
        if count==0:
                #once the balls reach the coordinate for the collision then the balls are moved with respect to their final velocities
                data(velocity1_final,velocity2_final)
                kinetic_energy()   # display kinetic energy loss
        ball1.x=ball1.x+(velocity1_final/3)
        count=1
    ball2.move(ball2.x,500)
    ball2.draw(canvas2)
    if ball2.x>810-(abs(velocity2)*time) and count==0:
       ball2.x=ball2.x+((velocity2)/3)
    else:
        #once the balls reach the coordinate for the collision then the balls are moved with respect to their final velocities
        ball2.x=ball2.x+((velocity2_final)/3)
        count=1
    canvas2.after(100,animate)
'''the function is responsible for getting the velocity in the correct format from the user and then returns the velocity back'''
def setvelocity1(e1):
    global velocity1
    if askyesno(title='set velocity',message='Are you sure you want to set velocity to this value'):
        velocity1=e1.get()
        velocity1=float(velocity1)
        velocity1=abs(velocty1)
    if velocity1:
        return (velocity1)
'''the function is responsible for getting the velocity in the correct format from the user and then returns the velocity back'''
def setvelocity2(e2):
    global velocity2
    if askyesno(title='set velocity',message='Are you sure you want to set velocity to this value'):
        velocity2=e2.get()
        velocity2=float(velocity2)
        if velocity2>0:
                velocity2=(-1.0)*velocity2
    if velocity2:
        return (velocity2)
'''the function is responsible for getting the mass in the correct format from the user and then returns the mass back'''
def setmass1(e3):
    global mass1
    if askyesno(title='set mass',message='Are you sure you want to set mass of ball 1 to this value'):
        mass1=e3.get()
        mass1=float(mass1)
        if mass1<0.0:
            showinfo(title='ERROR',message='please enter a non negative mass')
    if mass1:
        return (mass1)
'''the function is responsible for getting the mass in the correct format from the user and then returns the mass back'''
def setmass2(e4):
    global mass2
    if askyesno(title='set mass',message='Are you sure you want to set mass of ball 2 to this value'):
        mass2=e4.get()
        mass2=float(mass2)
        if mass2<0.0:
            showinfo(title='ERROR',message='please enter a non negative mass')
    if mass2:
        return (mass2)
'''the function is responsible for getting the coefficient of restitution in the correct format from the user and then returns the coefficient of restitution back'''
def restitution(e5):
    global res
    if askyesno(title='set cefficient of restitution',message='Are you sure you want to set coefficientof restitution to this value'):
        res=e5.get()
        res=float(res)
        if res<0.0 or res>1.0:
            showinfo(title='ERROR',message='please enter a value between 0 and 1')
    if res:
        return (res)    
''' the function creates a window with background and entery widgets to recieve the values. it also has the buttons to set these values to the variables.
the function also has the simulation button on the window which when clicked after entering the other values runs the simulation'''
def collision_interface():
    # window and canvas
    window3=Toplevel()
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
    #entry widgets
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
    #buttons
    button1=Button(window3,text='velocity of ball 1 in m/s',bg='light green',command=lambda x=e1:setvelocity1(x))
    button1.pack()
    button1.place(x=550,y=110)


    button2=Button(window3,text='velocity of ball 2 in m/s',bg='light green',command=lambda x=e2:setvelocity2(x))
    button2.pack()
    button2.place(x=550,y=150)

    button3=Button(window3,text='mass of ball 1 in kg',bg='light green',command=lambda x=e3:setmass1(x))
    button3.pack()
    button3.place(x=550,y=200)
    
    button4=Button(window3,text='mass of ball 2 in kg',bg='light green',command=lambda x=e4:setmass2(x))
    button4.pack()
    button4.place(x=550,y=250)
    
    button6=Button(window3,text='coefficient of restitution',bg='light green',command=lambda x=e5:restitution(x))
    button6.pack()
    button6.place(x=550,y=70)

    button5=Button(window3,text='collision simulation',bg='light green',command=collision)
    button5.pack()
    button5.place(x=470,y=300)

    window3.mainloop()

''' the entire file is linked to the project file because the project file has the main interface'''
