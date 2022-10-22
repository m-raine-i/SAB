from fileinput import close
from gtts import gTTS 
from playsound import playsound 
import random
import os
import speech_recognition as sr
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def speak(args):
    tts=gTTS(text=args, lang='en-US')
    random_string=get_random_string(4).lower()
    audio_file=os.path.dirname(random_string)+random_string+'-audio.mp3'
    tts.save(audio_file)
    playsound(audio_file)
    print(args)
    os.remove(audio_file)

def bigkas(args):
    tts=gTTS(text=args, lang='tl')
    random_string=get_random_string(4).lower()
    audio_file=os.path.dirname(random_string)+random_string+'-audio.mp3'
    tts.save(audio_file)
    playsound(audio_file)
    print(args)
    os.remove(audio_file)
    
while True:
    with sr.Microphone() as source:
        print('nakikinig')
        audio=sr.Recognizer().listen(source)

        try:
            print('iniintindi')
            qwery=sr.Recognizer().recognize_google(audio, language='tl')
            salita=str(qwery).lower()

            if 'kamusta' in salita and 'ka' in salita:
                bigkas('Magandang araw! Ako po ay nasa mabuting kalagayan. Ano po ang maitutulong ko sa inyo ngayon?')
                continue
            
            if 'how' in salita and 'you' in salita:
                speak('Good day! I am fine. How may I help you today?')

            if 'ano' in salita and 'pangalan' in salita:
                bigkas('Ako po ang Student Assistant Bot o si SAB.')
                continue

            if 'what' in salita and 'name' in salita:
                speak('I am the Student Assistant Bot or you can call me SAB for short.')
                continue

            if 'saan' in salita and 'opisina' in salita:
                bigkas('Sa ikatlong palapag ng gusali.')
                continue

            if 'where' in salita and 'office' in salita:
                speak("You can find the Registrar's office at the third floor of this building.")
                continue

            if 'maraming' in salita or 'salamat' in salita:
                bigkas('Walang anuman!')
                continue

            if 'thank' in salita and 'you' in salita:
                speak('No problem!')
                continue

        except Exception as e:
            print(e)
            continue