# ---------------------------------------------------------- CODE STARTS ---------------------------------------------------------- #

# ------------------- About The Author ------------------- #

__author__ = "Shreyansh Kushwaha"
__author_age__ = "13"
__author_class__ = "8th"

# -------------------------------------------------------- #

# -------------------  Importinng The Necesarry files and modules ------------------- #

from tkinter import *
import pafy
import youtube_dl
import os
import requests
from tkinter import messagebox

# ----------------------------------------------------------------------------------- #

# ------------------- MAIN FUNCTION TO PLAY MUSIC ------------------- #

def play(file):
    os.system('ffplay -autoexit -vn -nodisp "{}"'.format(file))
    try:
        os.remove(file)
    except:
        pass

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
root.geometry("500x400")
root.title('     '*10+'Music Streamer')
root.resizable(False,False)
root.wm_iconbitmap('F:\\Music Streamer\\Music Streamer GUI\\icon.ico')
guide = Label(root,text="Please enter the name of the song below:-")
spce = Label(root,text=" ")
guide.pack()
spce.pack()
name = Text(root,height=1,width=80)
name.pack()

# --------------------------------------------------------- #


# ------------------- Basic Variables ------------------- #

url = ''
ytdl_options = {
    'format': 'bestaudio'
}
title = ''

# ------------------------------------------------------- #


# ------------------- Changing directory ------------------- #

os.chdir('/')
path = os.environ['USERPROFILE']
os.chdir(f'{path}\\AppData\\Local\\Temp')

# ---------------------------------------------------------- #


# ------------------- Function to get the user input from the GUI Window ------------------- #

def get_input():
    global url,title
    url = Extract(name.get(1.0,END))
    with youtube_dl.YoutubeDL(ytdl_options) as ytdl:
        ytdl.download([url])
    try:
        video = pafy.new(url)
        print(video.title)
        title = ''
        for i in range(8):
            title += video.title[i]
    except:
        messagebox.showinfo("Error","Cannot Connect.. Internet not connected or invalid URL or id.")  
    get_start()
    
# ------------------------------------------------------------------------------------------- #


# ------------------- Exit Function ------------------- #

def destroy():
    root.destroy()
    exit()

# ----------------------------------------------------- #


# ------------------- Function which will manage all other functions and initiate the playing ------------------- #

def get_start():
    files = os.listdir()
    main = []
    for i in files:
        if i.endswith('.webm') or i.endswith('.mp3') or i.endswith('.m4a'):
            if title in i:
                main.append(i)
    for file in main:
        play(file)

# --------------------------------------------------------------------------------------------------------------- #


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

# -- ading space -- #

space1.pack()

# ----------------- #
exit_btn = Button(root,text="   Exit   ",command=lambda: destroy())
exit_btn.pack()

# --------------------------------------------------- #

# ------------------- STARTING THE MAIN LOOP ------------------- #
mainloop()
# -------------------------------------------------------------- #


# ---------------------------------------------------------- CODE ENDS ---------------------------------------------------------- #