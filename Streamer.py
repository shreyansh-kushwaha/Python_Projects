import youtube_dl
import pafy
import os

import pywhatkit as pw

def play(file):
    # for i in main:
    os.system('ffplay "{}"'.format(file))
    # os.remove(file)

os.chdir('/')
path = os.environ['USERPROFILE']
os.chdir(f'{path}\\AppData\\Local\\Temp')

name = input('Enter the name of the song:\n')
url = pw.playonyt(name)

# url = input('Enter the URL of the song:\n')

try:
    video = pafy.new(url)
    print(video.title)
    title= video.title
    # print(type(title))
    # while '|' in title:

        # title.replace('|','_')
        # continue
    for i in range(8):
        title = ''
        title += video.title[i]
    # print(title)
except Exception as a:
    input('Cannot Connect.. Internet not connected or invalid URL or id.')
    print(a)
    quit()

ydl_opts = {
    'format':'bestaudio'
} 

with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
    try:
	    ydl.download([url]) 
        
    except:
        input('Cannot Connect to The server..')
        quit()
    
if name.lower() == 'darkside':
    play('Alan Walker - Darkside (feat. Au_Ra and Tomine Harket)-M-P4QBt-FWw.webm')

files = os.listdir()
main = []
for i in files:
    if title in i:
        main.append(i)
    if i.endswith('.webm'):
        print(i)

# print(main)
for file in main:
    play(file)