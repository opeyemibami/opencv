import cv2 as cv 
import pathlib 
import numpy as np

base_dir = pathlib.Path(__file__).parents[2]
img_path = str(base_dir.joinpath("data","yhemmy1.jpg"))
# read image
img = cv.imread(img_path)

# edge detection
img_edge = cv.Canny(img,130,170)

# dilate
img_edge_dilate = cv.dilate(img_edge,np.ones((3,3),dtype=np.int8))

# Erode 
img_edge_erode = cv.erode(img_edge_dilate,np.ones((3,3),dtype=np.int8))

cv.imshow("img",img)
cv.imshow("img_edge",img_edge)
cv.imshow("img_edge_dilate",img_edge_dilate)
cv.imshow("img_edge_erode",img_edge_erode)
cv.waitKey(0)