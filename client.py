import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

SERVER = None
PORT = 8050
IP_ADDRESS = '127.0.0.1'
BUFFER_SIZE=4096

def setup():

    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    musicWindow()

setup()

def musicWindow():

    window=Tk()
    window.title('Music Sharer')
    window.geometry('300x300')
    window.configure(bg='LightSkyBlue')

    selectLabel=Label(window,text='Select Song',bg='LightSkyBlue',font=('Calibri',10))
    selectLabel.place(x=2,y=1)

    listBox=Listbox(window,height=10,width=39,activestyle='dotbox',bg='LightSkyBlue',borderwidth=2,font=('Calibri',10))
    listBox.place(x=10,y=10)

    scrollBar=Scrollbar(listBox)
    scrollBar.place(relheight=1,relx=1)
    scrollBar.config(command=listBox.yview)

    playButton=Button(window,text='Play',width=10,bd=1,bg='SkyBlue',font=('Calibri',10))
    playButton.place(x=30,y=200)

    stopButton=Button(window,text='Stop',width=10,bd=1,bg='SkyBlue',font=('Calibri',10))
    stopButton.place(x=200,y=200)

    downloadButton=Button(window,text='Download',width=10,bd=1,bg='SkyBlue',font=('Calibri',10))
    downloadButton.place(x=30,y=250)

    uploadButton=Button(window,text='Upload',width=10,bd=1,bg='SkyBlue',font=('Calibri',10))
    uploadButton.place(x=200,y=250)

    infoLabel=Label(window,text='',fg='Blue',font=('Calibri',10))
    infoLabel.place(x=4,y=400)

    window.mainloop()
