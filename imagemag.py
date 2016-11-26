from ImageWriter import *
'''f=float(raw_input('enter the focal length of the convex lens'))
u=float(raw_input('enter the distance of the object from the convex lens'))
v=(f*u)/(u-f)
magnification= (v/u)
print magnification
import PIL
from PIL import Image
img = Image.open('test.png')'''
img1=loadPicture('p2.bmp')
showPicture(img1)
'''size=img.size[0]
print size
print img.size[1]
basewidth = int(size*magnification)
heightwidth=int(img.size[1]*magnification)
print basewidth
print heightwidth
img=img.resize((basewidth,heightwidth), PIL.Image.ANTIALIAS)
img.save('test.png')'''
'''wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)'''
img1=loadPicture('test.png')
showpicture(img1)
        
        
