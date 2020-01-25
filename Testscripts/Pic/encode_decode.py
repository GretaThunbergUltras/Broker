import base64


# encode to base64
with open("test.jpg", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print(str)

# decode to jpg
fh = open("imageToSave.jpg", "wb")
fh.write(str.decode('base64'))
fh.close()
