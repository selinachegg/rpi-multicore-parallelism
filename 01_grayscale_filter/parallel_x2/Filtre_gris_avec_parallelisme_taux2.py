from multiprocessing import Process, Array
import sys
import os
import time
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as im
import numpy as np


def filtre_fct(k):
    if (k==1):
        block1 = Image.open("l.jpg")
        colonne,ligne= block1.size
        left = Image.new('RGB',(colonne, ligne))          
        for i in range (ligne):
            for j in range (colonne):
                pixel=block1.getpixel((j,i))
                pixel3 = int((pixel[0]+pixel[1]+pixel[2])/3)
                p=(pixel3,pixel3,pixel3)
                left.putpixel((j,i),p)
        left.save('left.jpg')  
    if (k==2):
        block1 = Image.open("r.jpg")
        colonne,ligne= block1.size
        right = Image.new('RGB',(colonne, ligne))          
        for i in range (ligne):
            for j in range (colonne):
                pixel=block1.getpixel((j,i))
                pixel3 = int((pixel[0]+pixel[1]+pixel[2])/3)
                p=(pixel3,pixel3,pixel3)
                right.putpixel((j,i),p)
        right.save('right.jpg')  
    return

if __name__ == '__main__':
    
    TimeCode1 = time.time()
    # Opens a image in RGB mode
    im = Image.open("lena.jpg")

    # Size of the image in pixels (size of original image)
    # (This is not mandatory)
    width, height = im.size

    # Setting the points for cropped image
    left = 0
    top = 0
    right = width/2
    bottom = height

    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))

    im1.save('l.jpg')
  ######################################
  ######################################
    # Opens a image in RGB mode
    im = Image.open("lena.jpg")

    # Size of the image in pixels (size of original image)
    # (This is not mandatory)
    width, height = im.size

    # Setting the points for cropped image
    left = width/2
    top = 0
    right = width
    bottom = height

    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))

    im1.save('r.jpg')
    ######################################
   ####################################
    jobs = []
    for k in range(1,5):
        if (k==1):
            p = Process(target= filtre_fct, args=(1,))
            jobs.append(p)
            p.start()
        if (k==2):
            p = Process(target= filtre_fct, args=(2,))
            jobs.append(p)
            p.start()    
    for job in jobs:
        job.join()
       
    image1 = Image.open("lena.jpg")

    width, height = image1.size
       
    nimage = Image.new('RGB',(width, height))
    nimage.paste(Image.open('left.jpg'),(0,0))
    nimage.paste(Image.open('right.jpg'),(600,0))
    plt.imshow(nimage)
    plt.show()
    TimeCode2 = time.time()
    print('Le temps qu il nous faut pour appliquer un filtre gris avec parallelisme est estimé a : ')
    print(TimeCode2-TimeCode1)
   



