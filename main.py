import sys
sys.path.append("./ui/modules/")
sys.path.append("./handlers/")
import os
from interface import *
from Custom_Widgets import *
import camera
import media
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self=self,ui=self.ui,jsonFiles=["./ui/jsons/style.json"])
        self.show()

        self.connectEvents()

        self.cameraHandler = camera.camera_handler(container = self)
        self.defaultCameraAddress = "127.0.0.1"
        self.recorder = media.recorder()

    def connectEvents(self):
        #Center Menu
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())

        #Right Menu
        self.ui.moreMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.profileMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())

        #Notification
        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())

        #Camera
        self.ui.camConnectBtn.clicked.connect(self.events)

        #Camera Controller Menu
        self.ui.camControllerOpenBtn.clicked.connect(lambda: self.ui.camControllerMenuSubContainer.expandMenu())
        self.ui.camControllerCloseBtn.clicked.connect(lambda: self.ui.camControllerMenuSubContainer.collapseMenu())
        self.ui.recordCb.stateChanged.connect(self.events)
    def events(self):
        if self.sender() == self.ui.camConnectBtn:
            #add delay mechanism
            if self.ui.camConnectBtn.text() == "Connect":
                address = ""
                if self.ui.camAddressLe.text() == "":
                    address = self.defaultCameraAddress
                else:
                    address = self.ui.camAddressLe.text()
                self.cameraHandler.connect(address = address, delay = 0)
            else:
                self.cameraHandler.stop()

        elif self.sender() == self.ui.recordCb:
            if self.ui.recordCb.isChecked():
                print("checked")
                self.recorder.configure(self.cameraHandler.cameraIp)
                self.recorder.start()
            else:
                print("unchecked")
                if self.recorder.recording_started:
                    self.recorder.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())