import cv2 as cv
import numpy as np


def get_limits(color_in_BGR):
    """
    return HSV upper and lower limts of a BGR color
    """
    # lower_limit, upper_limit = None
    BGRColorFrame = np.uint8([[color_in_BGR]])
    hsvColorFrame = cv.cvtColor(BGRColorFrame, cv.COLOR_BGR2HSV)
    lower_limit = hsvColorFrame[0][0][0] - 10, 100, 100 #OpenCV uses H: 0-179, S: 0-255, V: 0-255
    lower_limit = np.uint8([[np.uint8([lower_limit[0], 100, 100])]])
    upper_limit = hsvColorFrame[0][0][0] + 10, 255, 255 #OpenCV uses H: 0-179, S: 0-255, V: 0-255
    upper_limit = np.uint8([[np.uint8([upper_limit[0], 255, 255])]])
    return lower_limit, upper_limit