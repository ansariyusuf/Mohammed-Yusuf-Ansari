from Tkinter import *
from math import *
from tkMessageBox import *
from PIL import ImageTk, Image
import random
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

index=0
'''the function is responsible for getting the velocity in the correct format from the user and then returns the velocity back'''
def setvelocity(e1):
    global velocity
    if askyesno(title='set velocity',message='Are you sure you want to set velocity to this value'):
        velocity=e1.get()
        velocity=float(velocity)
        if velocity<0.0:
            showinfo(title='ERROR',message='please enter a positive velocity')
    return (velocity)

'''the function is responsible for getting the length of the stick in the correct format from the user and then returns the length back'''
def setlength(e2):
    global length
    if askyesno(title='set length',message='Are you sure you want to set legth of the string to this value'):
        length=e2.get()
        length=float(length)
        if int(length)<0 or int(length)>2.40:
            showinfo(title='ERROR',message='please enter the length value between 0 and 2 meters')
    return (length)
''' the function displays a text label saying that velocity is less than (2*g*l)^0.5 so the ball does not cross the horizontal line'''
def data():
    global velocity
    global length 
    text_label1=Label(window2,text='initial velocity is less than (2*g*l)^0.5 so the ball does not cross the horizontal line',relief=RAISED,font=("Helvetica", 16),bg='light green')
    text_label1.pack()
    text_label1.place(x=30,y=600)
''' the function displays a text label saying that initial velocity is less than (5*g*l)^0.5 and greater than (2*g*l)^0.5 so the ball crosses
the horizontal line but does not complete the circle'''
def data1():
    global velocity
    global length 
    text_label1=Label(window2,text='initial velocity is less than (5*g*l)^0.5 and greater than (2*g*l)^0.5 so the\n ball crosses the horizontal line but does not complete the circle',relief=RAISED,font=("Helvetica", 16),bg='light green')
    text_label1.pack()
    text_label1.place(x=30,y=600)
''' the function displays a text label saying that velocity is greater than (5*g*l)^0.5 so the ball completes the circle'''
def data2():
    global velocity
    global length 
    text_label1=Label(window2,text='initial velocity is greater than (5*g*l)^0.5 so the ball completes the circle',relief=RAISED,font=("Helvetica", 16),bg='light green')
    text_label1.pack()
    text_label1.place(x=30,y=600)
''' this function is the most important function of this program. it creates a window with a canvas to display the simulation. the function divides the
motion in a verticle into three cases. the fist case is when the velocity is not sufficient enough to cross the horizontal line. the second case is the
one in which the velocity is enough to cross the horizontal line but not enough to complete the circle.the third case is the one in which velocity is
enough to complete the circle. for each case we calculate the height to which the ball will reach and use this value generate ycoordinate list
which comprise of values separated by 0.1. now these values are placed in the circle equation to get the xcod and these xcod values are then placed into the
xcoordinate list. the lists are then passed into the animate function to run the simulation.'''
def motion():
    global xcoordinate
    global ycoordinate
    global velocity
    global length
    global canvas1
    global window2
    global background
    global index
    global ball
    global le
    index=0
    xcoordinate=[]
    ycoordinate=[]
    ball=Circle(250,250)
    window2=Toplevel()                  #it creates a window with a canvas to display the simulation
    window2.title('Motion in Verticle circle')
    window2.geometry('700x700')

    background1= ImageTk.PhotoImage(Image.open("green background.png"))
    background_label1 = Label(window2, image=background1)
    background_label1.pack()
    background_label1.place(x=0,y=0)
    
    background= ImageTk.PhotoImage(Image.open("verticle background.jpg"))
    canvas1=Canvas(window2,bg='light green',width=500,height=500)
    canvas1.create_image(250,250,image=background)
    canvas1.pack()
    canvas1.place(x=100,y=0)
    canvas1.create_line(0,250,500,250)
    canvas1.create_line(250,0,250,500)
    if velocity<=((2*9.8*length)**0.5):
        data()    
        length=length*100    
        i=250+length
        height=((velocity*velocity)/(2*9.8))*100
        count=0
        while i>(250+length-height):            #for each case we calculate the height to which the ball will reach and use this value generate ycoordinate list
                                                #which comprise of values separated by 0.1.
            ycoordinate.append(round(i,2))
            if count<30:
                    i=i-0.005
                    count+=1
            else:
                    i=i-0.1
                    count+=1
                    
        for i in range(len(ycoordinate)):
            y=ycoordinate[i]
            x=250+((length*length)-((y-250)**2))**0.5           #now these values are placed in the circle equation to get the xcod and these xcod values are then placed into the
                                                                #xcoordinate list.
            xcoordinate.append(round(x,2))
        l=[]    
        for i in range(len(xcoordinate)):
            l=[xcoordinate[i]]+l
        xcoordinate=xcoordinate+l    
        l=[]
        for i in range(len(ycoordinate)):
            l=[ycoordinate[i]]+l
        ycoordinate=ycoordinate+l
        l=[]
        for i in range(len(ycoordinate)):
            l=[ycoordinate[i]]+l
        ycoordinate=ycoordinate+l
        l=[]
        for i in range(len(xcoordinate)):
            x=((xcoordinate[i]-250)*(-1)+250)
            l.append(x)
        xcoordinate=xcoordinate+l
    if velocity>=((5*9.8*length)**0.5):
        data2()    
        length=length*100    #for each case we calculate the height to which the ball will reach and use this value generate ycoordinate list
                             #which comprise of values separated by 0.1.
        i=250+(length)
        count=0
        while i>=(250):
            ycoordinate.append(round(i,2))
            if count<30:
                    i=i-0.005
                    count+=1
            else:
                    i=i-0.1
                    count+=1
        for i in range(len(ycoordinate)):              #now these values are placed in the circle equation to get the xcod and these xcod values are then placed into the
                                                       #xcoordinate list.
            y=ycoordinate[i]
            x=250+((length*length)-((y-250)**2))**0.5
        
            xcoordinate.append(round(x,2))
        l=[]
        for i in range(len(ycoordinate)):
                y=ycoordinate[i]-(2*(ycoordinate[i]-250))
                l=[y]+l
        ycoordinate=ycoordinate+l        
        l=[]    
        for i in range(len(xcoordinate)):
            l=[xcoordinate[i]]+l
        xcoordinate=xcoordinate+l
        l=[]
        for i in range(len(ycoordinate)):
                y=ycoordinate[i]
                l=[y]+l
        ycoordinate=ycoordinate+l        
        l=[]
        for i in range(len(xcoordinate)):
            x=((xcoordinate[i]-250)*(-1)+250)
            l.append(x)
        xcoordinate=xcoordinate+l
    if ((2*9.8*length)**0.5)<velocity<((5*9.8*length)**0.5):
        data1()    
        length=length*100    
        i=250+length
        height=((velocity*velocity)/(2*9.8))*100
        count=0
        while i>(250+length-height):            #for each case we calculate the height to which the ball will reach and use this value generate ycoordinate list
                                                #which comprise of values separated by 0.1.
            ycoordinate.append(round(i,2))
            if count<30:
                    i=i-0.005
                    count+=1
            else:
                    i=i-0.1
                    count+=1
                    
        for i in range(len(ycoordinate)):         #now these values are placed in the circle equation to get the xcod and these xcod values are then placed into the
                                                  #xcoordinate list.
            y=ycoordinate[i]
            x=250+((length*length)-((y-250)**2))**0.5
            xcoordinate.append(round(x,2))
        l=[]    
        for i in range(len(xcoordinate)):
            l=[xcoordinate[i]]+l
        xcoordinate=xcoordinate+l    
        l=[]
        for i in range(len(ycoordinate)):
            l=[ycoordinate[i]]+l
        ycoordinate=ycoordinate+l
        l=[]
        for i in range(len(ycoordinate)):
            l=[ycoordinate[i]]+l
        ycoordinate=ycoordinate+l
        l=[]
        for i in range(len(xcoordinate)):
            x=((xcoordinate[i]-250)*(-1)+250)
            l.append(x)
        xcoordinate=xcoordinate+l
    canvas1.after(2000,animate)    #animate function to run the simulation.
    length=((length*(1.0))/100)
    le=length
    window2.mainloop()

''' the animate function is responsible for showing the simulation on the canvas. the function takes the xcoordiante and ycoordinate list along
with the index variable as globals. the function moves through the xcoordinate and ycoordinate list simulatneoulsy and moves the ball to the right
coordinate as per the list. while the index value is less than the length of the list the process is repeated. this process is repeated every 10 milli second
which gives us a visual effect of the  motion in a verticle circle. once the index reaches the end of the list then the animate function generates the trajectory path
by joining the coordinates present in the xcoordinate and the ycoordinate list.'''
def animate():
    global canvas1
    global xcoordinate
    global ycoordinate
    global ball
    global index
    global window2
    global background
    global length
    global le
    canvas1=Canvas(window2,bg='light green',width=500,height=500)
    canvas1.create_image(250,250,image=background)
    canvas1.pack()
    canvas1.place(x=100,y=0)
    canvas1.create_line(0,250,500,250)
    canvas1.create_line(250,0,250,500)
    if velocity<=((2*9.8*le)**0.5) or ((2*9.8*le)**0.5)<velocity<((5*9.8*le)**0.5):
            if len(xcoordinate)>80:
                    if index<len(xcoordinate):
                        if index>len(xcoordinate)/4:
                            ball.move(xcoordinate[index],ycoordinate[index])                    # the function takes the xcoordiante and ycoordinate list along
                                                                                                #with the index variable as globals. the function moves through the xcoordinate
                                                                                                # and ycoordinate list simulatneoulsy and moves the ball to the right
                                                                                                #coordinate as per the list.
                            canvas1.create_line(250,250,xcoordinate[index],ycoordinate[index])
                            ball.draw(canvas1)
                            index+=16    # incrementing index
                        else:
                            ball.move(xcoordinate[index],ycoordinate[index])
                            canvas1.create_line(250,250,xcoordinate[index],ycoordinate[index])
                            ball.draw(canvas1)
                            index+=13     # incrementing index
                        canvas1.after(10,animate)
                        if index>len(xcoordinate)-20:
                            index=0
                            for i in range(len(ycoordinate)-2):
                                    canvas1.create_line(xcoordinate[i],ycoordinate[i],xcoordinate[i+1],ycoordinate[i+1])
                   
            else:
                    if index<len(xcoordinate):
                        if index>len(xcoordinate)/4:
                            ball.move(xcoordinate[index],ycoordinate[index])                    # the function takes the xcoordiante and ycoordinate list along
                                                                                                #with the index variable as globals. the function moves through the xcoordinate
                                                                                                # and ycoordinate list simulatneoulsy and moves the ball to the right
                                                                                                #coordinate as per the list.
                            canvas1.create_line(250,250,xcoordinate[index],ycoordinate[index])
                            ball.draw(canvas1)
                            index+=8     # incrementing index
                        else:
                            ball.move(xcoordinate[index],ycoordinate[index])
                            canvas1.create_line(250,250,xcoordinate[index],ycoordinate[index])
                            ball.draw(canvas1)
                            index+=5      # incrementing index
                        canvas1.after(10,animate)
                        if index>len(xcoordinate)-20:
                            index=0
                            for i in range(len(ycoordinate)-2):
                                    canvas1.create_line(xcoordinate[i],ycoordinate[i],xcoordinate[i+1],ycoordinate[i+1])
                    
    if velocity>=((5*9.8*le)**0.5):
            if 220<xcoordinate[index]<280:
                    if index<len(xcoordinate):
                            ball.move(xcoordinate[index],ycoordinate[index])
                            canvas1.create_line(250,250,xcoordinate[index],ycoordinate[index])  # the function takes the xcoordiante and ycoordinate list along
                                                                                                #with the index variable as globals. the function moves through the xcoordinate
                                                                                                # and ycoordinate list simulatneoulsy and moves the ball to the right
                                                                                                #coordinate as per the list.
                            ball.draw(canvas1)
                            index+=10     # incrementing index
                        
                            canvas1.after(10,animate)
                            if index>len(xcoordinate)-20:
                                    index=0
                    else:
                        for i in range(len(ycoordinate)-2):
                            canvas1.create_line(xcoordinate[i],ycoordinate[i],xcoordinate[i+1],ycoordinate[i+1])
                    
            else:
                    if index<len(xcoordinate):
                            ball.move(xcoordinate[index],ycoordinate[index])
                            canvas1.create_line(250,250,xcoordinate[index],ycoordinate[index])  # the function takes the xcoordiante and ycoordinate list along
                                                                                                #with the index variable as globals. the function moves through the xcoordinate
                                                                                                # and ycoordinate list simulatneoulsy and moves the ball to the right
                                                                                                #coordinate as per the list.
                            ball.draw(canvas1)
                            index+=20     # incrementing index
                            canvas1.after(10,animate)
                            if index>len(xcoordinate)-20:
                                    index=0
                    else:    
                        for i in range(len(ycoordinate)-2):
                            canvas1.create_line(xcoordinate[i],ycoordinate[i],xcoordinate[i+1],ycoordinate[i+1])
                    
''' the function creates a window with background and entery widgets to recieve the values. it also has the buttons to set these values to the variables.
the function also has the simulation button on the window which when clicked after entering the other values runs the simulation'''            
def verticle_circle_interface():
    global xcoordinate
    global ycoordinate
    xcoordinate=[]
    ycoordinate=[]
    # window and canvas
    window1=Toplevel()
    window1.title('Motion in verticle circle')
    window1.geometry('830x495')
    

    background= ImageTk.PhotoImage(Image.open("background.jpg"))
    background_label = Label(window1, image=background)
    background_label.pack()
    background_label.place(x=0,y=0)

    background_image = ImageTk.PhotoImage(Image.open("verticlecircle heading.gif"))
    image_label = Label(window1, image=background_image)
    image_label.pack()
    image_label.place(x=200,y=70)
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


    button2=Button(window1,text='set length of the stick in m',bg='light green',command=lambda x=e2:setlength(x))
    button2.pack()
    button2.place(x=340,y=260)

    button3=Button(window1,text='motion in vertical circle',bg='light green',command=motion)
    button3.pack()
    button3.place(x=250,y=300)
    window1.mainloop()

''' the entire file is linked to the project file because the project file has the main interface'''
