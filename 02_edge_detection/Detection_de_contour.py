from multiprocessing import Process, Array
import sys
import os
import time
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as im
import numpy as np



VarG = 0
def filtre_fct(k):
    if (k==1):
        T1Filtre = time.time()
        block1 = Image.open("lu.jpg")
        block2 = Image.open("lu1.jpg")
        block11 = Image.open("lu.jpg")
        block22 = Image.open("lu1.jpg")
        colonne,ligne= block11.size
        Nimg1 = Image.new('RGB',(colonne, ligne))          
        for i in range (ligne):
            for j in range (colonne):
                block11=block1.getpixel((j,i))
                block22=block2.getpixel((j,i))
                R=int(block11[0]-block22[0])
                G=int(block11[1]-block22[1])
                B=int(block11[2]-block22[2])
                m = ((R+G+B)/3)
                if (m > 70):
                    Nimg1.putpixel((j,i),(255,255,255))
                if (m < 70):
                    Nimg1.putpixel((j,i),(0,0,0))
        T2Filtre = time.time()
        print('Le temps qu il nous faut pour appliquer le filtre contour est estimé a : ')
        print(T2Filtre-T1Filtre)
        Nimg1.save('Nimg1.jpg')  
    if (k==2):
        block1 = Image.open("ru.jpg")
        block2 = Image.open("ru1.jpg")
        block11 = Image.open("ru.jpg")
        block22 = Image.open("ru1.jpg")
        colonne,ligne= block11.size
        Nimg2 = Image.new('RGB',(colonne, ligne))          
        for i in range (ligne):
            for j in range (colonne):
                block11=block1.getpixel((j,i))
                block22=block2.getpixel((j,i))
                R=int(block11[0]-block22[0])
                G=int(block11[1]-block22[1])
                B=int(block11[2]-block22[2])
                m = ((R+G+B)/3)
                if (m > 70):
                    Nimg2.putpixel((j,i),(255,255,255))
                if (m < 70):
                    Nimg2.putpixel((j,i),(0,0,0))
        Nimg2.save('Nimg2.jpg')  

    if (k==3):
        block1 = Image.open("rl.jpg")
        block2 = Image.open("rl1.jpg")
        block11 = Image.open("rl.jpg")
        block22 = Image.open("rl1.jpg")
        colonne,ligne= block11.size
        Nimg3 = Image.new('RGB',(colonne, ligne))          
        for i in range (ligne):
            for j in range (colonne):
                block11=block1.getpixel((j,i))
                block22=block2.getpixel((j,i))
                R=int(block11[0]-block22[0])
                G=int(block11[1]-block22[1])
                B=int(block11[2]-block22[2])
                m = ((R+G+B)/3)
                if (m > 70):
                    Nimg3.putpixel((j,i),(255,255,255))
                if (m < 70):
                    Nimg3.putpixel((j,i),(0,0,0))
        Nimg3.save('Nimg3.jpg')      
    if (k==4):
        block1 = Image.open("ll.jpg")
        block2 = Image.open("ll1.jpg")
        block11 = Image.open("ll.jpg")
        block22 = Image.open("ll1.jpg")
        colonne,ligne= block11.size
        Nimg4 = Image.new('RGB',(colonne, ligne))          
        for i in range (ligne):
            for j in range (colonne):
                block11=block1.getpixel((j,i))
                block22=block2.getpixel((j,i))
                R=int(block11[0]-block22[0])
                G=int(block11[1]-block22[1])
                B=int(block11[2]-block22[2])
                m = ((R+G+B)/3)
                if (m > 70):
                    Nimg4.putpixel((j,i),(255,255,255))
                if (m < 70):
                    Nimg4.putpixel((j,i),(0,0,0))
        Nimg4.save('Nimg4.jpg')                

    return

if __name__ == '__main__':
    TimeCode1 = time.time()
   
    ImageFile = 'REF.jpg'
    ImageFile1 = 'REF1.jpg'
   

    imgRef = Image.open(ImageFile)
    imgRef1 = Image.open(ImageFile1)

   
    img_gris=imgRef
    img_gris1=imgRef1

    colonne,ligne=imgRef.size
    T1gris = time.time()
    for i in range(ligne):
        for j in range(colonne):
            pixel = imgRef.getpixel((j,i))
            pixel3 = int((pixel[0]+pixel[1]+pixel[2])/3)
            p=(pixel3,pixel3,pixel3)
            img_gris.putpixel((j,i),p)
    T2gris = time.time()
    print('Le temps qu il nous faut pour appliquer un filtre gris est estimé a : ')
    print(T2gris-T1gris)
    img_gris.save('image_gris.jpg')
#    
    colonne1,ligne1=imgRef1.size
    for i in range(ligne1):
        for j in range(colonne1):
            pixel1 = imgRef1.getpixel((j,i))
            pixel31 = int((pixel1[0]+pixel1[1]+pixel1[2])/3)
            p=(pixel31,pixel31,pixel31)
            img_gris1.putpixel((j,i),p)
    img_gris1.save('image_gris1.jpg')
   
   
   

    ######################################
    # Cropped image of above dimension
    T1Crop = time.time()
    imageNC = Image.open('image_gris.jpg')
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
    print('Le temps qu il nous faut pour decouper une image est estimé a : ')
    print(T2Crop-T1Crop)
#    ######################################
  ######################################
    # Cropped image of above dimension

    imageNC = Image.open('image_gris1.jpg')
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
    imageC.save('lu1.jpg')
#    ######################################

  ######################################
    # Cropped image of above dimension

    imageNC = Image.open('image_gris.jpg')
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
#    ######################################

  ######################################
    # Cropped image of above dimension

    imageNC = Image.open('image_gris1.jpg')
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
    imageC.save('ru1.jpg')
#    ######################################
   ######################################
    # Cropped image of above dimension

    imageNC = Image.open('image_gris.jpg')
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
#    ######################################

  ######################################
    # Cropped image of above dimension

    imageNC = Image.open('image_gris1.jpg')
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
    imageC.save('rl1.jpg')
#    ######################################
 ######################################
    # Cropped image of above dimension

    imageNC = Image.open('image_gris.jpg')
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
#    ######################################

  ######################################
    # Cropped image of above dimension

    imageNC = Image.open('image_gris1.jpg')
    width, height = imageNC.size
 
    # Setting the points for cropped image
    left = 0
    top = height /2
    right = width / 2
    bottom = height
     
    # Cropped image of above dimension
    # (It will not change original image)

    imageC = imageNC.crop((left, top, right, bottom))
    # Shows the image in image viewer
    imageC.save('ll1.jpg')
#    ######################################




   
   
           
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
       
    image1 = Image.open("REF.jpg")

    width, height = image1.size
       
    nimage = Image.new('RGB',(width, height))
    nimage.paste(Image.open('Nimg1.jpg'),(0,0))
    nimage.paste(Image.open('Nimg2.jpg'),(336,0))
    nimage.paste(Image.open('Nimg4.jpg'),(0,252))
    nimage.paste(Image.open('Nimg3.jpg'),(336,252))
   
    plt.imshow(nimage)
    plt.show()
    TimeCode2 = time.time()
    print(TimeCode2-TimeCode1)