import paho.mqtt.publish as publish
import time
from picamera import PiCamera
from time import sleep
from io import BytesIO
from botlib.broker import Broker

MQTT_SERVER = "localhost"
MQTT_PATH = "test_channel"

#const_str_date = "Date: "
#var_time = time.strftime("%d.%m.%Y %H:%M:%S")
#publish.single(MQTT_PATH,const_str_date + var_time, hostname=MQTT_SERVER)
#!/usr/bin/env python



camera = PiCamera()
camera.start_preview()
#time to focus
sleep(5)

broker = Broker('guenter')
buff=BytesIO()
camera.capture(buff, format = 'jpeg')
buff.seek(0)
broker.send_file(MQTT_PATH, buff.read())
camera.stop_preview()
print("Image captured")
print("DONE")

