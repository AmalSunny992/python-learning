from gtts import gTTS
from tkinter import *
import os
#text = "Today is a Good day"
text = open('demo.txt','r').read()
output = gTTS(text=text,lang='en',slow=False)
output.save('fileout.mp3')
os.system('start fileout.mp3')