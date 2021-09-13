# importing the modules
import PyPDF2
import pyttsx3
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# create the root window
root = tk.Tk()
root.title('Select a Pdf file to Play in Audio')
root.resizable(True,True )
root.geometry('500x500')


def select_file():
    filetypes = (
        ('pdf_files', '*.pdf'),
        ('text files', '*.txt'),
        ('All files', '*.*'),

    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    # path of the PDF file
    pathofpdf=("Enter the path of filkr")
    path = filename
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-70)

    # creating a PdfFileReader object
    pdfReader = PyPDF2.PdfFileReader(path)

    # the page with which you want to start
    # this will read the page of 25th page.
    from_page = pdfReader.getPage(24)

    # extracting the text from the PDF
    text = from_page.extractText()

    # reading the text
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()


    showinfo(
        title='Selected File',
        message=filename
    )


# open button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
)

open_button.pack(expand=True)


# run the application
root.mainloop()
