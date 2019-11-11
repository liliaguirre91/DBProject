#!/usr/bin/python3
# -*- coding: utf-8 -*-


# Using tutorial from http://www.dealingdata.net/2016/08/21/Python-MySQL-GUI/
# This must be run using Python 3

from tkinter import *
from tkinter import messagebox
import tkinter as tk

import pymysql as MySQL
import pandas as pd
import time
import datetime
import re
import os

# Class will set up the GUI
class App(object):
    def __init__(self, window):
        #Set the window's title
        window.wm_title("Database Phase 2 GUI")
        window.geometry('600x300')
        self.formatWindow(window)
        
    def formatWindow(self, window):
        self.current_row = 0
        self.insertionSection(window)
        self.querySection(window)
    
    def insertionSection(self, window):
        top_frame = Frame(window)
        heading = Label(window,text='INSERTIONS', fg="white", bg="blue").grid(row=self.current_row, column=0)
        self.current_row += 1
        self.inputLabel = Label(window, text='Please enter an Input file with insertion data and select the insert type:')
        self.inputLabel.grid(row=self.current_row, column=0)
        self.current_row += 1
        self.userInput_text = StringVar()
        self.userInput = Entry(window, textvariable=self.userInput_text)
        self.userInput.grid(row=self.current_row, column=0)
        self.current_row += 1
        
        #inputFile = self.userInput_text.get()
        self.singleInsert = Button (top_frame, text="Single Line Insert")
        self.singleInsert.grid(row=self.current_row,column=0, columnspan=1)
        self.multipleInsert = Button (top_frame, text="Multile Line Insert")
        self.multipleInsert.grid(row=self.current_row,column=1)
        self.loadInsert = Button (top_frame, text="Load Data Insert")
        self.loadInsert.grid(row=self.current_row,column=2)

        #self.enterFile_button.grid(row=self.current_row,column=0,columnspan=2)
        #self.current_row += 1
        
    def querySection(self, window):
        bottom_frame = Frame(window)
        heading = Label(window,text='QUERY').grid(row=self.current_row, column=0)
        self.current_row += 1
        self.inputLabel = Label(window, text='Please enter the table name you would like to query:')
        self.inputLabel.grid(row=self.current_row, column=0)
        self.current_row += 1
        self.userInput_text = StringVar()
        self.userInput = Entry(window, textvariable=self.userInput_text)
        self.userInput.grid(row=self.current_row, column=0)
        self.current_row += 1
        
        self.queryButton = Button (bottom_frame, text="Query Database").place(x=245, y=250)

    def getQuery(self):
        inputFile = self.userInput_text.get()
        con = MySQL.connect('localhost', 'root', '05deMayo!!', 'OffensiveNFLPlayers')

        with con:
            cur = con.cursor()
            cur.execute(inputFile)
            
            rows = cur.fetchall()
            print (rows) 
                
        print(inputFile)

# Define an main function to create GUI and send it to App class
def main():
    window = tk.Tk()
    start = App(window)
    
    window.mainloop()

# Run the main function
if __name__ == "__main__":
    main()


