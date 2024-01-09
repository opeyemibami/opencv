import cv2 as cv 
import numpy as np 
import pathlib

base_dir = pathlib.Path(__file__).parent.parent.parent

# read image in grayscale 
image_path = str(base_dir.joinpath('data','handwritten.png'))
img = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
img = cv.bitwise_not(img) # to have ideal image for this operations

# morphological transformations
kernel = np.ones((3,3),np.uint8)
erosion = cv.erode(img,kernel,iterations = 1)
dilation = cv.dilate(img,kernel,iterations = 1)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

cv.imshow("img",img)
cv.imshow("erosion",erosion)
cv.imshow("dilation",dilation)
cv.imshow("opening",opening)
cv.imshow("closing",closing)
cv.imshow("gradient",gradient)
cv.imshow("tophat",tophat)
cv.imshow("blackhat",blackhat)
cv.waitKey(0)