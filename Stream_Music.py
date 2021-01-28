import youtube_dl
import pafy
import os
os.chdir('/')
path = os.environ['USERPROFILE']
os.chdir(f'{path}\\AppData\\Local\\Temp')

url = input('Enter the URL of the song:\n')
video = pafy.new(url)
best = video.getbest()
ydl_opts = {
    'format':'bestaudio'
} 

with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
	ydl.download([url]) 

files = os.listdir()
main = []
for i in files:
    if video.title in i:
        main.append(i)

# print(main)
def play(file):
    # for i in main:
    os.system('ffplay "{}"'.format(file))
    os.remove(file)
for file in main:
    play(file)
