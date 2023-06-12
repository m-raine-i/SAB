import json
import os
import random
import string
import time
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

def load_queries(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for _ in range(length))
    return result_str

def bigkas(args):
    tts = gTTS(text=args, lang='tl')
    random_string = get_random_string(4).lower()
    audio_file = os.path.dirname(random_string) + random_string + '-audio.mp3'
    tts.save(audio_file)
    playsound(audio_file)
    print(args)
    os.remove(audio_file)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, phrase_time_limit=3)
        said = ""

        try:
            said = r.recognize_google(audio, language='tl')
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()

print("Simula")
print("Nakikinig...")
bigkas("Magandang araw Iskolar! Ano ang maitutulong ko?")
salita = get_audio()

queries = load_queries("test\queries tagalog.json")

running = True
while running:
    print("Iniintindi...")
    salita = get_audio()

    found = False
    for item in queries:
        if all(word in salita for word in item["query"].split()):
            found = True
            if item.get("qr_code_path"):
                bigkas(item["response"])
                time.sleep(0.2)
                url = item["qr_code_path"]
                os.startfile(url)
                time.sleep(0.5)
            else:
                bigkas(item["response"])
            break

    if not found:
        bigkas("Hindi kita maintindihan.")

    if any(word in salita for word in ["quit", "exit", "bye"]):
        bigkas("Paalam!")
        running = False