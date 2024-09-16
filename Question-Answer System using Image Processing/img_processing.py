import pytesseract as tess
import PIL

myconfig = r"--psm 8 --oem 3"
def img_to_string(img):    
    text = tess.image_to_string(PIL.Image.open(img), config = myconfig)
    return text