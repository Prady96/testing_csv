import pymysql
import pandas as pd
import argparse
import camelot
import sqlalchemy
# import tabula

from tkinter import *
from tkinter.filedialog import askopenfilename
import os
from tkinter import ttk
from time import sleep
from tkinter import messagebox

teams = range(100)

from tkinter.filedialog import askopenfilename


def Warning():
    # showwarning('PageNum Not Found', 'Please Enter the Page Number')
    messagebox.showerror("PageNum Not Found", "Please Enter the Page Number")


def convertXMLbutton():
    filename = askopenfilename()
    print(filename)
    # pathlable.configure(text=filename, foreground=blue)
    # return filename
    string = entryval.get()
    print(string)
    if(string == ""):
        Warning()
    file_name = filename
    page_num = string

    tables = camelot.read_pdf(file_name, pages=page_num)
    tables[0].to_csv('foo_xml.csv')
    tables.export('foo_xml.csv', f='xml')
    data = tables[0].df
    print(data)
    root.destroy


def convertJSONbutton():
    filename = askopenfilename()
    print(filename)
    # pathlable.configure(text=filename, foreground=blue)
    # return filename
    string = entryval.get()
    print(string)
    if(string == ""):
        Warning()
    file_name = filename
    page_num = string

    tables = camelot.read_pdf(file_name, pages=page_num)
    tables[0].to_csv('foo_json.csv')
    tables.export('foo_json.csv', f='json')
    data = tables[0].df
    print(data)
    root.destroy


root = Tk()
root.geometry("600x260")


pathlable = Label(root)
pathlable.grid(row=2, column=1)


entryval = Entry(root)
entryval.grid(row=16, column=0)
#button = Button(root, text="Print", command=printVal(pathlable))
#button.grid(row=10, column=1)


label1 = Label(root, text="welcome to file converter", padx=100, font=('Comic Sans MS', 20), pady=10).grid(row=0, columnspan=3, sticky=E)

label2 = Label(root, text="please browse the file to be conveted").grid(row=1, column=0)


label3 = Label(root, text="Your selected file here : ").grid(row=2, column=0)

pathlable = Label(root).grid(row=2, column=1)


label4 = Label(root, text="""Choose the format in which you want to convert your file""", justify=CENTER).grid(row=3)

xml_button = Button(root, text="Convert to XML", command=convertXMLbutton).grid(row=8, column=0)

json_button = Button(root, text="Convet to Json", command=convertJSONbutton).grid(row=8, column=1)

label5 = Label(root, text="Enter the page number you want to convert").grid(row=15, column=0)

button4 = Button(root, text="quit", command=root.destroy).grid(row=20, column=1)


root.mainloop()
