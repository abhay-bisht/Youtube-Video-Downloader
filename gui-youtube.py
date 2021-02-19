from tkinter import *
from pytube import YouTube
root = Tk()
root.geometry("300x200")
root.title("YOUTUBE ---  LITE")
Label(root,text = "YOUTUBE", font = "Consolas 50 bold").pack(anchor = CENTER)

def youtube():
    try:
        myvar.set("Downloading")
        root.update()
        YouTube(link.get()).streams.first().download()
        link.set("video downloaded........")
    except:
        myvar.set("error")
        root.update()
        link.set("entyer the correct link...")
myvar = StringVar()
myvar.set("ENTER THE LINK BELOW:")
Entry(root,textvariable = myvar , width = 40).pack(pady = 10)
link = StringVar()
Entry(root,textvariable = link , width = 40).pack(pady = 10)
Button(root,text = "Download Video" ,command= youtube).pack()
root.mainloop()
