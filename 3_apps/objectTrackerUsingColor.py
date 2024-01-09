import cv2 as cv 
import pathlib
import numpy as np 
from PIL import Image
from utils.getColorLimits import get_limits

# read webcam
cap = cv.VideoCapture(1)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# color_to_detect = [255,0,0] #blue in BGR colorspace
color_to_detect = [222,126,91] #Malibu Blue in BGR colorspace

while(True):
    # take each frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # convert from BGR to HSV colorspace
    hsv_img = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    # get upper and lower limits of color of interest for detection
    lower_limit, upper_limit = get_limits(color_to_detect)

    # define mask
    mask = cv.inRange(hsv_img,lower_limit,upper_limit)

    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv.rectangle(frame, (x1,y1),(x2,y2), (255,0,0), 5)
    

    # cv.imshow("mask",mask)
    cv.imshow("frame",frame)
    if cv.waitKey(1) & 0xFF == ord('q'):  #break when the key q is pressed on the keyboard
        break

cap.release()
cv.destroyAllWindows()

