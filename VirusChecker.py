from tkinter import *
from tkinter import messagebox

root = Tk()

root.title('Virus Checker')
root.geometry('400x300')

def check():
    messagebox.showwarning('Alert!', 'Stop! Virus found!')

button = Button(text='Click me to check for virus', command=check)
button.pack()

root.mainloop()