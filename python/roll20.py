from tkinter import *
from tkinter import ttk
from tkinter import font
from random import randint

root = Tk()
root.title("D20 Roller")

def roll_it(*args):
    try:

        rando = randint(1,20)
        
        modifier = mod.get()
        if not modifier:
            result.set(rando)
        else: 
            result.set(rando + int(modifier))

    except Exception as e:
        result.set("ERROR")
        print(e)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, stick=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

mod = StringVar()
msg = StringVar()
msgfont = font.Font(size=14)
result = StringVar()
resultfont = font.Font(size=22)

ttk.Label(mainframe, text="Modifier").grid(column=1, row=1, sticky=W)
ttk.Entry(mainframe, textvariable=mod).grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, text="Result").grid(column=2, columnspan=2, row=2, sticky=W)
ttk.Label(mainframe, textvariable=result, font=resultfont).grid(column=2, columnspan=2, row=3, sticky=W)
ttk.Button(mainframe, text="Roll D20", command=roll_it).grid(column=2, columnspan=2, row=4, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()