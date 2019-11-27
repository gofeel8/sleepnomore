#-*- coding:utf-8 -*-
import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QCheckBox, QTimeEdit, QSpinBox, QDial, QLineEdit, QRadioButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication, QTime, Qt, QTimer, QUrl
#from PyQt5.QtMultimedia import QSoundEffect

import os
# from PyQt5.QtCore import QTime, QTimer
# from PyQt5.QtWidgets import QApplication, QLCDNumber

import alarmyolo
from picamera import PiCamera

#camera = PiCamera()

class setTime(QWidget):
    def __init__(self):
        super(QWidget,self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(400, 400)
        # self.setGeometry(100, 100, 600, 620)
        self.setWindowTitle("알람 시간 설정")

        # self.lblNow = QLabel("", self)
        # self.lblNow.setFont(QFont("맑은 고딕", 25))
        # self.lblNow.setAlignment(Qt.AlignCenter)
        # self.lblNow.resize(350, 46)
        # self.lblNow.move(75, 60)

        self.day_txt = ["", "월", "화", "수", "목", "금", "토", "일"]
        self.day_chk = []
        self.day_chk.append(0)
        self.time_st = []
        self.time_st.append(0)
        # self.bell_text = []
        # self.bell_text.append(0)

        for r in range(1, 8):
            self.day_chk.append(QCheckBox(self.day_txt[r]+"요일", self))
            self.day_chk[r].move(20, 1+r*50)
            self.day_chk[r].setChecked(True)
            self.day_chk[r].setStyleSheet(
                "QCheckBox::indicator { width:20px; height: 20px; }"
                "QCheckBox {    spacing: 5px;    font-size:25px;  }")
            self.time_st.append(QTimeEdit(self))
            self.time_st[r].setDisplayFormat("hh:mm")
            self.time_st[r].setTime(QTime(9, 00))
            self.time_st[r].resize(100, 35)

            self.time_st[r].setStyleSheet(
                "QTimeEdit::up-button{ width:40px; }"
                "QTimeEdit::down-button{ width:40px; }")
            self.time_st[r].move(20+110, r*50)
            # self.bell_text.append(QLineEdit(self))
            # self.bell_text[r].setText("알람 텍스트를 입력하시오")
            # self.bell_text[r].move(20+110+110, 10+r*50)

        self.timer = QTimer()
        self.timer.timeout.connect(self.tChk)

#        self.bell = QSoundEffect()
        # self.bell.setSource(QUrl.fromLocalFile('bell_orginal.wav'))
        # self.bell.play()

        self.timer.start(100)

        self.okay = QPushButton(self)
        self.okay.setText("확인")
        self.okay.resize(80, 40)
        self.okay.move(280, 340)
        self.okay.clicked.connect(self.hide)

        self.basicBell = QRadioButton("기본벨 사용", self)
        self.basicBell.move(270, 260)
        self.basicBell.setChecked(True)

        self.customBell = QRadioButton("알람문구 사용", self)
        self.customBell.move(270, 290)

        # self.show()

    def tChk(self):
        t = time.localtime()
        # self.lblNow.setText("{}:{}:{}".format(t.tm_hour, t.tm_min, t.tm_sec))
        w = t.tm_wday+1
        # print(self.time_st[w].time().hour())
        # print(self.time_st[w].time().minute())
        # print(self.bell_text[w].text())
        # print(t.tm_hour)
        # print(t.tm_min)

        # print(self.basicBell.isChecked())

        if self.day_chk[w].isChecked() and self.time_st[w].time().hour() == t.tm_hour and t.tm_min == self.time_st[w].time().minute() and t.tm_sec == 0:
            for z in range (3):
		    os.system("sudo ./hub-ctrl -h 1 -P 2 -p 1")
		    if(alarmyolo.detect()):
			    self.play()
#  time.sleep(15)
	            os.system("sudo ./hub-ctrl -h 1 -P 2 -p 0")
	            time.sleep(10)


    def play(self):
        if self.basicBell.isChecked():
            print("기본벨 사용")
            os.system("omxplayer bell_orginal.mp3")
            #self.bell.setSource(QUrl.fromLocalFile('bell_orginal.wav'))
        elif self.customBell.isChecked():
	    for q in range(3):
                  os.system("mpg321 -g 350 bell_text.mp3")
		  time.sleep(2)
            #self.bell.setSource(QUrl.fromLocalFile('bell_text.mp3'))
            print("알람문구 사용")
#        self.bell.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.aboutToQuit.connect(app.deleteLater)
    ex = setTime()
    sys.exit(app.exec_())
