#################### importing required modules ######################
from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator


####################### creating GUI #################################
window = Tk()
window.geometry('1080x400')
window.title('Language_Translator')
window.wm_iconbitmap('icon.ico')


####################### define language ##############################
language = googletrans.LANGUAGES
lang_val = list(language.values())
lang1 = language.keys()


########################## Function ################################
def translate_text():
    try:
        txt_ = input_text.get(1.0, END)
        t1 = Translator()
        trans_txt = t1.translate(txt_, src=src_lang.get(), dest=dsn_lang.get())
        output_text.delete(1.0, END)
        output_text.insert(END, trans_txt.text)

    except Exception as e:
        messagebox.showerror('Info', 'Try again')


####################### Top-Bottom Label ###########################
Label(window, text='LANGUAGE TRANSLATOR', font='arial 22 bold italic', bg='white smoke').pack()
Label(window, text='PROJECT BY NAMEERA PATEL', font='arial 12 bold', bg='black', fg='white').pack(side=BOTTOM, fill='x')


######################### Source Side ##############################
frame1 = Frame(window)
frame1.place(x=30, y=110, height=210, width=410)

src_lang = ttk.Combobox(window, values=lang_val, width=22, state='r')
src_lang.place(x=30, y=75)
src_lang.set('English')

Label(window, text='Enter Text', font='timesnewroman 14 bold').place(x=210, y=70)
input_text = Text(frame1, font='timesnewroman 12', wrap=WORD, padx=5, pady=5, height=11, width=48)
input_text.place(x=0, y=0)

scr_scroll = Scrollbar(frame1)
scr_scroll.pack(side='right', fill='y')
scr_scroll.configure(command=input_text.yview)
input_text.configure(yscrollcommand=scr_scroll.set)


######################## Destination Side ##########################
frame2 = Frame(window)
frame2.place(x=640, y=110, height=210, width=410)

dsn_lang = ttk.Combobox(window, values=lang_val, width=22, state='r')
dsn_lang.place(x=880, y=75)
dsn_lang.set('Select Language')

Label(window, text='Translated Text', font='timesnewroman 14 bold').place(x=700, y=70)
output_text = Text(frame2, font='timesnewroman 12', wrap=WORD, padx=5, pady=5, height=11, width=48)
output_text.place(x=0, y=0)

dst_scroll = Scrollbar(frame2)
dst_scroll.pack(side='right', fill='y')
dst_scroll.configure(command=output_text.yview)
output_text.configure(yscrollcommand=dst_scroll.set)


Button(window, text='Translate', font='timesnewroman 15', bg='royal blue1',
       activebackground='sky blue', fg='white', command=translate_text).place(x=480, y=240)

window.mainloop()