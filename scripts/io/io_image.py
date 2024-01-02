import cv2 as cv
import pathlib

base_dir = pathlib.Path(__file__).parent.parent.parent


# read image 
image_path = str(base_dir.joinpath('data','panda.jpg'))
image = cv.imread(image_path)

# write image
cv.imwrite(image_path,image)

# visualize image
cv.imshow("image",image)
cv.waitKey(0)
cv.destroyAllWindows()
# TODO Write captured video to memory 