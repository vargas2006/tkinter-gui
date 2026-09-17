from tkinter import *
from tkinter.ttk import *
import time

def download():
    GB = 100
    downloaded = 0
    speed = 1
    while(downloaded < GB):
        time.sleep(0.2)
        bar['value']+=speed
        downloaded+=speed
        percent.set(str(downloaded/GB*100) + "% done")
        text.set(str(downloaded)+"/"+str(GB)+" GB downloaded")
        window.update_idletasks()
    

window = Tk()
text = StringVar()
percent = StringVar()
bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)
percentLabel = Label(window, textvariable=percent).pack()
textLabel = Label(window, textvariable=text).pack()
button = Button(window, text="Download", command=download).pack()


window.mainloop()