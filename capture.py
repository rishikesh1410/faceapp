
import cv2 , time
from PIL import Image
video = cv2.VideoCapture(0)
check, frame = video.read()


#gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
cv2.imshow("Capturing", frame)

key = cv2.waitKey(1)
#time.sleep(4)
cv2.destroyWindow("Capturing")
data = np.asarray(frame)
frame = np.array(Image.fromarray(np.roll(data, 1, axis=-1)))
