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
print("Listening...")
speak("Good day! How may I help you?")
salita = get_audio()

WAKE_KEYWORD = ["saab", "sad", "sud", "sod", "sap", "sam"]
for WAKE in WAKE_KEYWORD:
    if WAKE in salita:
        if salita.count(WAKE) > 0:
            speak("Good day! How may I help you?")

    while True:
                print("Understanding....")
                salita = get_audio()

                if 'request' in salita and 'documents' in salita:
                    speak("Please scan the QR code.")
                    time.sleep(0.2)
                    url = 'Appointment System.png'
                    os.startfile(url)
                    time.sleep(0.5)
                    speak("After logging in, choose the 'Request Appointment' and 'Avail P.U.P Services'. Set an appointment to the 'Institute of Technology Registrar and Admission'. After setting an appointment, please wait for two to three days to process your documents. Thank you.")
                    continue

                if 'appointment' in salita:
                    speak("Please scan the QR code.")
                    time.sleep(0.2)
                    url = 'Appointment System.png'
                    os.startfile(url)
                    time.sleep(0.5)
                    speak("After logging in, choose the 'Request Appointment' and 'Avail P.U.P Services'. Set an appointment to the 'Institute of Technology Registrar and Admission'. After setting an appointment, please wait for two to three days to process your documents. Thank you.")
                    continue

                if 'completion' in salita and 'grades' in salita:
                    speak("Please scan the QR code.")
                    time.sleep(0.2)
                    url = 'Completion of Grades Form.png'
                    os.startfile(url)
                    time.sleep(0.5)
                    speak("You may scan this QR code and take note of all the guidelines to follow. Thank you.")
                    continue

                if 'ace' in salita and 'add' in salita and 'subject' in salita:
                    speak("Please scan the QR code.")
                    time.sleep(0.2)
                    url = 'ACE Form ADD.png'
                    os.startfile(url)
                    time.sleep(0.5)
                    speak("You may answer this form by filling out the subjects that you need to add during the adjustment period. Thank you.")
                    continue

                if 'ace' in salita and 'change' in salita and 'subject' in salita:
                    speak("Please scan the QR code.")
                    time.sleep(0.2)
                    url = 'ACE Form CHANGE.png'
                    os.startfile(url)
                    time.sleep(0.5)
                    speak("You may answer this form by filling out the subjects that you need to change during the adjustment period. Thank you.")
                    continue

                if 'ace' in salita and 'withdrawal' in salita or 'withdraw' in salita:
                    speak("Please scan the QR code.")
                    time.sleep(0.2)
                    url = 'ACE Form WITHDRAWAL.png'
                    os.startfile(url)
                    time.sleep(0.5)
                    speak("You may answer this form by filling out the subjects that you want to withdaw during the adjustment period. Thank you.")
                    continue

                if 'leave' in salita and 'absence' in salita:
                    speak("You may write a narrative report about your reason on why you are filling a Leave of Absence. Your report should be addressed to the Dean, Engineer Ramir M Cruz. You may submit your narrative report to the Dean and to your respective Chairperson. Engineer Frescian C Ruiz is the Chairperson of the Engineering Technology while Josephine M Dela Isla is the Chairperson of the Management Technology. Thank you.")
                    continue

                else:
                    print('I cannot understand you.')