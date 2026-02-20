from multiprocessing import Process, Array
import sys
import os
import time
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as im
import numpy as np

if __name__ == '__main__':
    
    TimeCode1 = time.time()
    ImageFile = 'lena.jpg'
    imgRef = Image.open(ImageFile)
    lena_gris=imgRef
    colonne,ligne=imgRef.size
    T1gris = time.time()
    for i in range(ligne):
        for j in range(colonne):
            pixel = imgRef.getpixel((j,i))
            pixel3 = int((pixel[0]+pixel[1]+pixel[2])/3)
            p=(pixel3,pixel3,pixel3)
            lena_gris.putpixel((j,i),p)
    plt.imshow(lena_gris)
    plt.show()
    T2gris = time.time()
    print('Le temps qu il nous faut pour appliquer un filtre gris est estimé a : ')
    print(T2gris-T1gris)
    lena_gris.save('lena_gris.jpg')