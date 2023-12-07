import cv2
import pathlib

base_dir = pathlib.Path(__file__).parent.parent.parent

# read video
video_path = str(base_dir.joinpath('data','panda-vid.MP4'))
video = cv2.VideoCapture(video_path)

# visualize video
ret = True
while ret:
    ret, frame = video.read()
    if ret:
        cv2.imshow("frame",frame)
        cv2.waitKey(40)   #40 milisecs for video with 25frames/sec
video.release()
cv2.destroyAllWindows()