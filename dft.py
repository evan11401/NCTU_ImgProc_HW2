# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:30:21 2020

@author: cytsai
"""
import numpy as np
import cv2

# 2 Dimension Fourier Transform:
def DFT2D(image):
    global M, N
    (M, N) = image.size # (imgx, imgy)
    dft2d_red = [[0.0 for k in range(M)] for l in range(N)] 
    dft2d_grn = [[0.0 for k in range(M)] for l in range(N)] 
    dft2d_blu = [[0.0 for k in range(M)] for l in range(N)] 
    pixels = image.load()
    for k in range(M):
        for l in range(N):
            sum_red = 0.0
            sum_grn = 0.0
            sum_blu = 0.0
            for m in range(M):
                for n in range(N):
                    (red, grn, blu, alpha) = pixels[m, n]
                    e = cmath.exp(- 1j * pi2 * (float(k * m) / M + float(l * n) / N))
                    sum_red += red * e
                    sum_grn += grn * e
                    sum_blu += blu * e
            dft2d_red[l][k] = sum_red / M / N
            dft2d_grn[l][k] = sum_grn / M / N
            dft2d_blu[l][k] = sum_blu / M / N
    return (dft2d_red, dft2d_grn, dft2d_blu)

def IDFT2D(dft2d):
    (dft2d_red, dft2d_grn, dft2d_blu) = dft2d
    global M, N
    image = Image.new("RGB", (M, N))
    pixels = image.load() 
    for m in range(M):
        for n in range(N):
            sum_red = 0.0
            sum_grn = 0.0
            sum_blu = 0.0
            for k in range(M):
                for l in range(N):
                    e = cmath.exp(1j * pi2 * (float(k * m) / M + float(l * n) / N))
                    sum_red += dft2d_red[l][k] * e
                    sum_grn += dft2d_grn[l][k] * e
                    sum_blu += dft2d_blu[l][k] * e
            red = int(sum_red.real + 0.5)
            grn = int(sum_grn.real + 0.5)
            blu = int(sum_blu.real + 0.5)
            pixels[m, n] = (red, grn, blu)
    return image


image = cv2.imread("33.jpg", cv2.IMREAD_GRAYSCALE)
print(image.shape)
image = DFT(image)
print("DFT done!")
image = IDFT(image)
cv2.imshow('My Image', image)
#image.save("output.png", "PNG")