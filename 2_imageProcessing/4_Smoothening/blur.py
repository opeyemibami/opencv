import cv2 as cv
import pathlib

base_dir = pathlib.Path(__file__).parent.parent.parent

# read image 
image_path = str(base_dir.joinpath('data','beach.jpg'))
image = cv.imread(image_path)

# blur
k_size = 9
img_blur = cv.blur(image,(k_size,k_size))
img_gaussian_blur = cv.GaussianBlur(image,(k_size,k_size),7)
img_median_blur = cv.medianBlur(image,k_size)
img_bilateral_blur = cv.bilateralFilter(image,9,9,9)

# visualize images
cv.imshow("image",image)
cv.imshow("blur",img_blur)
cv.imshow("gaussian",img_gaussian_blur)
cv.imshow("median",img_median_blur)
cv.imshow("bilateral_blur",img_bilateral_blur)
cv.waitKey(0)