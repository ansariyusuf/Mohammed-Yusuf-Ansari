# modules for use
from Tkinter import *
from tkMessageBox import *
from PIL import ImageTk, Image
import random
from math import *
'''the function is responsible for getting the focal length in the correct format from the user and then returns the focal length back'''
def setfocalLength(e1):
    global focal
    if askyesno(title='set focal',message='Are you sure you want to set focal length to this value'):
        focal=e1.get()
        focal=float(focal)
        if focal>0:             #focal length is negative according to the optic convention in the case of concave mirror
            focal=(-1.0)*(focal)
        if abs(focal)>100:
            showinfo(title='ERROR',message='please enter the angle value between 0 and 100 cm')
    return (focal)
'''the function is responsible for getting the object distance in the correct format from the user and then returns the object distance back'''
def setobjDistance(e2):
    global objD
    if askyesno(title='set objDistance',message='Are you sure you want to set obj distance to this value '):
        objD=e2.get()
        objD=float(objD)
        if objD>0.0:
            showinfo(title='ERROR',message='please enter a negative value of obj distance ') #object distance is negative according to the optic convention in the case of concave mirror
        if objD<-65:
            showinfo(title='ERROR',message='please enter a value of obj distance greater than -65 cm')
        
    return (objD)
'''the function is responsible for getting the object height in the correct format from the user and then returns the object height back'''
def setobjHeight(e3):
    global objH
    if askyesno(title='set objHeight',message='Are you sure you want to set obj Height to this value '):
        objH=e3.get()
        objH=float(objH)
        if objH<0.0:
            showinfo(title='ERROR',message='please enter a positive value of obj Height ')
        if objH>15:
            showinfo(title='ERROR',message='please enter a value of obj Height less than 15 cm')    
    return (objH)
'''this function is the most important function of this program. it takes the object distance, focal length, object height in terms of global variable and then uses the
mirror formula to generate the image distance, magnification and image height the function also creates the window and a canvas to shoe the object and the image with their corresponding
heights. the canvas imports the background of a concave mirror and places the the points of focus, center of curvature . the function draws the object and the image using the
object distance, image distance and magnification. it further marks the points of image and the object to differentiate them from each other. the function also has many text labels
to display object height, image height, nature of the image and magnifiaction on the screen. '''
def L_Mag():
    global focal
    global objD
    global objH
    global imgD
    window3=Toplevel()    #window and canvas for the simulation
    window3.title('Linear Magnification by concave mirror')
    window3.geometry('1200x700')

    background1= ImageTk.PhotoImage(Image.open("green background.png"))
    background_label1 = Label(window3, image=background1)
    background_label1.pack()
    background_label1.place(x=0,y=0)

    
    background= ImageTk.PhotoImage(Image.open("concave mirror.png"))
    canvas1=Canvas(window3,bg='white',width=800,height=600)
    canvas1.create_image(650,300,image=background)
    canvas1.pack()
    canvas1.place(x=100,y=0)
    canvas1.create_text(650+(focal*5), 290, text='F')
    canvas1.create_oval(650+(focal*5)-3, 297, 650+(focal*5)+3,303,fill='black')
    
    canvas1.create_line(0,300,800,300)
    canvas1.create_text(650+(2*focal*5), 290, text='C')
    canvas1.create_oval(650+(2*focal*5)-3, 297, 650+(2*focal*5)+3,303,fill='black')
    
    u=objD
    f=focal
    h=objH
    if u!=f:
        v=(f*u)/(u-f)# mirror formula
    else:
        v=-100000
    mag=(-1.0)*(v/u)
    himg=abs(mag)*h
    canvas1.create_rectangle(645+(u*5), 300-(h*5), 650+(u*5), 300, fill="blue")
    canvas1.create_oval(650+(u*5)-5, 297, 650+(u*5)+3,303,fill='black')
    canvas1.create_text(650+(u*5)-2, 310, text='O')
    if v<-130:                                                                   # if the image is outside the canvas boundary it gives you a notification
        showinfo(title='ERROR',message='image out of canvas boundary')
    if v>30:
        showinfo(title='ERROR',message='image out of canvas boundary')
    else:    
        if mag<0:
            canvas1.create_rectangle(645+(v*5), 300, 650+(v*5), 300+(himg*5), fill="blue")   # depending on magnification draw the image
            canvas1.create_oval(650+(v*5)-5, 297, 650+(v*5)+3,303,fill='black')
            canvas1.create_text(650+(v*5)-2, 290, text='I')
        else:
            canvas1.create_rectangle(645+(v*5), 300-(himg*5), 650+(v*5), 300, fill="blue")
            canvas1.create_oval(650+(v*5)-5, 297, 650+(v*5)+3,303,fill='black')
            canvas1.create_text(650+(v*5)-2, 310, text='I')
    if v>0:
        state='virtual'
    else:
        state='real'     # decide the state of the image
    if abs(mag)>1:
        nature='magnified'
    else:
        nature='diminished'
    text_label1=Label(window3,text='Focal Length: '+str(f)+'cm',relief=RAISED,font=("Helvetica", 16),bg='light green')     # text labels as information to the user
    text_label1.pack()
    text_label1.place(x=920,y=100)
    text_label2=Label(window3,text='Object distance: '+str(u)+'cm',relief=RAISED,font=("Helvetica", 16),bg='light green')
    text_label2.pack()
    text_label2.place(x=920,y=200)
    text_label3=Label(window3,text='Image Disatnce: '+str(round(v,2))+'cm',relief=RAISED,font=("Helvetica", 16),bg='light green')
    text_label3.pack()
    text_label3.place(x=920,y=300)
    text_label4=Label(window3,text='Hieght of object: '+str(round(h,2))+'cm',relief=RAISED,font=("Helvetica", 16),bg='light green')
    text_label4.pack()
    text_label4.place(x=920,y=400)
    text_label5=Label(window3,text='Hieght of Image: '+str(round(himg,2))+'cm',relief=RAISED,font=("Helvetica", 16),bg='light green')
    text_label5.pack()
    text_label5.place(x=920,y=500)
    text_label6=Label(window3,text='Magnification: '+str(round(mag,2)),relief=RAISED,font=("Helvetica", 16),bg='light green')
    text_label6.pack()
    text_label6.place(x=920,y=600)
    text_label7=Label(window3,text='The Image is '+state+' and '+nature,relief=RAISED,font=("Helvetica", 16),bg='light green')
    text_label7.pack()
    text_label7.place(x=870,y=650)
    window3.mainloop()

''' the function creates a window with background and entery widgets to recieve the values. it also has the buttons to set these values to the variables.
the function also has the simulation button on the window which when clicked after entering the other values runs the simulation'''
def Linear_Magnification():
    global e1
    global e2
    global e3
    window2=Toplevel()
    window2.title('Linear Magnification')
    window2.geometry('830x546')

    background1= ImageTk.PhotoImage(Image.open("l magnification.gif"))
    background_label1 = Label(window2, image=background1)
    background_label1.pack()
    background_label1.place(x=0,y=0)
    
    e1=Entry(window2,bg='red')
    e1.pack()
    e1.place(x=200,y=210)
    e2=Entry(window2,bg='red')
    e2.pack()
    e2.place(x=200,y=260)
    e3=Entry(window2,bg='red')
    e3.pack()
    e3.place(x=200,y=310)

    button3=Button(window2,text=' set focal length in cm',bg='light green',command=lambda x=e1:setfocalLength(x))
    button3.pack()
    button3.place(x=340,y=210)


    button4=Button(window2,text='set object distance in cm',bg='light green',command=lambda x=e2:setobjDistance(x))
    button4.pack()
    button4.place(x=340,y=260)
    
    button5=Button(window2,text='set object height in cm',bg='light green',command=lambda x=e3:setobjHeight(x))
    button5.pack()
    button5.place(x=340,y=310)
    
    button6=Button(window2,text='Magnification by a concave mirror',bg='light green',command=L_Mag)
    button6.pack()
    button6.place(x=300,y=360)
    window2.mainloop()

''' the entire file is linked to the project file because the project file has the main interface'''
