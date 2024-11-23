from gtts import gTTS

import os,sys

def TTS(inputfile):
    f = open(inputfile,'r')
    text = f.read()
    tts = gTTS(text,lang='en',tld="co.in",slow=False)
    f.close()
    tts.save("output.mp3")
    os.system("mpv output.mp3")
    os.system(f" rm {inputfile} ") 
