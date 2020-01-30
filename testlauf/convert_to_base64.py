import base64

def convert_to_base64():
    #convert pic into base64
    with open("test.jpg", "rb") as f:
        encoded = base64.b64encode(f.read())
    print("converted to base64")
    return encoded

def save_to_textfile(encoded):
    #write pic.base64 into txt
    with open("test.txt","w") as f:
        f.write(repr(encoded))
