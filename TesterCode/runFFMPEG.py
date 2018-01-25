import subprocess
import os

os.chdir('/usr/local/home/efarkas/PodLine/Pods/')
#subprocess.call(['ffmpeg', '-i', 'picture%d0.png', 'output.avi'])
#subprocess.call(['ffmpeg', '-i', 'output.avi', '-t', '5', 'out.gif'])
subprocess.call(['ffmpeg', '-i', 'test.mp4', '-vf', 'transpose=2', 'testrotate.mp4'])

