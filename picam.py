#-*- coding:utf-8 -*-
from picamera import PiCamera,Color
from time import sleep
import os

def show():
	camera = PiCamera()
	gps = "5sec"
	camera.hflip = True
#camera.brightness = 50
	os.system("sudo ./hub-ctrl -h 1 -P 2 -p 1")
	camera.start_preview()
	camera.annotate_background = Color('red')
	camera.annotate_foreground = Color('white')
	camera.annotate_text = gps
	sleep(5)
	camera.stop_preview()
	os.system("sudo ./hub-ctrl -h 1 -P 2 -p 0")
	camera.close()


#show()
