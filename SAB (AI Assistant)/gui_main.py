from tkinter import *
import os, sys
#import admin_gui (eng).py
#import admin_gui (fil).py

def eng_gui():
    os.system('python3 admin_gui (eng).py')
def fil_gui():
    os.system('python3 admin_gui (fil).py')

wn = tkinter.Tk() 
wn.title("Student Assistant Bot")
wn.geometry('700x300')

photo = PhotoImage(file = "star.png")
wn.iconphoto(False, photo)

wn.config(bg='Maroon')
  
Label(wn, text='What responses do you want to edit?', bg='Maroon',
      fg='white', font=('Courier', 15)).place(x=120, y=10)

#Button to convert PDF to Audio form
Button(wn, text="English", bg='Goldenrod',font=('Courier', 15),
       command=eng_gui).place(x=150, y=100) 

Button(wn, text="Filipino", bg='Goldenrod',font=('Courier', 15),
       command=fil_gui).place(x=300, y=100) 


wn.mainloop()
