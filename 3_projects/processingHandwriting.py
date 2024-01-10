import cv2 as cv 
import numpy as np 
import pathlib

base_dir = pathlib.Path(__file__).parent.parent

# read image in grayscale 
image_path = str(base_dir.joinpath('data','handwritten.png'))
img = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

# morphological transformation
kernel = np.ones((3,3),np.uint8)
img_inverted = cv.bitwise_not(img)
tophat = cv.morphologyEx(img_inverted, cv.MORPH_TOPHAT, kernel)
img_inverted = cv.bitwise_not(tophat)
# thresholding
ret, otsu_thresh = cv.threshold(img_inverted,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
ret, simple_plus_otsu_thresh = cv.threshold(img_inverted,ret+10,255,cv.THRESH_BINARY)



# Using Adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,21,30)

cv.imshow("img",img)
cv.imshow('simple_plus_otsu_thresh',simple_plus_otsu_thresh)
cv.imshow('otsu_thresh',otsu_thresh)
cv.imshow('adaptive_thresh',adaptive_thresh)
cv.waitKey(0)