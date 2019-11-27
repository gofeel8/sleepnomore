from picamera import PiCamera
from subprocess import Popen, PIPE
import threading
from time import sleep
import os, fcntl
import cv2


#camera = PiCamera()
#iframe = 0
def detect():
#	os.system("sudo ./hub-ctrl -h 1 -P 2 -p 1")
#	camera = pi
	camera = PiCamera()
#Yolo v3 is a full convolutional model. It does not care the size of input image, as long as h and w are multiplication of 32

#camera.resolution = (160,160)
#camera.resolution = (416, 416)
#camera.resolution = (544, 544)
	camera.resolution = (608, 608)
#camera.resolution = (608, 288)


#camera.capture('frame.jpg')
#sleep(0.1)

#spawn darknet process
	yolo_proc = Popen(["./darknet",
			   "detector",
			   "test",
			   "obj.data",
			   "./yolov3-custom.cfg",
			   "./yolov3-custom.weights",
			   "-thresh","0.1"],
			   stdin = PIPE, stdout = PIPE)

	fcntl.fcntl(yolo_proc.stdout.fileno(), fcntl.F_SETFL, os.O_NONBLOCK)

	cnt = 0
	print("cnt : " +str(cnt))
	tf = 0 
	print("tf : "+ str(tf))

	while True:
	    try:
		stdout = yolo_proc.stdout.read()
		if 'Enter Image Path' in stdout:
#		    try:
#		       im = cv2.imread('predictions.png')
##		       print(im.shape)
#		       cv2.imshow('record',im)
#		       key = cv2.waitKey(5) 
#		    except Exception:
#		       pass
		    camera.capture('frame.jpg')
		    yolo_proc.stdin.write('frame.jpg\n')
		if len(stdout.strip())>0:
		    print('start get %s end' % stdout)
		    if(stdout.find("sleep") != -1):
			    print("find sleeping person")
			    tf += 1
			    print(tf)
			    if tf == 1 :
			       print("wake up")
			       yolo_proc.kill()
                               camera.close()
#	                       os.system("sudo ./hub-ctrl -h 1 -P 2 -p 0")
			       return True
		    cnt += 1
		    print("count : " + str(cnt))
		    if cnt == 2:
		        print("False")
		        camera.close()
			yolo_proc.kill()
#			os.system("sudo ./hub-ctrl -h 1 -P 2 -p 0")
			return False
	    except Exception:
		pass

#print(detect())
