# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.filedialog as fd
from tkinter import messagebox
import os
from transformers import pipeline

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

def startClick():
    text_Box_1.delete("1.0", END)
    result = generator(entry_Box_1.get(), do_sample=True, min_length=int(entry_Box_2.get()), max_length=int(entry_Box_3.get()), temperature=float(entry_Box_4.get()), num_beams=int(entry_Box_5.get()), no_repeat_ngram_size=int(entry_Box_6.get()), early_stopping=True)
    result = str(result).replace("\n","")
    result = result.replace("\\","")
    result = result.replace("[{'generated_text': '","")
    result = result.replace("'}]","")
    text_Box_1.insert(END, result)
    
xSpacing = 10
ySpacing = 10

#create home screen
Gui_Home_Screen = Tk(className=' GPT Neo Text Generator')

#Window Size Constants
START_HEIGHT = 1280 
START_WIDTH =  720
MIN_HEIGHT = int(START_HEIGHT / 4)
MIN_WIDTH =  int(START_WIDTH / 4)
Gui_Home_Screen.minsize(height=MIN_HEIGHT, width=MIN_WIDTH)
Gui_Home_Screen.geometry(str(START_HEIGHT) + 'x' + str(START_WIDTH))

#prompt entry box
Label(Gui_Home_Screen, text="Enter a prompt:").grid(row=0, column=0, padx=xSpacing, pady=ySpacing)
entry_Box_1 = Entry(Gui_Home_Screen, width=80)
entry_Box_1.grid(row=0, column=1, padx=xSpacing, pady=ySpacing)

#create start button
startButton = Button(Gui_Home_Screen, text='Generate response', command=startClick).grid(row=0, column=2, sticky=W, padx=xSpacing, pady=ySpacing)

#min_length entry box
Label(Gui_Home_Screen, text="Min_Length:").grid(row=1, column=0, padx=xSpacing, pady=ySpacing)
entry_Box_2 = Entry(Gui_Home_Screen, width=20)
entry_Box_2.grid(row=1, column=1, padx=xSpacing, pady=ySpacing)

#max_length entry box
Label(Gui_Home_Screen, text="Max_Length:").grid(row=2, column=0, padx=xSpacing, pady=ySpacing)
entry_Box_3 = Entry(Gui_Home_Screen, width=20)
entry_Box_3.grid(row=2, column=1, padx=xSpacing, pady=ySpacing)

#temperature entry box
Label(Gui_Home_Screen, text="Temperature:").grid(row=3, column=0, padx=xSpacing, pady=ySpacing)
entry_Box_4 = Entry(Gui_Home_Screen, width=20)
entry_Box_4.grid(row=3, column=1, padx=xSpacing, pady=ySpacing)

#num_beams entry box
Label(Gui_Home_Screen, text="Num_Beams:").grid(row=4, column=0, padx=xSpacing, pady=ySpacing)
entry_Box_5 = Entry(Gui_Home_Screen, width=20)
entry_Box_5.grid(row=4, column=1, padx=xSpacing, pady=ySpacing)

#no_repeat_ngram_size entry box
Label(Gui_Home_Screen, text="no_repeat_ngram_size:").grid(row=5, column=0, padx=xSpacing, pady=ySpacing)
entry_Box_6 = Entry(Gui_Home_Screen, width=20)
entry_Box_6.grid(row=5, column=1, padx=xSpacing, pady=ySpacing)

#text box for result
text_Box_1 = Text(Gui_Home_Screen, height=20, width=80)
text_Box_1.grid(row=6, column=1, padx=xSpacing, pady=ySpacing)

#start main loop and show form
Gui_Home_Screen.mainloop()






