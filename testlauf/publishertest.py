#!/usr/bin/env python

from picamera import PiCamera
from time import sleep
import base64
import mqtt_photo
import convert_to_base64
import send_file
import mqtt_delete
import os

take_picture()
convert_to_base64()
save_to_textfile()
send_textfile()
delete_textfile()
delete_picture()





