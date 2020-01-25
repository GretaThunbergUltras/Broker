import base64
from PIL import Image
from io import BytesIO

f = open('test.txt', 'r')
data = f.read()
print(data)
f.closed 

# Soweit so gut
# Daten werden eingelesen und ab Var übergeben 

im = Image.open(BytesIO(base64.b64decode(data))) # Ich verstehe auch die Errormeldung nicht weil eig müsste die fkt funktionieren 


im.save('newimage.jpg', 'JPEG')
