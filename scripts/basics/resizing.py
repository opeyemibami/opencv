import cv2 as cv
import  pathlib

base_dir = pathlib.Path(__file__).parent.parent.parent

# read image 
image_path = str(base_dir.joinpath('data','panda2.jpg'))
image = cv.imread(image_path)

# resize image
resize_image = cv.resize(image,(510,255))

print(image.shape)
print(resize_image.shape)

cv.imshow("image",image)
cv.imshow("resize_image",resize_image)
cv.waitKey(0)
