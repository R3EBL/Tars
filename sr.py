import speech_recognition as sr
import sys

def speech(outputfile):
    r = sr.Recognizer()
    
    with open(outputfile, 'w') as f:
        with sr.Microphone() as source:
            print("Talk now...")
            r.adjust_for_ambient_noise(source)
            audio_text = r.listen(source, timeout=10) 
            print("Time over, thanks")

            try: 
                audio = r.recognize_google(audio_text)
                print(f"Recognized speech: {audio}")
                f.write(audio)  
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand the audio")
                sys.exit(1)
            except sr.RequestError as e:
                print(f"Error with the API request: {e}")
                sys.exit(1)


