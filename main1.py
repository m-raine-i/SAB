import os

def mainMenu():
    print ("1. English")
    print ("2. Filipino")
    print ("3. Quit")
    selection=int(input("Filipino or English?: "))
    if selection==1:
        eng()
    elif selection==2:
        fil()
    elif selection==3:
        exit
    else:
        print("Please choose between Filipino or English.")
        mainMenu()

def eng():
    os.system('python main2.py')
def fil():
    os.system('python main3.py')

mainMenu()