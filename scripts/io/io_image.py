import cv2
import pathlib

base_dir = pathlib.Path(__file__).parent.parent.parent


# read image 
image_path = str(base_dir.joinpath('data','panda.jpg'))
image = cv2.imread(image_path)


# visualize image
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()