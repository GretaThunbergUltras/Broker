# -*- coding: utf-8 -*-

import base64
from PIL import Image
from io import BytesIO


f = open('test.txt', 'r')
data = f.read()
f.closed


im = Image.open(BytesIO(base64.b64decode(data)))
im.save('newimage.jpg', 'JPEG')

print("decoded to jpg...")


