import cv2 as cv
import  pathlib

base_dir = pathlib.Path(__file__).parent.parent.parent

# read image 
image_path = str(base_dir.joinpath('data','handwritten.png'))
image = cv.imread(image_path)

# convert to grayscale
img_gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

# simeple thresholding
ret, simple_thresh = cv.threshold(img_gray,100,255,cv.THRESH_BINARY)
print(ret)
# Otsu's thresholding
ret, otsu_thresh = cv.threshold(img_gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
# Otsu's thresholding after Gaussian filtering
blur = cv.GaussianBlur(img_gray,(5,5),0)
ret_otsu, gaussian_otsu_thresh = cv.threshold(blur,139.0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
print(ret)
ret, simple_thresh_otsu_ret = cv.threshold(img_gray,ret_otsu,255,cv.THRESH_BINARY)

cv.imshow("image",image)
cv.imshow("simple_thresh",simple_thresh)
cv.imshow("otsu_thresh",otsu_thresh)
cv.imshow("gaussian_otsu_thresh",gaussian_otsu_thresh)
cv.imshow("simple_thresh_otsu_ret",simple_thresh_otsu_ret)
cv.waitKey(0)