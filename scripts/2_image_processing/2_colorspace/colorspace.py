import cv2 as cv
import pathlib


base_dir = pathlib.Path(__file__).parent.parent.parent


# read image 
image_path = str(base_dir.joinpath('data','leave.jpg'))
image = cv.imread(image_path)

# color conversion
img_gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
img_rgb = cv.cvtColor(image,cv.COLOR_BGR2RGB)
img_hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)

# visualize 
cv.imshow("image",image)
cv.imshow("gray",img_gray)
cv.imshow("rgb",img_rgb)
cv.imshow("hsv",img_hsv)
cv.waitKey(0)
cv.destroyAllWindows()