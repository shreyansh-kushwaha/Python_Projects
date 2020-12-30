from tkinter import *

root = Tk()

root.geometry('300x300')
root.title('Calculator')


def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    try:
        Mbox('Answer', f'{eval(inputValue)}', 0)
    except:
        Mbox('Error', 'Kindly enter a valid equation to continue....', 0)

    # print(inputValue)
textBox=Text(root, height=1, width=109)
textBox.pack()
buttonCommit=Button(root, height=1, width=10, text="Calculate", command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button

test = Label(text='    ')
test.pack()

import ctypes  # An included library with Python install.
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


buttonCommit.pack()

root.mainloop()
