import cv2
import time
import threading
from PIL import Image
from pynput import keyboard
from pynput.keyboard import Key, Controller
from datetime import datetime, timedelta
# define a video capture object
vid = cv2.VideoCapture(0)
vid_cod = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter("test.mp4", vid_cod, 20.0, (640,480))
keyboard = Controller()
def capture():
    period = timedelta(seconds=10)
    next_time = datetime.now() + period
    while (True):

            ret, frame = vid.read()
            cv2.imshow("frame", frame)
            output.write(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if next_time <= datetime.now():
                keyboard.press('q')

    vid.release()
    output.release()

    cv2.destroyAllWindows()

def vid_to_img():
    cap = cv2.VideoCapture(r"C:\Users\yashb\PycharmProjects\proxy\test.mp4")
    i = 0
    j = 1
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        if j < 16:
            cv2.imwrite('videoyash' + str(i) + '.jpg', frame)
            i += 1
            j += 1

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture()
    time.sleep(5)
    vid_to_img()
    time.sleep(5)
