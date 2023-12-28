import threading
import cv2
import numpy as np
import sys
import time
from PySide2 import QtGui

class camera_handler():
    def __init__(self, container):
        self.container = container
        self.cameraStarted = False

    def connect(self, address, delay):
        self.cameraIp = address
        self.delay = delay
        self.start_time = time.time()
        try:
            self.capture = cv2.VideoCapture(self.cameraIp)
            if self.capture == None:
                print("no camera found")
                sys.exit()
        except:
            print("capture Error")
            sys.exit()
        self.start()

    def wait_delay(self):
        self.frame_buffer = []
        ret, frame = self.capture.read()
        current_time = time.time()
        while(ret and ((current_time-self.start_time) < self.delay)):
            self.frame_buffer.append(frame)
            ret, frame = self.capture.read()
            current_time = time.time()
        # one frame can be destroyed in this logic!
    def display(self):
        # self.wait_delay()
        self.frame_buffer = []
        self.cameraStarted = True
        self.container.ui.camConnectBtn.setStyleSheet("color:green;")
        self.container.ui.camConnectBtn.setText("Disconnect")
        self.container.ui.camDisplayPages.setCurrentIndex(1)
        if len(self.frame_buffer) == 0:
            ret, frame = self.capture.read()
            self.frame_buffer.append(frame)
        # while((len(self.frame_buffer) > 0) and self.cameraStarted):
        #     current_frame = self.frame_buffer[0]
        #     self.frame_buffer.pop(0)
        #     height, width, channel = current_frame.shape
        #     bytesPerLine = 3 * width
        #     qImg = QtGui.QImage(current_frame.data, width, height, bytesPerLine,QtGui.QImage.Format_RGB888).rgbSwapped()
        #     pixmap = QtGui.QPixmap.fromImage(qImg)
        #     self.container.ui.camDisplayConnectedLabel.setPixmap(pixmap)
        #     self.container.ui.camDisplayConnectedLabel.show()
        #     ret, frame = self.capture.read()
        #     if ret:
        #         self.frame_buffer.append(frame)
        #     if cv2.waitKey(1) & 0xFF == ord('q'):
        #         break
        while(self.cameraStarted):
            if len(self.frame_buffer) > 0:
                current_frame = self.frame_buffer[0]
                self.frame_buffer.pop(0)
                height, width, channel = current_frame.shape
                bytesPerLine = 3 * width
                qImg = QtGui.QImage(current_frame.data, width, height, bytesPerLine,QtGui.QImage.Format_RGB888).rgbSwapped()
                pixmap = QtGui.QPixmap.fromImage(qImg)
                self.container.ui.camDisplayConnectedLabel.setPixmap(pixmap)
                self.container.ui.camDisplayConnectedLabel.show()
            ret, frame = self.capture.read()
            if ret:
                self.frame_buffer.append(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    def start(self):
        t = threading.Thread(target=self.display,args = ())
        t.daemon = True
        t.start()
    def stop(self):
        self.cameraStarted = False
        self.container.ui.camConnectBtn.setStyleSheet("color:red;")
        self.container.ui.camConnectBtn.setText("Connect")
        self.container.ui.camDisplayPages.setCurrentIndex(0)
