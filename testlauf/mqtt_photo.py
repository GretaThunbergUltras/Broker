!/usr/bin/env python

from picamera import PiCamera
from time import sleep

def take_picture():
	camera = PiCamera()
	camera.start_preview()
	#time to focus
	sleep(5)
	#save as
	camera.capture('/home/pi/Pictures/picture.jpg')
	camera.stop_preview()
	print("Image captured")

