import os
if os.path.exists("/home/pi/Pictures/picture.jpg"):
  os.remove("/home/pi/Pictures/picture.jpg")
  print("Deleted file")
else:
  print("The file does not exist") 

