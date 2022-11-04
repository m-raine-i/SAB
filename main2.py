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

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, phrase_time_limit = 3)
        said = ""

        try:
            said = r.recognize_google(audio, language='tl')
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()


print("Start")

while True:
    print("nakikinig...")
    salita = get_audio()

    WAKE_KEYWORD = ["saab", "sad", "sud", "sod", "sap"]
    for WAKE in WAKE_KEYWORD:
        if WAKE in salita:
            if salita.count(WAKE) > 0:
                bigkas("Magandang araw iskolar! Ano po ang maitutulong ko?") #can be replaced by LED lighting up w/ a 'ping(?)' sound
                print("iniintindi...")
                salita = get_audio()

                """if 'kamusta' in salita and 'ka' in salita:
                    bigkas('Magandang araw! Ako po ay nasa mabuting kalagayan. Ano po ang maitutulong ko sa inyo ngayon?')
                    continue

                if 'how' in salita and 'you' in salita:
                    speak('Good day! I am fine. How may I help you today?')
                    continue"""

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

                else:
                    bigkas('Di kita maintindihan')


                #di pala pwede ito, magiging random at iisa lang ang response XD,
                #gawa ako iba for experimental purposes
                """KAMUSTA_STRS = ["kamusta ka", "how are you", "kamusta"]
                for phrase in CALENDAR_STRS:
                    if phrase in text:
                        date = get_date(text)
                        if date:
                            get_events(date, SERVICE)
                        else:
                            speak("I don't understand")

                NOTE_STRS = ["make a note", "write this down", "remember this"]
                for phrase in NOTE_STRS:
                    if phrase in text:
                        speak("What would you like me to write down?")
                        note_text = get_audio()
                        note(note_text)
                        speak("I've made a note of that.")"""
