import os

def delete_textfile():
    if os.path.exists("/home/pi/Pictures/picture.jpg"):
        os.remove("/home/pi/Pictures/picture.jpg")
        print("Deleted file")
    else:
        print("The file does not exist") 

def delete_picture():
    if os.path.exists("/home/pi/Pictures/picture.jpg"):
        os.remove("/home/pi/Pictures/picture.jpg")
        print("Deleted picture")
    else:
        print("The picture does not exist")
