import cv2
import numpy as np
from threading import Thread

DVR_IP = '169.254.108.159'
USER_NAME = 'admin'
PASSWORD = 'admin000'

class RtspCamera:
    def __init__(self, num  ):
        self.rtsp_url = f"rtsp://{USER_NAME}:{PASSWORD}@{DVR_IP}:554/h264/ch{num}/main/av_stream"
        print("connecting with dvr...")
        self.cap = cv2.VideoCapture(self.rtsp_url)
        print("connected")

    def read(self):
        ret, frame = self.cap.read()
        try:
            frame = cv2.resize(frame, (frame.shape[1]//2, frame.shape[0]//2), interpolation=cv2.INTER_CUBIC)
            return ret, frame
        except:
            print("fail! , connecting with dvr again...")
            self.cap.release()
            self.cap = cv2.VideoCapture(self.rtsp_url)
            print("connected")
            self.read()
            return False, np.zeros((500,500,3), dtype=np.uint8)

class FastRtspStream:
    def __init__(self, camera_number):
        self.stream = True
        self.cap1 = RtspCamera(camera_number)
        self.t1 = Thread(target=self.__get_frame)
        self.frame1 = np.zeros((500,500,3), dtype=np.uint8)
        self.t1.start()
    def __get_frame(self):
        while self.stream:
            self.frame1 = self.cap1.read()[1]

    def release(self):
        print("ended")
        self.stream = False
        self.t1.join()
        cv2.destroyAllWindows()
    
    def read(self):
        return self.frame1
        
if __name__ == "__main__":
    cap = FastRtspStream(1)
    while True:
        frame = cap.read()
        cv2.imshow("frame", frame)
        key = cv2.waitKey(1)
        if key ==27:
            break
        elif key == ord("s"):
            cv2.imwrite(r"C:\Users\moman\OneDrive\Desktop\croco\yolov7\test_images_by_me\img.png", frame)
            print("DONE ")
    cap.release()
