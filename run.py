import sys
sys.path.append("./ui/modules/")
from login import *
from Custom_Widgets import *
import mysql.connector
import warnings
warnings.filterwarnings("ignore")
import sys
import mainApp
class loginWidget(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show()
        self.connectEvents()
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ma77266100$1372mysql",
            database="smartvolley"
        )
        self.cursor = self.db.cursor()

        self.ui.usernameLe.installEventFilter(self)
        self.ui.passwordLe.installEventFilter(self)
    def connectEvents(self):
        self.ui.loginBtn.clicked.connect(self.loginFunction)

    def eventFilter(self, widget, event):
        if event.type() == QtCore.QEvent.KeyPress and (widget is self.ui.passwordLe or widget is self.ui.usernameLe) :
            key = event.key()
            if key == QtCore.Qt.Key_Return:
                self.ui.loginBtn.click()


    def loginFunction(self):
        username = self.ui.usernameLe.text()
        password = self.ui.passwordLe.text()
        message = QMessageBox(self)
        if username == "":
            message.setWindowTitle("Login Failed")
            message.setText("username cannot be empty")
            message.setStandardButtons(QMessageBox.Ok)
            message.setIcon(QMessageBox.Warning)
            message.exec_()
        elif password == "":
            message.setWindowTitle("Login Failed")
            message.setText("password cannot be empty")
            message.setStandardButtons(QMessageBox.Ok)
            message.setIcon(QMessageBox.Warning)
            message.exec_()
        else:
            self.cursor.execute("SELECT * FROM login WHERE username LIKE " + "\'"+username+"\'"+ "AND password LIKE " + "\'" + password + "\'" + " LIMIT 1" )
            results = self.cursor.fetchall()
            if len(results) == 0:
                message.setWindowTitle("Login Failed")
                message.setText("Wrong username or password")
                message.setStandardButtons(QMessageBox.Ok)
                message.setIcon(QMessageBox.Warning)
                message.exec_()
            else:
                appWindow = mainApp.MainWindow()
                appWindow.show()
                self.destroy()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = loginWidget()
    sys.exit(app.exec_())