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
        
        self.inputLabel = Label(window, text='Please enter an Input file with insertion data')
        self.inputLabel.grid(row=self.current_row, column=0)
        self.userInput_text = StringVar()
        self.userInput = Entry(window, textvariable=self.userInput_text)
        self.userInput.grid(row=self.current_row, column=1)
        self.current_row += 1
        
        #inputFile = self.userInput_text.get()
        self.enterFile_button = Button (window, text="Enter file")
        self.enterFile_button.configure( command=self.getQuery)
        self.enterFile_button.grid(row=self.current_row,column=0,columnspan=2)
        self.current_row += 1
 
        #delete
        self.inputLabel = Label(window, text='Enter the name of the table that will be deleted')
        self.inputLabel.grid(row=self.current_row, column=0)
        self.userInput_text = StringVar()
        self.userInput = Entry(window, textvariable=self.userInput_text)
        self.userInput.grid(row=self.current_row, column=1)
        #self.current_row += 1

        self.enterFile_button = Button (window, text="Delete table")
        self.enterFile_button.configure( command=self.getQuery)
        self.enterFile_button.grid   (row=self.current_row,column=15,columnspan=2)
        self.current_row += 1

    def getQuery(self):
        inputFile = self.userInput_text.get()
        con = MySQL.connect('localhost', 'root', 'B1ahB1ah@563130', 'nflplayers')

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


