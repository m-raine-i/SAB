from fileinput import close
from gtts import gTTS
from playsound import playsound
import random
import os
import speech_recognition as sr
import string
import time

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
print("nakikinig...")
salita = get_audio()

WAKE_KEYWORD = ["saab", "sad", "sud", "sod", "sap", "sam"]
for WAKE in WAKE_KEYWORD:
    if WAKE in salita:
        if salita.count(WAKE) > 0:
            bigkas("Magandang araw iskolar! Ano po ang maitutulong ko?")

    while True:
                print("iniintindi...")
                salita = get_audio()

                if 'request' in salita and 'document' in salita:
                    bigkas("Scan ang QR code.")
                    time.sleep(0.5)
                    url = 'Appointment System.png'
                    os.startfile(url)
                    time.sleep(0.5)
                    bigkas("Pagkatapos mag-log in, piliin ang 'Request Appointment' at ang 'Avail PUP Services'. Magtakda ng appointment sa 'Institute of Technology Registrar and Admission'. Maaaring maghintay na lamang ng dalawa hanggang tatlong araw upang maiproseso ang iyong dokumento. Maraming salamat.")
                    continue

                if 'appointment' in salita:
                    bigkas("Scan ang QR code.")
                    time.sleep(0.5)
                    url = 'Appointment System.png'
                    os.startfile(url)
                    time.sleep(0.5)
                    bigkas("Pagkatapos mag-log in, piliin ang 'Request Appointment' at ang 'Avail PUP Services'. Magtakda ng appointment sa 'Institute of Technology Registrar and Admission'. Maaaring maghintay na lamang ng dalawa hanggang tatlong araw upang maiproseso ang iyong dokumento. Maraming salamat.")
                    continue

                if 'completion' in salita and 'grades' in salita:
                    bigkas("Scan ang QR code.")
                    time.sleep(0.5)
                    url = 'Completion of Grades Form.png'
                    os.startfile(url)
                    time.sleep(0.5)
                    bigkas("Maaaring mag-scan din sa QR code na ito para sa mga alituntunin na kailangang tandaan. Maraming salamat.")
                    url = 'Completion of Grades.png'
                    os.startfile(url)
                    continue

                if 'ace' in salita and 'add' in salita and 'subject' in salita:
                    bigkas("Scan ang QR code.")
                    time.sleep(0.5)
                    url = 'ACE Form ADD.png'
                    os.startfile(url)
                    time.sleep(0.5)
                    bigkas("Maaaring sagutan ang ACE Form para sa pagdagdag ng mga asignatura. Maraming salamat.")
                    continue

                if 'ace' in salita and 'change' in salita and 'subject' in salita:
                    bigkas("Scan ang QR code.")
                    time.sleep(0.5)
                    url = 'ACE Form CHANGE.png'
                    os.startfile(url)
                    time.sleep(0.5)
                    bigkas("Maaaring sagutan ang ACE Form upang magbago ng ilang asignatura o ang schedule. Maraming salamat.")
                    continue

                if 'ace' in salita and 'withdrawal' in salita or 'withdraw' in salita:
                    bigkas("Scan ang QR code.")
                    time.sleep(0.5)
                    url = 'ACE Form WITHDRAWAL.png'
                    os.startfile(url)
                    time.sleep(0.5)
                    bigkas("Maaaring sagutan ang ACE Form para sa pag-withdraw ng mga asignatura. Maraming salamat.")
                    continue

                if 'leave' in salita and 'absence' in salita:
                    bigkas("Maaaring gumawa ng narrative report tungkol sa iyong rason sa pag-file ng Leave of Absence. Ito ay dapat naka-address kay Engineer Ramir M Cruz, ang Dean. Ang narrative report ay dapat ibigay sa Dean at sa kinauukulang Chairperson ng Institute of Technology. Si Engineer Frescian C Ruiz ay ang Chairperson ng Engineering Technology at si Josephine M Dela Isla ang Chairperson ng Management Technology.")
                    continue

                else:
                    bigkas('Di kita maintindihan')
