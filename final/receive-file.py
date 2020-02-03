import base64
import time

from botlib.broker import Broker


def callback(cid, userdata, msg, ):
    print('received something')
    #print(str(msg.payload))
    try:
        with open('image.jpeg', 'wb') as out:
            print("Image saved")
            temp = str(msg.payload)[2:-1]
            print("Image saved "+str(len(temp)))
            temp2 = base64.b64decode(temp)
            print("Image saved")
            out.write(temp2)
            print("Image saved")
    except Exception as e:
        print("fail")
        print(e)

subs = {
    'test_channel': callback
}

b = Broker('jockel', host='gruppe11', subscriptions=subs)

while True:
    time.sleep(1)

