#!/usr/bin/env python

from picamera import PiCamera
from time import sleep
import time

def stopwatch(seconds):
    start = time.time()
    time.clock()    
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        print("%2d" %  (elapsed + 1))
        time.sleep(1) 
    
    

camera = PiCamera()
camera.start_preview()
#time to focus
stopwatch(4)

#save as
camera.capture('/home/pi/Pictures/picture.jpg')
camera.stop_preview()
print(">> Image captured")

