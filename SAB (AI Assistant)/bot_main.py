from tkinter import *
import os, sys

def mainMenu():
    print ("1. English")
    print ("2. Filipino")
    print ("3. Quit")
    selection=int(input("English or Filipino?: "))
    if selection==1:
        eng()
    elif selection==2:
        fil()
    elif selection==3:
        sys.exit(0)
    else:
        print("Please choose between Filipino or English.")
        mainMenu()

def eng():
    os.system('python3 english.py')
def fil():
    os.system('python3 filipino.py')

mainMenu()

