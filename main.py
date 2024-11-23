
import tts,sr,os,sys,subprocess

data = "data.txt"
ai_res= "ai_res.txt"



# fucked it * sigh * , rewrite it for realtime ai tts
def LaamaSearch(data,ai_res):
    with open(data,'r') as read_file:
        queries = read_file.read().strip()

    with open(ai_res,'w') as output_file:
        # This fucked the program!
        result = subprocess.Popen(
            ["ollama", "run", "llama3.2:3b", queries],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode==0:
            output_file.write(result.stdout)
        else:
            sys.exit(1)

os.system('clear')
print("\t RUNNING SPEECH RECOGNITION\n")
print("Please speak--------->\n")

sr.speech(data)
LaamaSearch(data,ai_res)
tts.TTS(ai_res)


