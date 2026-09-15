from tkinter import *

def create_window():
    new_window = Tk()       # Toplevel() - new window on top of the other window, linked on the bottom window, pag sinara mo ung main masasara lahat
                            # Tk() -  new independent window, pag sinara mo ung main hindi masasara lahat
    old_window.destroy()    #close out of old window then create new window
    Label(new_window, text="Hello").pack()


old_window = Tk()

Button(old_window, text="create new window", command=create_window).pack()

old_window.mainloop()