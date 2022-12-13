import cv2
import sys
import numpy as np

# Options
PREVIEW = 0
BLUR = 1
FEATURES = 2
CANNY = 3

feature_params = dict( maxCorners = 500,
                       qualityLevel = 0.2,          # Maximum quality * quality level sets the threshold to consider the corners only if above it
                       minDistance = 15,            # Euclidean distance in pixel space
                       blockSize = 9)

s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

image_filter = PREVIEW
Alive = True

source = cv2.VideoCapture(s)

win_name = "Image Filters"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
result = None

while Alive:
    has_frame, frame = source.read()
    if not has_frame:
        print('An error occurred')
        break

    frame = cv2.flip(frame, 1)

    if image_filter == PREVIEW:
        result = frame
    elif image_filter == BLUR:
        result = cv2.blur(frame, ksize=(13,13))  # Kernel matrix size must always be odd
    elif image_filter == CANNY:
        result = cv2.Canny(frame, 145, 150)    # Ignores the pizel gradients (edges) below the lower threshold and considers all the pixel gradients above the higher threshold. However if an edge is between the the lower and higher threshold value, it will consider the edge only if its next to a higher threshold
    elif image_filter == FEATURES:
        result = frame
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(frame_gray, **feature_params)
        if corners is not None:
            for x, y in np.float32(corners).reshape(-1,2):
                x=np.round(x).astype("int")
                y=np.round(y).astype("int")
                cv2.circle(result, (x,y), 7, (0,255,0), 1)

    cv2.imshow(win_name, result)

    key = cv2.waitKey(1)
    if key == ord('q') or key == ord('Q') or key == 27:
        Alive = False
    elif key == ord('b') or key == ord('B'):
        image_filter = BLUR
    elif key == ord('c') or key == ord('C'):
        image_filter = CANNY
    elif key == ord('f') or key == ord('F'):
        image_filter = FEATURES
    elif key == ord('p') or key == ord('P'):
        image_filter = PREVIEW

source.release()
cv2.destroyWindow(win_name)