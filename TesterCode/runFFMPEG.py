import subprocess
import os
from PIL import Image
import pytesseract

#subprocess.call(['mkdir', 'Podcast1Frames'])
#subprocess.call(['ffmpeg', '-i', 'test.mp4', '-vf', 'fps=1/10', 'Podcast1Frames/frame%03d.png'])

path = "./Podcast1Frames/"
#os.chdir('/usr/local/home/efarkas/PodLine/TesterCode/Podcast1Frames')

frames = os.listdir(path)
frames.sort(key=str.lower)
Ofile = open("TITLES.txt", "w")
#Ofile.write("Image Name \t\t Title \n")
print("OCRing") #debug
for im in frames:
	if im.endswith('.png'):
		image = Image.open(path + im)
		text = pytesseract.image_to_string(image, lang = 'eng')
		title = text.partition("\n\n")[0]
		filteredText = "".join(i for i in title if ord(i) <128)
		inputPath = os.path.join(path, im)	
		#Ofile.write(im + "\t\t")	
		Ofile.write(filteredText + "\n")

