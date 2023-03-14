from ast import Import
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random
import json
import pickle

from fileinput import close
from gtts import gTTS
from playsound import playsound
import PIL.Image
import os, sys, subprocess
import speech_recognition as sr
import string
import time

import warnings

import tkinter 
from tkinter import *

# Ignore any warning messages
warnings.filterwarnings('ignore')

#put full path below if file itself can't be detected; has to be in same folder w/ main3.py
with open(r"..\SAB (AI Assistant)\json_files\fil_intents.json") as file:
    data = json.load(file)

try:
    with open("..\\SAB (AI Assistant)\\bot\\fil\\fil_data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:

    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

            if intent["tag"] not in labels:
                labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

        with open("..\\SAB (AI Assistant)\\bot\\fil\\fil_data.pickle", "wb") as f:
            pickle.dump((words, labels, training, output), f)


    training = numpy.array(training)
    output = numpy.array(output)

tensorflow.compat.v1.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

try:
    model.load("..\\SAB (AI Assistant)\\bot\\fil\\fil_model.tflearn")
except:
    model = tflearn.DNN(net) #####
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("..\\SAB (AI Assistant)\\bot\\fil\\fil_model.tflearn")

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)


#==========VOICE FIL===============
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



def fil_voice():
    print("Nagsisimula...")
    print("Handa na ang bot!")
    bigkas("Magandang araw! Ano ang maitutulong ko sayo?")


    while True:
        print("Iniintindi.....")
        salita = get_audio()
        if salita == "quit": 
            break 

        results = model.predict([bag_of_words(salita, words)])
        results_index = numpy.argmax(results)
        tag = labels[results_index]

        if results[0, results_index] > 0.7:
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']
                    qr_code = tg['qr_code'] 

            bigkas(random.choice(responses)) 
            
            if qr_code != "":
                folder=r"..\SAB (AI Assistant)\qr_codes"

                files = folder+'\\'+qr_code
                qr = PIL.Image.open(files)
                qr.show()
                time.sleep(20)

            if tag == "thanks":
                break
            
        
        else:
           bigkas("Pakiulit po. Di kita maintindihan.")

fil_voice()

#==========GUI===============
"""wn = tkinter.Tk() 
wn.title("Student Assistant Bot")
wn.geometry('700x300')

photo = PhotoImage(file = "star.png")
wn.iconphoto(False, photo)

wn.config(bg='Maroon')
  
Label(wn, text='Please press the button to start.', bg='Maroon',
      fg='white', font=('Courier', 15)).place(x=120, y=10)

#Button to convert PDF to Audio form
Button(wn, text="Simulan", bg='Goldenrod',font=('Courier', 15),
       command=eng_voice).place(x=300, y=100) ######original

wn.mainloop()"""