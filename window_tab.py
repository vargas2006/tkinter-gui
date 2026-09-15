from tkinter import *
from tkinter import ttk



window = Tk()
notebook = ttk.Notebook(window) # widget that manages a collection of windows/display

tab1 = Frame(notebook) #new frame for tab1
tab2 = Frame(notebook) # new frame for tab2

notebook.add(tab1, text="Tab 1") # add tab1 to the notebook
notebook.add(tab2, text="Tab 2") # add tab2 to the notebook
notebook.pack(expand=True, fill="both") # expand - to fil any space not used
                                        # fill - to fill space taken up by other widgets
label1 = Label(tab1, text="Hello Tab 1", font=("Consolas", 30), width=50, height=50, bg="red")
label1.pack() #display label 1

label2 = Label(tab2, text="Hello Tab 2", font=("Consolas", 30), width=50, height=50, bg="blue")
label2.pack() #display label 2

window.mainloop()