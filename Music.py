# ---------------------------------------------------------- CODE STARTS ---------------------------------------------------------- #

# ------------------- About The Author ------------------- #

__author__ = "Shreyansh Kushwaha"
__author_age__ = "13"
__author_class__ = "8th"

# -------------------------------------------------------- #

# -------------------  Importinng The Necesarry files and modules ------------------- #

from tkinter import *
import pafy
import os
import requests
from tkinter import messagebox

# ----------------------------------------------------------------------------------- #

# --- getting current directory and defining some variables --- #

cuurent_dir = os.getcwd()
main_url = ''
formatt = ''

# --------------------------------- #

# ------------------- MAIN FUNCTION TO PLAY MUSIC ------------------- #

def play(pth_dir,file):
    if formatt == "with video":
        os.system(f'{pth_dir}\\ffplay -autoexit "{file}"')
    else:
        os.system(f'{pth_dir}\\ffplay -autoexit -vn -nodisp "{file}"')

# ------------------------------------------------------------------- #


# ------------------- EXTRACT URL FUNCTION ------------------- #

def Extract(topic):
    """Will play video on following topic, takes about 10 to 15 seconds to load"""
    url = 'https://www.youtube.com/results?q=' + topic
    count = 0
    try:
        cont = requests.get(url)
    except:
        messagebox.showerror('Error','Cannot Connect.. Internet not connected or invalid URL or id.')
        cont = ''
    data = cont.content
    data = str(data)
    lst = data.split('"')
    for i in lst:
        count+=1
        if i == 'WEB_PAGE_TYPE_WATCH':
            break
    if lst[count-5] == "/results":
        messagebox.showerror("Error","No video found.")
    return "https://www.youtube.com"+lst[count-5]

# ------------------------------------------------------------ #

# -------------------  Basic GUI Setup -------------------  #

root = Tk()
root.title("     "*10+"Music Downloader")
root.geometry("500x400")
root.resizable(False,False)
try:
    root.wm_iconbitmap('F:\\Music Streamer\\Music Streamer GUI\\icon.ico')
except:
    pass
guide = Label(root,text="Please enter the name of the song below:-")
spce = Label(root,text=" ")
guide.pack()
spce.pack()
name = Text(root,height=1,width=80)
name.pack()

# --------------------------------------------------------- #

# ---- Spacing and organising ---- #

space2 = Label(root,text=" ")
space2.pack()

# -------------------------------- #

# ----- Dropdown list ---- #

variable = StringVar(root)
variable.set("Choose the format.") # default value
w = OptionMenu(root, variable, "with video", "without video")
w.pack()

# ------------------------ #


# ------------------- Basic Variables ------------------- #

url = ''
title = ''

# ------------------------------------------------------- #

# ------------------- Function to get the user input from the GUI Window ------------------- #

def get_input():
    global url,title,best,main_url,formatt
    url = Extract(name.get(1.0,END))
    formatt=variable.get()
    try:
        video = pafy.new(url)
        best = video.getbest()
        main_url = best.url
        print(video.title)
    except:
        messagebox.showinfo("Error","Cannot Connect.. Internet not connected or invalid URL or id.")  
    play(cuurent_dir,main_url)
    
# ------------------------------------------------------------------------------------------- #


# ------------------- Exit Function ------------------- #

def destroy():
    root.destroy()
    exit()

# ----------------------------------------------------- #


# ------------------- Creating some space between the text input area and the button ------------------- #

space = Label(root,text=" ")
space.pack()
space1 = Label(root,text=" ")

# ------------------------------------------------------------------------------------------------------ #


# ------------------- Creating the button which will stream the music -------------------  #

stream = Button(root,text='Stream Song',command=lambda: get_input())
stream.pack()

# ---------------------------------------------------------------------------------------- #


# ------------------- Exit Button ------------------- #

# -- adding space -- #

space1.pack()

# ----------------- #
exit_btn = Button(root,text="   Exit   ",command=lambda: destroy())
exit_btn.pack()

# --------------------------------------------------- #

# ------------------- STARTING THE MAIN LOOP ------------------- #
mainloop()
# -------------------------------------------------------------- #


# ---------------------------------------------------------- CODE ENDS ---------------------------------------------------------- #
