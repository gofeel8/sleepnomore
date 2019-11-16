#-*- coding:utf-8 -*-
import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QCheckBox, QTimeEdit, QSpinBox, QDial, QLineEdit, QTextEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication, QTime, Qt, QTimer, QUrl
#from PyQt5.QtMultimedia import QSoundEffect

from gtts import gTTS
# from PyQt5.QtCore import QTime, QTimer
# from PyQt5.QtWidgets import QApplication, QLCDNumber


class setSound(QWidget):
    def __init__(self):
        super(QWidget,self).__init__()
        self.initUI()

    def initUI(self):
        # self.setGeometry(0, 0, 500, 520)
        self.setWindowTitle("알람 소리 설정")
        self.resize(500, 400)
        self.bell_text = QTextEdit(self)
        self.bell_text.move(40, 60)
        self.bell_text.resize(400, 200)

        self.save = QPushButton(self)
        self.save.setText("저장")
        self.save.resize(120, 60)
        self.save.move(180, 280)
        self.save.clicked.connect(self.saveText)

        self.cancle = QPushButton(self)
        self.cancle.setText("취소")
        self.cancle.resize(120, 60)
        self.cancle.move(320, 280)
        self.cancle.clicked.connect(self.exit)

        self.loadText()

        # self.basicBell = QCheckBox("기본벨 사용", self)
        # self.basicBell.move(30, 280)
        # self.basicBell.setChecked(True)

        # self.customBell = QCheckBox("알람문구 사용", self)
        # self.customBell.move(30, 320)

        self.lb = QLabel("알람문구", self)
        self.lb.move(40, 35)

        # self.show()

    def showWindow(self):
        self.loadText()
        self.show()

    def saveText(self):
        # pass
        s_txt = self.bell_text.toPlainText()
        f = open('soundtext.txt', 'w')
        f.write(s_txt)
        if s_txt:
            # print(s_txt)
            tts = gTTS(text=s_txt, lang='en', slow=False)
            tts.save("bell_text.mp3")
        f.close()
        self.hide()

    def loadText(self):
        # pass
        f = open('soundtext.txt', 'r')
        rt = f.read()
        self.bell_text.setText(rt)
        f.close()

    def exit(self):
        # pass
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.aboutToQuit.connect(app.deleteLater)
    ex = setSound()
    sys.exit(app.exec_())
