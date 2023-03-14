import tkinter
from tkinter import *
import os, sys
"""import eng
from eng import eng_voice
import fil
from fil import fil_voice"""

def e_voice():
    os.system('python bot\\eng\\eng.py')
def f_voice():
    os.system('python bot\\fil\\fil.py')

wn = tkinter.Tk() 
wn.title("Student Assistant Bot")
wn.geometry('700x300')

photo = PhotoImage(file = "star.png")
wn.iconphoto(False, photo)

wn.config(bg='Maroon')
  
Label(wn, text='How do you want to communicate with the bot?\n(Paano mo gustong kausapin ang bot?)', bg='Maroon',
      fg='white', font=('Courier', 15)).place(x=80, y=20)

#Button to convert PDF to Audio form
Button(wn, text="English", bg='Goldenrod',font=('Courier', 15),
       command=e_voice).place(x=200, y=100) 

Button(wn, text="Filipino", bg='Goldenrod',font=('Courier', 15),
       command=f_voice).place(x=350, y=100) 


wn.mainloop()