import cv2 as cv
import  pathlib

base_dir = pathlib.Path(__file__).parent.parent.parent

# read image 
image_path = str(base_dir.joinpath('data','handwritten.png'))
image = cv.imread(image_path)

# convert to grayscale
img_gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

# thresholding
ret, simple_thresh = cv.threshold(img_gray,100,255,cv.THRESH_BINARY)
adaptive_thresh = cv.adaptiveThreshold(img_gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,21,30)


cv.imshow("image",image)
cv.imshow("simple_thresh",simple_thresh)
cv.imshow("adaptive_thresh",adaptive_thresh)
cv.waitKey(0)
