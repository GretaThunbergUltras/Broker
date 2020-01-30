# -*- coding: utf-8 -*-

import base64
from PIL import Image
from io import BytesIO

def convert_to_jpg():
    f = open('test.txt', 'r')
    data = f.read()
    f.closed

def save_to_jpg():
    im = Image.open(BytesIO(base64.b64decode(data)))
    im.save('newimage.jpg', 'JPEG')

    print("decoded to jpg...")
