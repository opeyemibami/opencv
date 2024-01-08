import cv2
import pathlib

base_dir = pathlib.Path(__file__).parent.parent
output_path = str(base_dir.joinpath('data','output.avi'))

# read webcam
webcam = cv2.VideoCapture(1)
if not webcam.isOpened():
    print("Cannot open camera")
    exit()

# We need to set resolutions. 
# so, convert them from float to integer. 
frame_width = int(webcam.get(3)) 
frame_height = int(webcam.get(4)) 
size = (frame_width, frame_height)

# to save video after capture, define video writer 
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter(output_path,fourcc,20,size)

# visualize 
while True:
    ret, frame = webcam.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Perform operation on the capture and save
    frame = cv2.flip(frame, 0)
    out.write(frame)

    cv2.imshow("frame",frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):  #break when the key q is pressed on the keyboard
        break

webcam.release() #release memory
cv2.destroyAllWindows()