# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\user\Desktop\pyqt5\alarmUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(800, 450)
        self.time = QtWidgets.QLCDNumber(Form)
        self.time.setGeometry(QtCore.QRect(30, 80, 671, 281))
        self.time.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.time.setFrameShadow(QtWidgets.QFrame.Raised)
        self.time.setSmallDecimalPoint(False)
        self.time.setMode(QtWidgets.QLCDNumber.Dec)
        self.time.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.time.setObjectName("time")
        self.date = QtWidgets.QLabel(Form)
        self.date.setGeometry(QtCore.QRect(40, 20, 651, 61))
        self.date.setObjectName("date")
        self.date.setStyleSheet("font: bold 25pt")
        self.date.setAlignment(Qt.AlignCenter)
        self.setting = QtWidgets.QPushButton(Form)
        self.setting.setGeometry(QtCore.QRect(100, 350, 151, 51))
        self.setting.setObjectName("setting")
        self.camera = QtWidgets.QPushButton(Form)
        self.camera.setGeometry(QtCore.QRect(520, 350, 151, 51))
        self.camera.setObjectName("camera")

        self.sound = QtWidgets.QPushButton(Form)
        self.sound.setGeometry(QtCore.QRect(310, 350, 151, 51))
        self.sound.setObjectName("sound")

        self.retranslateUi(Form)
        self.setting.clicked.connect(Form.settingAlarm)
        self.camera.clicked.connect(Form.showCamera)

        self.sound.clicked.connect(Form.settingSound)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "SleepNoMore"))
        self.date.setText(_translate("Form", "TextLabel"))
        self.setting.setText(_translate("Form", "알람설정"))
        self.camera.setText(_translate("Form", "카메라확인"))
        self.sound.setText(_translate("Form", "알람문구설정"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
