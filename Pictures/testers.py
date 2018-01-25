

from PIL import Image
import pytesseract
import os



path = "/usr/local/home/eguerrer/PodLine/Pictures/"


list = os.listdir(path)
for im in list:
	if im.endswith('.png'):
		image = Image.open(im)
		text = pytesseract.image_to_string(image, lang = 'eng')
		title = text.partition("\n\n")[0]
		filteredText = "".join(i for i in title if ord(i) <128)
		inputPath = os.path.join(path, im)	
		print("Next image: " +  im)	
		print( "Next slide: " + filteredText)
		print("\n")


