import paho.mqtt.publish as publish
import time 

MQTT_SERVER = "localhost"
MQTT_PATH = "test_channel"

const_str_date = "Date: "
var_time = time.strftime("%d.%m.%Y %H:%M:%S")

publish.single(MQTT_PATH,const_str_date + var_time, hostname=MQTT_SERVER)

print("DONE")

