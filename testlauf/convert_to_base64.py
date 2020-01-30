import base64

def convert_to_base64():
	#convert pic into base64
	encoded = base64.b64encode(open("test.jpg", "rb").read())
	print("convertet to base64")

def save_to_textfile():
	#write pic.base64 into txt
	file = open("test.txt","w")
	file.write(repr(encoded))
	file.close()
