'''import pymysql
import pandas as pd
import argparse
import camelot
import sqlalchemy
# import tabula
'''
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

    # tables = camelot.read_pdf(file_name, pages=page_num)
    # tables[0].to_csv('foo_xml.csv')
    # tables.export('foo_xml.csv', f='xml')
    # data = tables[0].df
    # print(data)
    # root.destroy
    try:
        # BLOCK PDF
        # Conversion to csv file
        tables = camelot.read_pdf(file_name, pages=page_num)
        tables[0].to_csv('foo.csv')
        tables.export('foo_allTables.csv', f='csv')
        # conversion to json file
        tables[0].to_json('foo.json')
        tables.export('foo_json_allTables_.json', f='json')
        # conversion to exel file
        print("_try__helloworld_")
        tables[0].to_excel('foo.excel')
        tables.export('foo_excel_allTables_.xls', f='excel')
        # final data frame used for various purposes
        data = tables[0].df
        print(data)  # printing data in command line
    except IndexError:
        # STREAM PDF
        # Conversion to csv file
        print('_except_helloworld__data_')
        tables = camelot.read_pdf(file_name, pages=page_num, flavor='stream', row_close_tol=10)
        tables[0].to_csv('foo_stream.csv')
        # conversion to json file
        tables[0].to_json('foo_stream.json')
        tables.export('foo_json_allTables_stream_.json', f='json')
        # conversion to exel file
        tables[0].to_excel('foo_stream.xls')
        tables.export('foo_excel_allTables_stream_.xls', f='xls')
        # final data frame used for various purposes
        data = tables[0].df
        print(data)
    except OptionError:
        print("Unsupported Operation __Option_Error__")
    except error:
        print('Error Opertaion __No_engine__ for diff file type')
    except NameError as nm:
        print("The error defined is", nm, "not supported")


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


"""
    tables = camelot.read_pdf(file_name, pages=page_num)
    tables[0].to_csv('foo_json.csv')
    tables.export('foo_json.csv', f='json')
    data = tables[0].df
    print(data)
    root.destroy
"""
root= Tk()
root.configure(background="grey3")

pathlable = Label(root)
pathlable.grid(row=2, column=1)

# entryval = Entry(root)
# entryval.grid(row=16, column=0)
#button = Button(root, text="Print", command=printVal(pathlable))
#button.grid(row=10, column=1)


#root.geometry("550x500")

title=Label(root,text="welcome to file converter",fg="goldenrod", padx=100, font=('Comic Sans MS', 20), pady=10,background="grey3").grid(row=0, columnspan=3, sticky=E)
frame1=Frame(root,highlightbackground="green", highlightcolor="green", highlightthickness=2, width=400, height=10, bd= 0,background="grey3")
frame1.grid(row=1,column=0,padx=10)
pdflabel = Label(frame1,text="Convert Your Pdf",font=('Comic Sans MS', 16),background="grey3",fg="lavender").grid(row=0,column=0,columnspan=3,sticky=N,pady=10)
Btnjson = Button(frame1,text="convert to JSON",bg="plum1",activebackground="MediumOrchid1",command=convertJSONbutton).grid(row=1,column=0)
Btnxml = Button(frame1,text="convert to Xml",command=convertXMLbutton).grid(row=1,column=1)
pglabel = Label(frame1,text="please enter page no.").grid(row=3,column=0,padx=10,pady=10)
txt = Entry(frame1).grid(row=3,column=1,padx=10,pady=10)

frame2=Frame(root,highlightbackground="green", highlightcolor="green", highlightthickness=2, width=400, height=10, bd=0,background="grey3")
frame2.grid(row=1,column=1,padx=10)
imglabel = Label(frame2,text="Convert Your Image",font=('Comic Sans MS', 16),background="grey3",fg="lavender").grid(row=0,column=0,columnspan=3,sticky=N,pady=10)
Btnjson = Button(frame2,text="convert to JSON",bg="peach puff",activebackground="IndianRed3").grid(row=1,column=0)
Btnxml = Button(frame2,text="convert to Xml").grid(row=1,column=1)
pglabel = Label(frame2,text="please enter page no.").grid(row=3,column=0,padx=10,pady=10)
txt = Entry(frame2).grid(row=3,column=1,padx=10,pady=10)

frame3=Frame(root,highlightbackground="green", highlightcolor="green", highlightthickness=2, bd=0,bg="yellow")
frame3.grid(row=2,column=0,columnspan=2,sticky=S,padx=10,pady=10)

path= Label(root,text="Your selected file here :  ",bg="gray3",fg="lavender").grid(row=3,column=0,pady=10,padx=10,sticky=S)
#quitbtn = Button(root,text="quit",command=ro)
root.mainloop()
