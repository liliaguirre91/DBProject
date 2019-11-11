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

output = "hi"

# Class will set up the GUI
class App(object):
    
    def __init__(self, window):
        #Set the window's title
        window.wm_title("Database Phase 2 GUI")
        window.geometry('600x300')
        self.formatWindow(window)
        
        
#---------------------------------------------------------------------------------------------
    def getQuery(self):
        tableName = self.userInput_text.get()
        global output
        if (tableName.lower() != "players" and tableName.lower() != "games" and tableName.lower() != "teams" and  tableName.lower() != "play"):
            tk.messagebox.showinfo("Alert Message", "Please enter a valid table: players, games, teams, or play!")
        else:
            
            query = "SELECT * FROM " + tableName + ";"
            con = MySQL.connect('localhost', 'root', 'databaseTeam#6', 'OffensiveNFLPlayers')

            with con:
                cur = con.cursor()
                cur.execute(query)
                rows = cur.fetchall()
                
                if (tableName.lower() == "players"):
                    output = "\n   Player ID | First Name | Last Name | Team ID | Position | Touchdowns | Total Yards | Salary"
                    output = output + "\n   ----------+------------+-----------+---------+----------+------------+-------------+---------\n"
                    for row in rows:
                        output = output + "    " + str(row[0]) + "\t " + row[1] + " \t   " + row[2] + "\t   " + str(row[3]) + " \t    " + row[4] + "   \t  " + str(row[5]) + "   \t   " + str(row[6]) + "   \t " + str(row[7]) + "\n"
                    print(output)
                
                elif (tableName.lower() == "games"):
                    print ("\n   Game ID\t|\tDate\t|\tStadium\t|\tResult\t|\tAttendance\t|\tTicket revenue")
                
                elif (tableName.lower() == "teams"):
                    print ("\n   Team ID\t|\tTeam Name\t|\tCity")
                
                elif (tableName.lower() == "play"):
                    print ("\n   PlayerID\t|\tGame ID")
            
        
#---------------------------------------------------------------------------------------------
    def formatWindow(self, window):
        scrollbar = Scrollbar(window).pack( side = "right", fill = "y" )
        self.current_row = 0
        self.insertionSection(window)
        self.deleteSection(window)
        self.querySection(window)
        
        
#---------------------------------------------------------------------------------------------
    def insertionSection(self, window):
        top_frame = Frame(window).pack()
        heading = Label(window,text='INSERTIONS', fg="white", bg="gray").pack(pady=20, fill="x")#grid(row=self.current_row, column=0, rowspan="5")
        self.current_row += 1
        self.inputLabel = Label(window, text='Please enter an Input file with insertion data and select the insert type:').pack()
        #self.inputLabel.grid(row=self.current_row, column=0)
        self.current_row += 1
        self.userInput_text = StringVar()
        self.userInput = Entry(window, textvariable=self.userInput_text).pack()
        #self.userInput.grid(row=self.current_row, column=0)
        self.current_row += 1
        
        #inputFile = self.userInput_text.get()
        self.singleInsert = Button (top_frame, text="Single Line Insert").pack()
        #self.singleInsert.grid(row=self.current_row,column=0)
        self.multipleInsert = Button (top_frame, text="Multile Line Insert").pack()
        #self.multipleInsert.grid(row=self.current_row,column=1)
        self.loadInsert = Button (top_frame, text="Load Data Insert").pack()
        #self.loadInsert.grid(row=self.current_row,column=2)
        self.current_row += 2

        #self.enterFile_button.grid(row=self.current_row,column=0,columnspan=2)
        #self.current_row += 1


#---------------------------------------------------------------------------------------------
    def querySection(self, window):
        global output
        heading = Label(window,text='QUERY', fg="white", bg="gray").pack(pady=20, fill="x")
        self.current_row += 1

        self.inputLabel = Label(window, text='Please enter the name of the table you would like to query:').pack()
        #self.inputLabel.grid(row=self.current_row, column=0)
        #self.current_row += 1
        self.userInput_text = StringVar()
        self.userInput = Entry(window, textvariable=self.userInput_text).pack()
        #self.userInput.grid(row=self.current_row, column=0)
        self.current_row += 1
        
        self.queryButton = Button (window, text="Query Database", highlightcolor="green", highlightthickness=4, command=self.getQuery).pack()
        
        print(output)
        textbox = Text(window, height=25, relief= "ridge", borderwidth= 6)
        textbox.pack()
        textbox.insert(END, output)

#---------------------------------------------------------------------------------------------
    def deleteSection(self, window):
        #delete
        heading = Label(window,text='DELETIONS', fg="white", bg="gray").pack(pady=20, fill="x")
        self.inputLabel = Label(window, text='Enter the name of the table that will be deleted').pack()
        #self.inputLabel.grid(row=self.current_row, column=0)
        self.userInput_text = StringVar()
        self.userInput = Entry(window, textvariable=self.userInput_text).pack()
        #self.userInput.grid(row=self.current_row, column=1)
        #self.current_row += 1

        self.enterFile_button = Button (window, text="Delete table").pack()
        #self.enterFile_button.configure( command=self.getQuery)
        #self.enterFile_button.grid   (row=self.current_row,column=15,columnspan=2)
        self.current_row += 1



            

            #print(query)
#---------------------------------------------------------------------------------------------
# Define an main function to create GUI and send it to App class
def main():
    window = tk.Tk()
    start = App(window)
    
    window.mainloop()

# Run the main function
if __name__ == "__main__":
    main()


