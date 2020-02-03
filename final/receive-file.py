import base64
import time
from botlib.broker import Broker

def callback(cid, userdata, msg):
    anzahl = open("number.txt").read()
    type(anzahl)
    nummer=int(anzahl)
    nummer=nummer+1
    numberOfPic= str(nummer)

    file=open("number.txt","w")
    file.write(numberOfPic)
    file.close()
    with open('/media/extern/Images/image'+ numberOfPic +'.jpeg', 'wb') as out:
        out.write(base64.b64decode(msg.payload))
        print("Image" +numberOfPic +" saved")

subs = {
    'test_channel': callback
}

b = Broker('jockel', subscriptions=subs)

while True:
    time.sleep(1)
