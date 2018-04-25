#import tkinter as tk / may not need this anymore
from tkinter import *
from tkinter import ttk
from tkinter import font
from random import randint

class tkWindow:

    # Verify modifier input
    def validate(self, action, index, value_if_allowed,
                 prior_value, text, validation_type, trigger_type, widget_name):
        if len(value_if_allowed) <= 2 and text in '0123456789.-+':
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False

    def __init__(self, root):

        # Actual dice roll
        def roll_it(*args):
            try:

                maxroll = die.get()
                rando = randint(1, maxroll)

                modifier = mod.get()
                if not modifier:
                    result.set(rando)
                else:
                    result.set(rando + int(modifier))

            except Exception as e:
                result.set("ERROR")
                print(e)

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        ## Subframe for controls
        controlframe = tk.Frame(mainframe, bg='lavender', width=450, height=60)
        controlframe.grid(column=1, row=1, sticky=N+W+E+S)
        controlframe.columnconfigure(0, weight=2)
        controlframe.rowconfigure(0, weight=2)

        ## Subframe for results
        resultframe = tk.Frame(mainframe, bg='cyan', width=450, height=50)
        resultframe.grid(column=3, row=1, sticky=N+W+E+S)
        resultframe.columnconfigure(0, weight=1)
        resultframe.rowconfigure(1, weight=1)

        mod = StringVar()
        result = IntVar()
        resultfont = font.Font(size=22)

        ttk.Label(controlframe, text="Select Die:").grid(column=0,row=0)
        die = IntVar()
        d6 = ttk.Radiobutton(controlframe, text='D6', variable=die, value=6).grid(column=0,row=1, sticky=N+W+E)
        d8 = ttk.Radiobutton(controlframe, text='D8', variable=die, value=8).grid(column=0,row=2, sticky=N+W+E)
        d10 = ttk.Radiobutton(controlframe, text='D10', variable=die, value=10).grid(column=0,row=3, sticky=N+W+E)
        d20 = ttk.Radiobutton(controlframe, text='D20', variable=die, value=20).grid(column=0,row=4, sticky=N+W+E)

        ttk.Label(controlframe, text="Modifier").grid(column=0, row=5, stick=N+W+E+S)
        vcmd = (root.register(self.validate),
                        '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        ttk.Entry(controlframe, textvariable=mod, validate="key", validatecommand=vcmd, width=2).grid(column=1, row=5, sticky=N+W+E+S)
        ttk.Label(resultframe, text="Result").grid(column=0, row=0, sticky=N+W+E)
        ttk.Label(resultframe, textvariable=result, font=resultfont).grid(column=0, row=1, sticky=N+W+E+S)

        ttk.Button(mainframe, text="Roll it", command=roll_it).grid(column=2, columnspan=2, row=4, sticky=W+E)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

root = Tk()
tkWindow(root)
root.mainloop()