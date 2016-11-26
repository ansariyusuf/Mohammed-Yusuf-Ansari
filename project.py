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
import projectile
import collision
import verticleCircle
import magnification

'''we import Tkinter PIL and tkmessagebox to create a good GUI'''

# main interface    
window=Tk() # main interface window
window.title('physics Simulator')
window.geometry('1100x800')

background= ImageTk.PhotoImage(Image.open("background.jpg"))  #background image for the window
background_label = Label(window, image=background)
background_label.pack()
background_label.place(x=0,y=0)

background1= ImageTk.PhotoImage(Image.open("physics.jpg"))     #background image for the window
background_label1 = Label(window, image=background1)
background_label1.pack()
background_label1.place(x=100,y=0)

background2= ImageTk.PhotoImage(Image.open("projectile.jpg"))     #background image for the window
background_label2 = Label(window, image=background2)
background_label2.pack()
background_label2.place(x=50,y=200)

background3= ImageTk.PhotoImage(Image.open("projectile2.jpg"))     #background image for the window
background_label3 = Label(window, image=background3)
background_label3.pack()
background_label3.place(x=700,y=200)

background4= ImageTk.PhotoImage(Image.open("collison.gif"))      #background image for the window
background_label4 = Label(window, image=background4)
background_label4.pack()
background_label4.place(x=700,y=400)

background7= ImageTk.PhotoImage(Image.open("collison2.gif"))       #background image for the window
background_label7 = Label(window, image=background7)
background_label7.pack()
background_label7.place(x=100,y=400)

background5= ImageTk.PhotoImage(Image.open("concave background.png"))    #background image for the window
background_label5 = Label(window, image=background5)
background_label5.pack()
background_label5.place(x=700,y=600)

background6= ImageTk.PhotoImage(Image.open("motion in a verticle circle.png"))    #background image for the window
background_label6 = Label(window, image=background6)
background_label6.pack()
background_label6.place(x=100,y=600)

background8= ImageTk.PhotoImage(Image.open("simulator.jpg"))      #background image for the window
background_label8 = Label(window, image=background8)
background_label8.pack()
background_label8.place(x=510,y=0)

#buttons

button1=Button(window,text='Projectile Motion',background='yellow',relief=RAISED,width='15',height='3',font=("Brush Script Std", 16),activebackground='light green',command=projectile.projectile_interface)
button1.pack()
button1.place(x=410,y=250)        #button for projectile motion


button2=Button(window,text='Collision',background='yellow',relief=RAISED,width='10',height='3',font=("Brush Script Std", 16),activebackground='light green',command=collision.collision_interface)
button2.pack()
button2.place(x=440,y=380)       #button for collision


button3=Button(window,text='Magnification by Concave Mirror',background='yellow',relief=RAISED,width='26',height='4',font=("Brush Script Std", 16),activebackground='light green',command=magnification.Linear_Magnification)
button3.pack()
button3.place(x=350,y=500)        #button for magnification by a concave mirror

button4=Button(window,text='Motion in a Verticle Circle',background='yellow',relief=RAISED,width='20',height='4',font=("Brush Script Std", 16),activebackground='light green',command=verticleCircle.verticle_circle_interface)
button4.pack()
button4.place(x=390,y=650)       #button for motion in verticle circle

window.mainloop()
