import subprocess
import os
from PIL import Image
import pytesseract
import datetime

#User Inputs
podcastVideoInput = 'ShortPodcast.mp4'
frameFreq = '10' #save frame every _ seconds

#File/Folder Destination Generation based on User Inputs
podcastName = podcastVideoInput.split('.')[0]
framesDestFolder = podcastName + 'Frames'
outlineFilename = podcastName + "Outline.txt"
outputFrame = framesDestFolder + '/frame%03d.png'
framesPath = "./" + framesDestFolder + "/"
subprocess.call(['mkdir', framesDestFolder])

#Call FFMPEG to save frames every frameFreq seconds in framesDestFolder
subprocess.call(['ffmpeg', '-i', podcastVideoInput, '-vf', 'fps=1/'+frameFreq, outputFrame])

#Sort frames in alphabetical order so they will be read chronologically
frames = os.listdir(framesPath)
frames.sort(key=str.lower)

#Open output file for reading and writing.  Create file if doesn't exist.
Ofile = open(outlineFilename, 'w+')

#Loop through 
print("OCRing") #debug
time = 0
for frameName in frames:
	if frameName.endswith('.png'):
		frame = Image.open(framesPath + frameName)
		text = pytesseract.image_to_string(frame, lang = 'eng')
		title = text.partition("\n")[0]
		title.replace("\n", " ") 
		filteredTitle = "".join(i for i in title if ord(i) <128)	
		
                #Do not write duplicate titles
                duplicateFlag = 0
		Ofile.seek(0)
		for st in Ofile: #how to loop thru file line by line
			prevTitle = st.split('\t')[1] #get title; ignore timestamp
			if prevTitle == (filteredTitle + "\n"):
				duplicateFlag = 1
				break
		if (duplicateFlag == 0):
			timestamp = str(datetime.timedelta(seconds=time))
			Ofile.write(timestamp + '\t' + filteredTitle + "\n")
			#Ofile.write(filteredTitle + "\n")
		time = time + int(frameFreq)
Ofile.close()
