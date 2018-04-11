from tkinter import *
from tkinter import ttk
from tkinter import font
from random import randint

root = Tk()
root.title("D20 Roller")

def roll_it(*args):
    try:
        
        MSGDICT = {1:"YOU'RE THE BEST WIFE!", 2:"YOU MAKE ME SO HAPPY!", 3:"I LOVE YOU SO MUCH!", 4:"LET'S GET JIGGY WITH IT!", \
                    5:"I LOVE YOUR MEATLOAF!", 6:"I WASN'T ALIVE UNTIL I MET YOU!", 7:"YOU ARE MY SUNSHINE!", \
                    8:"MY LIFE WOULD BE EMPTY WITHOUT YOU!", 9:"TO SEE YOU SMILE IS TO SEE SUN PART THE HEAVENS", \
                    10:"I LOVE CHICKENSALAD BECAUSE OF YOU!", 11:"YOU'RE THE REASON I GET UP IN THE MORNING", \
                    12:"I'LL NEVER BE ABLE TO THANK YOU ENOUGH FOR TAKING ME TO THE BEACH!", \
                    13:"WHAT LIGHT THROUGH YONDER WINDOW BREAKS?  IT IS THE EAST, AND FAIR CINDY IS MY SUN!", \
                    14:"I FEEL LIKE LIGHTENING.  MY BURDEN IS AWESOME!", \
                    15:"IF I BUT HAD HEAVEN'S EMBROIDERED CLOTH, BUT I BEING A POOR MAN HAVE ONLY MY DREAMS.  TREAD CAREFULLY FOR YOU TREAD ON MY DREAMS!", \
                    16:"I WISH I HAD MET YOU EARLIER IN LIFE!", 17:"I'VE NEVER KNOWN A LOVE QUITE LIKE THIS!", \
                    18:"DID IT HURT?  I MEAN, WHEN YOU FELL FROM HEAVEN?", 19:"I KNOW GOD LOVES ME BECAUSE HE GAVE ME YOU!", \
                    20:"THE THOUGHT OF LOSING YOU SCARES ME BECAUSE I KNOW I'LL NEVER FIND LOVE LIKE YOURS AGAIN!"}
        
        rando = randint(1,20)
        
        modifier = mod.get()
        if not modifier:
            result.set(rando)
        else: 
            result.set(rando + int(modifier))

        msg.set("CINDY, " + MSGDICT[rando])
        
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
ttk.Label(mainframe, textvariable=msg, justify=CENTER, wraplength=150).grid(column=1, columnspan=2, row=5, rowspan=5)


for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()