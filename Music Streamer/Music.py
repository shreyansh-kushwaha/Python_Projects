#### ----- This python code will help you to stream music from the internet ----- ####

# -------------------------------------------------------------- CODE STARTS -------------------------------------------------------------- #

# ----- Author Details ----- #

__author__ = "Shreyansh Kushwaha"
__author_age__ = "13"
__author_class__ = "8th"

# -------------------------- #



# ----- Importing The Modules ----- #

from requests import __title__
import youtube_dl
import pafy
import os
import Extract_URL

# --------------------------------- #



# ---- Function To Clear The Screen ---- #

def clear():
    os.system('cls')

# -------------------------------------- #



# ---- Clearing The Screen ---- #

clear()

# ----------------------------- #




# ----- Changing Directory ----- #

os.chdir('/')
path = os.environ['USERPROFILE']
os.chdir(f'{path}\\AppData\\Local\\Temp')

# ------------------------------ #



# ----- Main Function To Play Song ----- #

def play(file):
    os.system('ffplay "{}"'.format(file))
    try:
        os.remove(file)
    except:
        pass

# ------------------------= #



# ---- Taking the user input for the name of the song ---- #

name = input('Enter the name of the song:\n')

# -------------------------------------------------------- #


# ---- Getting the youtube URL for the song ---- #

url = Extract_URL.Extract(name)

# ---------------------------------------------- #


# ---- Getting the title of the video and error handling ---- #

try:
    video = pafy.new(url)
    print(video.title)
    title = ''
    for i in range(8):
        title += video.title[i]
except Exception as a:
    input('Cannot Connect.. Internet not connected or invalid URL or id.')
    print(a)
    quit()

# ------------------------------------------------------------ #


# ---- Defining the format of the song ---- #

ydl_opts = {
    'format':'bestaudio'
} 

# ----------------------------------------- #



# ---- Downloading the data of the youtube video in the audio format ---- #

with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
    try:
	    ydl.download([url]) 
        
    except:
        input('Cannot Connect to The server..')
        quit()

# ----------------------------------------------------------------------- #



# ---- Preventing Some Errors ---- #

if name.lower() == 'darkside':
    play('Alan Walker - Darkside (feat. Au_Ra and Tomine Harket)-M-P4QBt-FWw.webm')

# -------------------------------- #



# ---- Getting the name of the files in the directory and finding the audio file ---- #

files = os.listdir()
main = []
for i in files:
    if title in i:
        main.append(i)

# ----------------------------------------------------------------------------------- #


# ---- Playing the Final Audio Files ---- #

for file in main:
    play(file)

# --------------------------------------- #



# -------------------------------------------------------------- CODE ENDS -------------------------------------------------------------- #