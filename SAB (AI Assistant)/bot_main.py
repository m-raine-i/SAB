from tkinter import *
import os, sys
import eng.py
import fil.py

wn = tkinter.Tk() 
wn.title("Student Assistant Bot")
wn.geometry('700x300')

photo = PhotoImage(file = "star.png")
wn.iconphoto(False, photo)

wn.config(bg='Maroon')
  
Label(wn, text='How do you want to communicate with the bot?', bg='Maroon',
      fg='white', font=('Courier', 15)).place(x=120, y=10)

#Button to convert PDF to Audio form
Button(wn, text="English", bg='Goldenrod',font=('Courier', 15),
       command=eng_voice).place(x=150, y=100) 

Button(wn, text="Filipino", bg='Goldenrod',font=('Courier', 15),
       command=fil_voice).place(x=300, y=100) 


wn.mainloop()

