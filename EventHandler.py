from tkinter import *

root = Tk()

root.title('Event Handler')
root.geometry('1000x1000')

def handle_key(event):
    print(event.char)

root.bind('<Key>', handle_key)

def handle_click(event):
    print('The button is clicked.')

button = Button(text = 'Click me!')
button.pack()
button.bind('<Button-1>', handle_click)

root.mainloop()