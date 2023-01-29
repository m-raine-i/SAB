import speech_recognition
import pyttsx3 as tts
from neuralintents import GenericAssistant
import sys

recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 150) 

todo_list = ['Go Shopping', 'Clean Room']

def greeting():
  speaker.say("Hello, What can I do for you?")
  speaker.runAndWait()
  
def create_note():
  global recognizer

  speaker.say("What do you want to write as note?")
  speaker.runAndWait()

  done = True

  while not done:
    try:         
      with speech_recognition.Microphone() as mic:

        recognizer.adjust_for_ambient_noise(mic, duration = 0.2)
        audio = recognizer.listen(mic)

        note = recognizer.recognize_google(audio)
        note = note.lower()

        speaker.say("Choose a filename!")
        speaker.runAndWait()

        recognizer.adjust_for_ambient_noise(mic, duration = 0.2)
        audio = recognizer.listen(mic)

        filename = recognizer.recognize_google(audio)
        filename = filename.lower()

      with open(filename, 'w') as f:
        f.write(note)
        done = True
        speaker.say("New note successfully created")
        speaker.runAndWait()

    except speech_recognition.UnknownValueError:
      recognizer = speech_recognition.Recognizer()
      speaker.say("I did not understand you. Please try again!")
      speaker.runAndWait()
      
def show_todo():
  speaker.say("Your list contains the following elements")
  for item in todo_list:
    speaker.say(item)
  speaker.runAndWait()
  
def add_todo():
  global recognizer

  speaker.say("What item do you want to add?")
  speaker.runAndWait()

  done = True

  while not done:
    try:

      with speech_recognition.Microphone() as mic:

        recognizer.adjust_for_ambient_noise(mic, duration = 0.3)
        audio = recognizer.listen(mic)

        item = recognizer.recognize_google(audio)
        item = item.lower()

        todo_list.append(item)
        done = True

        speaker.say(item + " was added to the list!")
        speaker.runAndWait()

    except speech_recognition.UnknownValueError:
      recognizer = speech_recognition.Recognizer()
      speaker.say("I'm sorry, can you repeat it again!")
      speaker.runAndWait()
      
def close():
  speaker.say("Paalam")
  speaker.runAndWait()
  sys.exit(0)

mappings = {
  "greeting": greeting,
  "create_node": create_note,
  "add_todo": add_todo,
  "show_todo": show_todo,
  "exit": close
}

assistant = GenericAssistant('intents.json',intent_methods=mappings)
assistant.train_model()

while True:

  try:

    with speech_recognition.Microphone() as mic:

      recognizer.adjust_for_ambient_noise(mic, duration = 0.2)
      audio = recognizer.listen(mic)

      message = recognizer.recognize_google(audio)
      message = message.lower()

    assistant.request(message)

  except speech_recognition.UnknownValueError:
    recognizer = speech_recognition.Recognizer()