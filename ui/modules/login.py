# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginKJTbMW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowFlags(Qt.FramelessWindowHint)
        Form.setAttribute(Qt.WA_TranslucentBackground)
        Form.resize(450, 550)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 30, 370, 480))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 40, 300, 420))
        self.label.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop:0.835227 rgba(0, 0, 0, 75));\n"
"border-image: url(:/images-downloaded/images/downloaded/background.png);\n"
"border-radius:20px")
        self.label.setScaledContents(False)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 60, 280, 390))
        self.label_2.setStyleSheet(u"background-color:rgba(0,0,0,100);\n"
"border-radius:15px;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(135, 95, 90, 40))
        font = QFont()
        font.setFamily(u"HP Simplified Light")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color:rgba(255,255,255,210);")
        self.usernameLe = QLineEdit(self.widget)
        self.usernameLe.setObjectName(u"usernameLe")
        self.usernameLe.setGeometry(QRect(80, 165, 200, 40))
        font1 = QFont()
        font1.setPointSize(10)
        self.usernameLe.setFont(font1)
        self.usernameLe.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.passwordLe = QLineEdit(self.widget)
        self.passwordLe.setObjectName(u"passwordLe")
        self.passwordLe.setGeometry(QRect(80, 230, 200, 40))
        self.passwordLe.setFont(font1)
        self.passwordLe.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.passwordLe.setEchoMode(QLineEdit.Password)
        self.loginBtn = QPushButton(self.widget)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setGeometry(QRect(80, 310, 200, 40))
        font2 = QFont()
        font2.setFamily(u"HP Simplified Light")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.loginBtn.setFont(font2)
        self.loginBtn.setStyleSheet(u"QPushButton#loginBtn{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#loginBtn:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#loginBtn:pressed{	\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105, 118, 132, 200);\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Log In", None))
        self.usernameLe.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.passwordLe.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.loginBtn.setText(QCoreApplication.translate("Form", u"Log in", None))
    # retranslateUi

