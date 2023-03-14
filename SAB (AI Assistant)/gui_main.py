import tkinter
from tkinter import *
import os, sys
#import admin_gui_eng as e_gui
#import admin_gui_fil as f_gui

def e_gui():
    os.system('python admin\\admin_gui_eng.py')
def f_gui():
    os.system('python admin\\admin_gui_fil.py')

wn = tkinter.Tk() 
wn.title("Student Assistant Bot")
wn.geometry('700x300')

photo = PhotoImage(file = "star.png")
wn.iconphoto(False, photo)

wn.config(bg='Maroon')
  
Label(wn, text='What bot responses do you want to edit?\n(Anong mga pagtugon ng bot ang nais mong baguhin?)', bg='Maroon',
      fg='white', font=('Courier', 15)).place(x=50, y=20)

#Button to convert PDF to Audio form
Button(wn, text="English", bg='Goldenrod',font=('Courier', 15),
       command=e_gui).place(x=200, y=100) 

Button(wn, text="Filipino", bg='Goldenrod',font=('Courier', 15),
       command=f_gui).place(x=350, y=100) 


wn.mainloop()