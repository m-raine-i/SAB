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

            if 'Document' in salita or 'Form' in salita:
                speak('this is your QR code')
                continue

        except Exception as e:
            print(e)
            continue