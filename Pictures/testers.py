

from PIL import Image
import pytesseract
import os



path = "/usr/local/home/eguerrer/PodLine/Pictures/"
firstString = "";
Ofile = open("TITLES.txt", "w")
list = os.listdir(path)
for im in list:
	if im.endswith('.png'):
		image = Image.open(im)
		text = pytesseract.image_to_string(image, lang = 'eng')
		title = text.partition("\n\n")[0]
		filteredText = "".join(i for i in title if ord(i) <128)
		# if firstString is empty 
		# set firstString to filtered text
		# and write to text
		# else if first string is not empty
		# compare the first String to filtered String
		# if it is the same then don't write to text
		# if it is not the same then do write it to the file
		# assign first String to filtered text
		firstString = Ofile.readline()
		for st in Ofile
			if firstString != filteredText
				inputPath = os.path.join(path, im)	
				Ofile.write("Next image:" + im)
				Ofile.write("\n")
				Ofile.write( "Next slide: " + filteredText)
				Ofile.write("\n")
				st = Ofile.readline()
Ofile.close()


		


