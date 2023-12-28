from threading import  Thread
import sys
import cv2
import os
from datetime import date
import time

class recorder:
    def __init__(self):
        self.recording_started = False
    def configure(self, cameraIp):
        self.frame_buffer = []
        self.capture = cv2.VideoCapture(cameraIp)
        ret , frame = self.capture.read()
        self.frame_buffer.append(frame)
        fshape = frame.shape
        fheight = fshape[0]
        fwidth = fshape[1]
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        fileDirectory = "./records/"+str(date.today())
        os.makedirs(fileDirectory,exist_ok=True)
        current_time = time.localtime(time.time())
        fileAddress = fileDirectory+"/"+str(current_time.tm_hour)+"-"+str(current_time.tm_min)+"-"+str(current_time.tm_sec)+".avi"
        self.writer = cv2.VideoWriter(fileAddress, fourcc, 30.0, (fwidth, fheight))
    def update(self):
        while self.recording_started:
            ret, frame = self.capture.read()
            self.frame_buffer.append(frame)
            self.writer.write(self.frame_buffer[0])
            self.frame_buffer.pop(0)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def start(self):
        self.recording_started = True
        t = Thread(target=self.update,args=())
        t.start()
    def stop(self):
        self.recording_started = False




