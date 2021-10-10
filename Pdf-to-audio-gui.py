# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# importing the modules
import PyPDF2
import pyttsx3
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
#def page_select():


def banner():
    print("PPPPPPPPPPPPPPPPP   ")
    print("PPPPP          PPPPPP   ")
    print("PPPPP         PPPPPP   ")
    print("PPPPP       PPPPPP   ")
    print("PPPPP PPPPPPPPPPP  ")
    print("PPPPP   ")
    print("PPPPP   ")
    print("PPPPP   ")
    print("PPPPP   ")
    print("PPPPP   ")
    print("PPP   ")
banner()

k=int(input("Enter Page no:"))
# create the root window
root = tk.Tk()
root.title('Select a Pdf file to Play in Audio')
root.resizable(True,True )
root.geometry('500x500')
#open(pathofpdf, 'rb')

Select_page=(k)


def select_file():
    filetypes = (
        ('pdf_files', '*.pdf'),
        ('text files', '*.txt'),
        ('All files', '*.*'),

    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='~/Documents/java',
        filetypes=filetypes)
    # path of the PDF file
    pathofpdf=("Enter the path of file")
    path = filename
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-70)

    # creating a PdfFileReader object
    pdfReader = PyPDF2.PdfFileReader(path)


    # the page with which you want to start
   
    from_page = pdfReader.getPage(k)

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
#quit button
Quit_button=tk.Button(
    root,
    text="Click Here To Quit",
    command=root.quit,).pack()


# run the application
root.mainloop()
