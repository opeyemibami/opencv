import cv2 as cv
import  pathlib

base_dir = pathlib.Path(__file__).parent.parent.parent

# read image 
image_path = str(base_dir.joinpath('data','panda2.jpg'))
image = cv.imread(image_path)

# crop the image by indexing
cropped_image = image[:,225:765]

print(image.shape)
print(cropped_image.shape)

cv.imshow("image",image)
cv.imshow("cropped_image",cropped_image)
cv.waitKey(0)
