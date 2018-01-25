

from PIL import Image
import pytesseract
import os



path = "/usr/local/home/eguerrer/pictures/pictester"


list = os.listdir(path)
for im in list:
	if im.endswith('.png'):
		image = Image.open(im)
		text = pytesseract.image_to_string(image, lang = 'eng')
		title = text.partition("\n\n")[0]
		inputPath = os.path.join(path, im)
		#writer = open("output.txt", "r+")				
		print("Next image: " +  im)	
		#writer.write("Next image: " +  im)	
		#writer.write("\n")
	#	print("\n")
		#writer.write( "Next slide: " + title)

		print( "Next slide: " + title)
		#writer.write("\n")

		print("\n")

#writer.close()
