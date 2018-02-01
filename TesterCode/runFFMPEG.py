import subprocess
import os
from PIL import Image
import pytesseract

framesDestFolder = 'Podcast1Frames'
podcastVideoInput = 'test.mp4'
outputFrame = framesDestFolder + '/frame%03d.png'
path = "./" + framesDestFolder + "/"
outlineFilename = "TITLES.txt"

#subprocess.call(['mkdir', framesDestFolder])
#subprocess.call(['ffmpeg', '-i', podcastVideoInput, '-vf', 'fps=1/10', outputFrame])

frames = os.listdir(path)
frames.sort(key=str.lower)
Ofile = open(outlineFilename, 'w+')
#Ofile.write("Image Name \t\t Title \n")

print("OCRing") #debug
for frameName in frames:
	if frameName.endswith('.png'):
		frame = Image.open(path + frameName)
		text = pytesseract.image_to_string(frame, lang = 'eng')
		title = text.partition("\n")[0]
		title.replace("\n", " ") 
		print("Title1: " + title)		
		filteredTitle = "".join(i for i in title if ord(i) <128)
		#filteredTitle.replace("\n", " ") 
		print("Title2: " + filteredTitle)		
		
                #Do not write duplicate titles
                #firstString = Ofile.readline()
                duplicateFlag = 0
		Ofile.seek(0)
		for st in Ofile: #how to loop thru file line by line
	#		print("st: " + st)		
			if st == (filteredTitle + "\n"):
	#			print("DUPLICATE")		
				duplicateFlag = 1
				break
		if (duplicateFlag == 0):
			#Ofile.write(frameName + "\t\t")	
			Ofile.write(filteredTitle + "\n")
Ofile.close()
