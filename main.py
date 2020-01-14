# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:54:42 2020

@author: cytsai
"""

from PIL import Image
import cmath
pi2 = cmath.pi * 2.0

def DFT2D(image):
    global M, N
    (M, N) = image.size # (imgx, imgy)
    dft2d_red = [[0.0 for k in range(M)] for l in range(N)] 
    pixels = image.load()
    for k in range(M):
        print(k)
        for l in range(N):
            sum_red = 0.0
            for m in range(M):
                for n in range(N):
                    (red) = pixels[m, n]
                    e = cmath.exp(- 1j * pi2 * (float(k * m) / M + float(l * n) / N))
                    sum_red += red * e
            dft2d_red[l][k] = sum_red / M / N
    return dft2d_red
        
def IDFT2D(dft2d):
    (dft2d_red, dft2d_grn, dft2d_blu) = dft2d
    global M, N
    image = Image.new("RGB", (M, N))
    pixels = image.load() 
    for m in range(M):
        for n in range(N):
            sum_red = 0.0
            for k in range(M):
                for l in range(N):
                    e = cmath.exp(1j * pi2 * (float(k * m) / M + float(l * n) / N))
                    sum_red += dft2d_red[l][k] * e
            red = int(sum_red.real + 0.5)
            pixels[m, n] = (red)
    return image

# TEST
# Recreate input image from 2D DFT results to compare to input image
image = Image.open("33.jpg")
print(image.size)
image = DFT2D(image)
print('dft done')
image = IDFT2D(image)
image.save("output.png", "PNG")