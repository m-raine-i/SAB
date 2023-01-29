from fileinput import close
from gtts import gTTS
from playsound import playsound
from PIL import Image
import random
import os, sys, subprocess
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

# WAKE_KEYWORD = ["saab", "sad", "sud", "sod", "sap", "sam"]
# for WAKE in WAKE_KEYWORD:
#    if WAKE in salita:
#        if salita.count(WAKE) > 0:
#            speak("Good day! How may I help you?")

while True:
            print("Understanding....")
            salita = get_audio()

            if 'request' in salita and 'documents' in salita:
                speak("Please scan the QR code.")
                time.sleep(0.1)
                im = Image.open(r"AppointmentSystem.png")
                im.show()
                time.sleep(0.5)
                speak("After logging in, choose the 'Request Appointment' and 'Avail P.U.P Services'. Set an appointment to the 'Institute of Technology Registrar and Admission'. After setting an appointment, please wait for two to three days to process your documents. Thank you.")
                continue

            if 'appointment' in salita:
                speak("Please scan the QR code.")
                time.sleep(0.1)
                im = Image.open(r"AppointmentSystem.png")
                im.show()
                time.sleep(0.5)
                speak("After logging in, choose the 'Request Appointment' and 'Avail P.U.P Services'. Set an appointment to the 'Institute of Technology Registrar and Admission'. After setting an appointment, please wait for two to three days to process your documents. Thank you.")
                continue

            if 'completion' in salita and 'grades' in salita:
                speak("Please scan the QR code.")
                time.sleep(0.1)
                im = Image.open(r"Completion of Grades Form.png")
                im.show()
                time.sleep(0.5)
                speak("You may scan this QR code and take note of all the guidelines to follow. Thank you.")
                im = Image.open(r"CompletionofGrades.png")
                im.show()
                continue

            if 'ace' in salita and 'add' in salita and 'subject' in salita:
                speak("Please scan the QR code.")
                time.sleep(0.1)
                im = Image.open(r"ACEFormADD.png")
                im.show()
                time.sleep(0.5)
                speak("You may answer this form by filling out the subjects that you need to add during the adjustment period. Thank you.")
                continue

            if 'ace' in salita and 'change' in salita and 'subject' in salita:
                speak("Please scan the QR code.")
                time.sleep(0.1)
                im = Image.open(r"ACEFormCHANGE.png")
                im.show()
                time.sleep(0.5)
                speak("You may answer this form by filling out the subjects that you need to change during the adjustment period. Thank you.")
                continue

            if 'ace' in salita and 'withdrawal' in salita or 'withdraw' in salita:
                speak("Please scan the QR code.")
                time.sleep(0.1)
                im = Image.open(r"ACEFormWITHDRAWAL.png")
                im.show()
                time.sleep(0.5)
                speak("You may answer this form by filling out the subjects that you want to withdaw during the adjustment period. Thank you.")
                continue

            if 'leave' in salita and 'absence' in salita:
                speak("You may write a narrative report about your reason on why you are filling a Leave of Absence. Your report should be addressed to the Dean, Engineer Ramir M Cruz. You may submit your narrative report to the Dean and to your respective Chairperson. Engineer Frescian C Ruiz is the Chairperson of the Engineering Technology while Josephine M Dela Isla is the Chairperson of the Management Technology. Thank you.")
                continue
                
            if 'student' in salita and 'payment' in salita:
                speak("You may visit the Accounting Office and look for Evelyn Aseniero for this kind of transaction.")
                speak("After talking to the Accounting Officer, you may pay at the P.U.P Main Cashier and pass all the requirements: Original and one photocopy of the P.U.P Official Receipt (O.R), Request Form, Certificate of Candidacy and General Clearance.")
                speak("After paying, you may scan this QR code.")
                time.sleep(0.1)
                im = Image.open(r"StudentPayment.png")
                im.show()
                time.sleep(0.5)
                speak("Fill out the Student Payment form with these information provided in the QR code.")
                im = Image.open(r"Directions.png")
                im.show()
                continue
                
            if 'diploma' in salita or 'transcript' in salita and 'records' in salita:
                speak("Please scan the QR code.")
                time.sleep(0.1)
                im = Image.open(r"AppointmentSystem.png")
                im.show()
                time.sleep(0.5)
                speak("After logging in, choose the options: 'Request Appointment' and 'Avail P.U.P Services'. Set an appointment to 'Institute of Technology Registrar and Admission' and request for the document that you need. After requesting, please wait for two to three days to process your documents. Thank you.")
                continue
                
            if 'readmission' in salita or 're-admission' in salita:
                speak("Please scan this QR code.")
                im = Image.open(r"Readmission.png")
                im.show()
                time.sleep(0.5)
                speak("Please fill in the Application for Re-admission Form. Be informed that students whose studies in P.U.P were discontinued for a period of time may be considered for re-admission depending on their previous academic performance and availability of slots.")
                speak("The returning student, in addition to paying the re-admission fee, shall submit the following documents to the Admissions Office. Please scan this QR code for the additional requirements.")
                time.sleep(0.1)
                im = Image.open(r"Readmission Req.png")
                im.show()
                time.sleep(0.5)
                speak("For the readmission procedures, please scan this next QR code.")
                im = Image.open(r"Readmission Procedure.png")
                im.show()
                continue
                
            if 'bye' in salita or 'goodbye' in salita:
                speak("Goodbye. Thank you.")
                sys.exit(0)

            else:
                print("I cannot understand you.")
