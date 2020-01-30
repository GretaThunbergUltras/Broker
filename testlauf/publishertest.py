#!/usr/bin/env python

from picamera import PiCamera
from time import sleep
import base64
from mqtt_photo import *
from convert_to_base64 import *
from send_file import *
from mqtt_delete import *
import os

take_picture()
encoded = convert_to_base64()
save_to_textfile(encoded)
send_textfile()
delete_textfile()
delete_picture()
