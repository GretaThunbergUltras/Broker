# -*- coding: utf-8 -*-
import base64

#convert pic into base64
encoded = base64.b64encode(open("test.jpg", "rb").read())


#write pic.base64 into txt
file = open("test.txt","w")
file.write(repr(encoded))
file.close()

print("encoded to b64...")
