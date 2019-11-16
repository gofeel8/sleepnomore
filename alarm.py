#-*- coding:utf-8 -*-
import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QCheckBox, QTimeEdit, QSpinBox, QDial
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication, QTime, Qt, QTimer, QUrl, QDate, Qt
#from PyQt5.QtMultimedia import QSoundEffect
from alarmUI import Ui_Form
from timeBell import setTime
from sound import setSound
# from PyQt5.QtCore import QTime, QTimer
# from PyQt5.QtWidgets import QApplication, QLCDNumber


class Alarm(QWidget, Ui_Form):
    def __init__(self):
        super(QWidget,self).__init__()
        super(Ui_Form,self).__init__()
        self.setupUi(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.chk)
        self.timer.start()
        # self.showFullScreen()
        self.show()

    def chk(self):
        now = QTime.currentTime()
        time = now.toString('hh:mm')
        if (now.second() % 2) == 0:
            time = time[:2] + ' ' + time[3:]

        self.time.display(time)

        date = QDate.currentDate()
        self.date.setText(date.toString(Qt.DefaultLocaleLongDate))

    def showCamera(self):
        pass
        # t = time.localtime()
        # w = t.tm_wday+1
        # print(h.bell_text[w].text())

    def settingAlarm(self):
        h.show()

    def settingSound(self):
        s.showWindow()

    def closeEvent(self, QCloseEvent):
        ans = QMessageBox.question(self, "종료확인", "종료하시겠습니까",
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if ans == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    s = setSound()
    h = setTime()

    ex = Alarm()
    sys.exit(app.exec_())
