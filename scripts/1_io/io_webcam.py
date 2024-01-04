import cv2

# read webcam
webcam = cv2.VideoCapture(1)
if not webcam.isOpened():
    print("Cannot open camera")
    exit()

# visualize 
while True:
    ret, frame = webcam.read()
    cv2.imshow("frame",frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):  #break when the key q is pressed on the keyboard
        break

webcam.release() #release memory
cv2.destroyAllWindows()