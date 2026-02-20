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
        block1 = Image.open("lu.jpg")
        colonne,ligne= block1.size
        Nimg1 = Image.new('RGB',(colonne, ligne))          
        for i in range (ligne):
            for j in range (colonne):
                pixel=block1.getpixel((j,i))
                pixel3 = int((pixel[0]+pixel[1]+pixel[2])/3)
                p=(pixel3,pixel3,pixel3)
                Nimg1.putpixel((j,i),p)
        Nimg1.save('Nimg1.jpg')  
    if (k==2):
        block1 = Image.open("ru.jpg")
        colonne,ligne= block1.size
        Nimg2 = Image.new('RGB',(colonne, ligne))          
        for i in range (ligne):
            for j in range (colonne):
                pixel=block1.getpixel((j,i))
                pixel3 = int((pixel[0]+pixel[1]+pixel[2])/3)
                p=(pixel3,pixel3,pixel3)
                Nimg2.putpixel((j,i),p)
        Nimg2.save('Nimg2.jpg')  

    if (k==3):
        block1 = Image.open("rl.jpg")
        colonne,ligne= block1.size
        Nimg3 = Image.new('RGB',(colonne, ligne))          
        for i in range (ligne):
            for j in range (colonne):
                pixel=block1.getpixel((j,i))
                pixel3 = int((pixel[0]+pixel[1]+pixel[2])/3)
                p=(pixel3,pixel3,pixel3)
                Nimg3.putpixel((j,i),p)
        Nimg3.save('Nimg3.jpg')      
    if (k==4):
        block1 = Image.open("ll.jpg")
        colonne,ligne= block1.size
        Nimg4 = Image.new('RGB',(colonne, ligne))          
        for i in range (ligne):
            for j in range (colonne):
                pixel=block1.getpixel((j,i))
                pixel3 = int((pixel[0]+pixel[1]+pixel[2])/3)
                p=(pixel3,pixel3,pixel3)
                Nimg4.putpixel((j,i),p)
        Nimg4.save('Nimg4.jpg')                

    return

if __name__ == '__main__':
    
    TimeCode1 = time.time()
    ######################################
    # Cropped image of above dimension
    imageNC = Image.open('lena.jpg')
    width, height = imageNC.size
 
    # Setting the points for cropped image
    left = 0
    top = 0
    right = width / 2
    bottom = height /2
     
    # Cropped image of above dimension
    # (It will not change original image)

    imageC = imageNC.crop((left, top, right, bottom))
    # Shows the image in image viewer
    imageC.save('lu.jpg')
    T2Crop = time.time()

  ######################################
  ######################################
    # Cropped image of above dimension

    imageNC = Image.open('lena.jpg')
    width, height = imageNC.size
 
    # Setting the points for cropped image
    left = width /2
    top = 0
    right = width
    bottom = height /2
     
    # Cropped image of above dimension
    # (It will not change original image)

    imageC = imageNC.crop((left, top, right, bottom))
    # Shows the image in image viewer
    imageC.save('ru.jpg')
    ######################################
   ######################################
    # Cropped image of above dimension

    imageNC = Image.open('lena.jpg')
    width, height = imageNC.size
 
    # Setting the points for cropped image
    left = width /2
    top = height /2
    right = width
    bottom = height
     
    # Cropped image of above dimension
    # (It will not change original image)

    imageC = imageNC.crop((left, top, right, bottom))
    # Shows the image in image viewer
    imageC.save('rl.jpg')
  ######################################
  ######################################
   

    # Cropped image of above dimension

    imageNC = Image.open('lena.jpg')
    width, height = imageNC.size
 
    # Setting the points for cropped image
    left = 0
    top = height /2
    right = width /2
    bottom = height
     
    # Cropped image of above dimension
    # (It will not change original image)

    imageC = imageNC.crop((left, top, right, bottom))
    # Shows the image in image viewer
    imageC.save('ll.jpg')
  ######################################
  ######################################
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
        if (k==3):
            p = Process(target= filtre_fct, args=(3,))
            jobs.append(p)
            p.start()
        if (k==4):
            p = Process(target= filtre_fct, args=(4,))
            jobs.append(p)
            p.start()    
    for job in jobs:
        job.join()
       
    image1 = Image.open("lena.jpg")

    width, height = image1.size
       
    nimage = Image.new('RGB',(width, height))
    nimage.paste(Image.open('Nimg1.jpg'),(0,0))
    nimage.paste(Image.open('Nimg2.jpg'),(600,0))
    nimage.paste(Image.open('Nimg4.jpg'),(0,450))
    nimage.paste(Image.open('Nimg3.jpg'),(600,450))
   
    plt.imshow(nimage)
    plt.show()
    TimeCode2 = time.time()
    print('Le temps qu il nous faut pour appliquer un filtre gris avec parallelisme est estimé a : ')
    print(TimeCode2-TimeCode1)
   



