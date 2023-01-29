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

print("Simula")
print("Nakikinig...")
bigkas("Magandang araw, Iskolar! Ano po ang maitutulong ko?")

salita = get_audio()

#WAKE_KEYWORD = ["saab", "sad", "sud", "sod", "sap", "sam", "sub"]
#for WAKE in WAKE_KEYWORD:
#    if WAKE in salita:
#        if salita.count(WAKE) > 0:
#            bigkas("Magandang araw iskolar! Ano po ang maitutulong ko?")

while True:
            print("Iniintindi...")
            salita = get_audio()
            
            #if 'kumusta' in salita or 'kamusta' in salita:
            #    bigkas("Magandang araw iskolar! Ano po ang maitutulong ko?")

            if 'request' in salita and 'document' in salita:
                bigkas("Scan ang QR code.")
                time.sleep(0.1)
                im = Image.open(r"AppointmentSystem.png")
                im.show()
                time.sleep(0.5)
                bigkas("Pagkatapos mag-log in, piliin ang 'Request Appointment' at ang 'Avail PUP Services'. Magtakda ng appointment sa 'Institute of Technology Registrar and Admission'. Maaaring maghintay na lamang ng dalawa hanggang tatlong araw upang maiproseso ang iyong dokumento. Maraming salamat.")
                continue

            if 'appointment' in salita:
                bigkas("Scan ang QR code.")
                time.sleep(0.1)
                im = Image.open(r"AppointmentSystem.png")
                im.show()
                time.sleep(0.5)
                bigkas("Pagkatapos mag-log in, piliin ang 'Request Appointment' at ang 'Avail PUP Services'. Magtakda ng appointment sa 'Institute of Technology Registrar and Admission'. Maaaring maghintay na lamang ng dalawa hanggang tatlong araw upang maiproseso ang iyong dokumento. Maraming salamat.")
                continue

            if 'completion' in salita and 'grades' in salita:
                bigkas("Scan ang QR code.")
                time.sleep(0.1)
                im = Image.open(r"Completion of Grades Form.png")
                im.show()
                time.sleep(0.5)
                bigkas("Maaaring mag-scan din sa QR code na ito para sa mga alituntunin na kailangang tandaan. Maraming salamat.")
                im = Image.open(r"CompletionofGrades.png")
                im.show()
                continue

            if 'add' in salita and 'subjects' in salita:
                bigkas("Scan ang QR code.")
                time.sleep(0.1)
                im = Image.open(r"ACEFormADD.png")
                im.show()
                time.sleep(0.5)
                bigkas("Maaaring sagutan ang ACE Form para sa pagdagdag ng mga asignatura. Maraming salamat.")
                continue

            if 'change' in salita and 'subjects' in salita:
                bigkas("Scan ang QR code.")
                time.sleep(0.1)
                im = Image.open(r"ACEFormCHANGE.png")
                im.show()
                time.sleep(0.5)
                bigkas("Maaaring sagutan ang ACE Form upang magbago ng ilang asignatura o ang schedule. Maraming salamat.")
                continue

            if 'withdrawal' in salita or 'withdraw' in salita:
                bigkas("Scan ang QR code.")
                time.sleep(0.1)
                im = Image.open(r"ACEFormWITHDRAWAL.png")
                im.show()
                time.sleep(0.5)
                bigkas("Maaaring sagutan ang ACE Form para sa pag-withdraw ng mga asignatura. Maraming salamat.")
                continue

            if 'leave' in salita and 'absence' in salita:
                bigkas("Maaaring gumawa ng narrative report tungkol sa iyong rason sa pag-file ng Leave of Absence. Ito ay dapat naka-address kay Engineer Ramir M Cruz, ang Dean. Ang narrative report ay dapat ibigay sa Dean at sa kinauukulang Chairperson ng Institute of Technology. Si Engineer Frescian C Ruiz ay ang Chairperson ng Engineering Technology at si Josephine M Dela Isla ang Chairperson ng Management Technology.")
                continue
                
            if 'student' in salita and 'payment' in salita:
                bigkas("Maaaring tumungo sa Accounting Office at hanapin si Evelyn Aseniero para sa transaksyon na ito.")
                bigkas("Pagkatapos makipagusap sa Accounting Officer, magbayad sa P.U.P Main Cashier at magpasa ng Original at isa photocopy ng P.U.P Official Receipt (O.R), Request Form, Certificate of Candidacy at General Clearance.")
                bigkas("Pagkatapos magbayad, scan ang QR code.")
                time.sleep(0.1)
                im = Image.open(r"StudentPayment.png")
                im.show()
                time.sleep(0.5)
                bigkas("Ilagay sa Student Payment form ang mga impormasyon na ito.")
                im = Image.open(r"Directions.png")
                im.show()
                continue
                
            if 'diploma' in salita or 'transcript' in salita and 'records' in salita:
                bigkas("Scan ang QR code.")
                time.sleep(0.1)
                im = Image.open(r"AppointmentSystem.png")
                im.show()
                time.sleep(0.5)
                bigkas("Pagkatapos mag-log in, piliin ang 'Request Appointment' at ang 'Avail P.U.P Services'. Magtakda ng appointment sa 'Institute of Technology Registrar and Admission' at hanapin ang kinakailangang dokumento. Maaaring maghintay na lamang ng dalawa hanggang tatlong araw upang maiproseso ang iyong dokumento. Maraming salamat.")
                continue
                
            if 'readmission' in salita or 're-admission' in salita:
                bigkas("Scan ang QR code.")
                im = Image.open(r"Readmission.png")
                im.show()
                time.sleep(0.5)
                bigkas("Mangyaring punan ang Aplikasyon para sa Readmission Form. Maabisuhan na ang mga estudyanteng tumigil sa pag-aaral ay maaari ang muling pagpasok depende sa kanilang nakaraang akademikong pagganap at availability ng slots.")
                bigkas("Ang nagbabalik na estudyante, maliban sa pagbayad ng readmission fee, ay dapat magsumite ng mga sumusunod na dokumento sa Admissions Office. Mangyaring scan ang QR code na ito.")
                time.sleep(0.1)
                im = Image.open(r"Readmission Req.png")
                im.show()
                time.sleep(0.5)
                bigkas("Para sa readmission procedures, maaaring scan ang susunod na QR code na ito.")
                im = Image.open(r"Readmission Procedure.png")
                im.show()
                continue

            if 'paalam' in salita:
                bigkas("Paalam. Maraming salamat.")
                sys.exit(0)

            else:
                time.sleep(1)
                print("Hindi kita maintindihan.")
