import sys
sys.path.append("./ui/modules/")
import os
from interface import *
from Custom_Widgets import *
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self=self,ui=self.ui,jsonFiles=["./ui/jsons/style.json"])
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())