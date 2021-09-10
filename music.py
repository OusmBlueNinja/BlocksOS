import playsound
from playsound import playsound

while True:


    print("type the sone name in here after you moves the audio file into the folder containing the main.py file")
    print("SONG WILL PLAY TO END AND YOU CANT STOP IT")
    text = input("song name (exa: music2.mp3)~ ")
    playsound(text)
    if input("play again (yes | no)") == "no":
        break
    else:
        print("playing ", text)
        continue
    
    