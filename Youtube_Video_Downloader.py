from tkinter import *
import youtube_dl
import ctypes  

root = Tk()
root.geometry('600x550')
root.title('Youtube Video Downloader')
root.wm_iconbitmap('C:\\Users\\Shreyansh\\icon.ico')

options=['video only','audio only','video and audio']

variable = StringVar(root)
variable.set('Choose The Type Of file you wanna download.') # default value

w = OptionMenu(root, variable, *options)
# w.pack()

def exit_app():
    root.destroy()
    exit()

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def download():
    if variable.get() == 'video only':
        ytdl_options ={'format':'bestvideo'}
    elif variable.get()== 'audio only':
        ytdl_options = {
            'format':'bestaudio'
        }
    else:
        ytdl_options = {
            'format':'22'
        }
    with youtube_dl.YoutubeDL(ytdl_options) as ytdl:
        try:
            ytdl.download([url_area.get('1.0','end-1c')])
            Mbox('Information..','File Successfully Downloaded..',0)
        except Exception as error:
            Mbox('Error','Sorry Buddy, an error has occured while downloading the video. Kindly check your internet connection or video URL and then try again..',0)
            # exit()


space1 = Label(text='               ')
space2 = Label(text='               ')
space3 = Label(text='               ')
space4 = Label(text='               ')
space5 = Label(text='               ')
space6 = Label(text='               ')
space7 = Label(text='               ')

space1.pack()
space2.pack()
space3.pack()
space4.pack()
space5.pack()
space6.pack()
space7.pack()


# type_url = Text(root,height=1,width=50)
# guide1 = Label(text='Enter what do you wanna download (video or audio)..')
# guide1.pack()
space = Label(text='               ')
# type_url.pack()
w.pack()
space.pack()
guide2 = Label(text='Enter the URL of the video.')
guide2.pack()
url_area = Text(root,height=1,width=50)
url_area.pack()
download = Button(root,text = '  Download  ',command=download)
download.pack()
space66 = Label(text='               ')
space66.pack()
exit_btn = Button(root,text='     Exit     ',command=exit_app)
exit_btn.pack()

root.mainloop()


# from tkinter import *

# master = Tk()

# variable = StringVar(master)
# variable.set("one") # default value

# w = OptionMenu(master, variable, "one", "two", "three")
# w.pack()

# mainloop()