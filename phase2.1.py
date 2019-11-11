
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

#output = "hi"

# Class will set up the GUI
#class App(object):
    
    #def __init__(self, window):
        #Set the window's title
       
        #self.formatWindow(window)
        
        
#---------------------------------------------------------------------------------------------
def getQuery():
    tableName = queryInput_text.get()
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
            
        queryTextbox.insert(END, output)
 
 
 
window = tk.Tk()
#start = App(window)
window.wm_title("Database Phase 2 GUI")
window.geometry('600x300')

#---------------------------------------------------------------------------------------------
#scrollbar = Scrollbar(window).pack( side = "right", fill = "y" )
current_row = 0
#self.insertionSection(window)
#self.deleteSection(window)
#self.querySection(window)
        
        
#---------------------------------------------------------------------------------------------

top_frame = Frame(window).pack()
insertHeading = Label(window,text='INSERTIONS', fg="white", bg="gray").pack(pady=20, fill="x")#grid(row=self.current_row, column=0, rowspan="5")

insertLabel = Label(window, text='Please enter an Input file with insertion data and select the insert type:').pack()

insertInput_text = StringVar()
insertInput = Entry(window, textvariable=insertInput_text).pack()
        
singleInsert = Button (top_frame, text="Single Line Insert").pack()
multipleInsert = Button (top_frame, text="Multile Line Insert").pack()
loadInsert = Button (top_frame, text="Load Data Insert").pack()

     
#---------------------------------------------------------------------------------------------

queryHeading = Label(window,text='QUERY', fg="white", bg="gray").pack(pady=20, fill="x")
queryLabel = Label(window, text='Please enter the name of the table you would like to query:').pack()
queryInput_text = StringVar()
queryInput = Entry(window, textvariable=queryInput_text).pack()
queryButton = Button (window, text="Query Database", highlightcolor="green", highlightthickness=4, command=getQuery).pack()
#print(output)
queryTextbox = Text(window, height=25, width=100, relief= "ridge", borderwidth= 6)
queryTextbox.pack()


#---------------------------------------------------------------------------------------------

        #delete
deleteHeading = Label(window,text='DELETIONS', fg="white", bg="gray").pack(pady=20, fill="x")
deleteLabel = Label(window, text='Enter the name of the table that will be deleted').pack()
deleteInput_text = StringVar()
deleteInput = Entry(window, textvariable=deleteInput_text).pack()

delete_button = Button (window, text="Delete table").pack()


window.mainloop()

            

            #print(query)
#---------------------------------------------------------------------------------------------
# Define an main function to create GUI and send it to App class
    




