
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
def connectToDB():
    con = MySQL.connect('localhost', 'root', 'databaseTeam#6', 'OffensiveNFLPlayers')
    #con = MySQL.connect('localhost', 'root', 'Databases19', 'ProjectDB')
    with con:
        cur = con.cursor()
    return cur
        
        
#---------------------------------------------------------------------------------------------
def getQuery():
    tableName = queryInput_text.get()
    if (tableName.lower() != "players" and tableName.lower() != "games" and tableName.lower() != "teams" and  tableName.lower() != "play"):
        tk.messagebox.showinfo("Alert Message", "Please enter a valid table: players, games, teams, or play!")
    else:
            
        query = "SELECT * FROM " + tableName + ";"
        cur = connectToDB()
        cur.execute(query)
        rows = cur.fetchall()
        desc = cur.description      #this gets the attribute names
        if (tableName.lower() == "players"):
            output = ("{0:>0} {1:>10} {2:>12} {3:>8} {4:>12} {5:>12} {6:>12} {7:>10}".format(desc[0][0], desc[1][0], desc[2][0], desc[3][0], desc[4][0], desc[5][0], desc[6][0], desc[7][0])) + "\n" #8 columns
            for row in rows:
                output += ("{0:>0} {1:>10} {2:>15} {3:>8} {4:>12} {5:>12} {6:>12} {7:>10}".format(row[0], row[1], row[2], row [3], row[4], row[5], row[6], row[7])) + "\n"
            output += "\n"
            queryTextbox.insert(0.0, output)
                
        elif (tableName.lower() == "games"):
            #print ("\n   Game ID\t|\tDate\t|\tStadium\t|\tResult\t|\tAttendance\t|\tTicket revenue")
            output = ("{0:>0} {1:>10} {2:>35} {3:>10} {4:>15} {5:>15}".format(desc[0][0], desc[1][0], desc[2][0], desc[3][0], desc[4][0], desc[5][0])) + "\n" #6 attributes
            for row in rows:
                output += ("{0:>0} {1:} {2:>35} {3:>10} {4:>15} {5:>15}".format(row[0], row[1], row[2], row [3], row[4], row[5])) + "\n"
            output += "\n"
            queryTextbox.insert(0.0, output)
                
        elif (tableName.lower() == "teams"):
            #print ("\n   Team ID\t|\tTeam Name\t|\tCity")
            output = ("{0:>0} {1:>12} {2:>15}".format(desc[0][0], desc[1][0], desc[2][0])) + "\n" #8 columns
            for row in rows:
                output += ("{0:>0} {1:>15} {2:>15} ".format(row[0], row[1], row[2])) + "\n"
            output += "\n"
            queryTextbox.insert(0.0, output)
               
        elif (tableName.lower() == "play"):
            #print ("\n   PlayerID\t|\tGame ID")
            output = ("{0:>0} {1:>7}".format(desc[0][0], desc[1][0])) + "\n" #8 columns
            for row in rows:
                output += ("{0:>0} {1:>10}".format(row[0], row[1])) + "\n"
            output += "\n"
            queryTextbox.insert(0.0, output)
            
   # queryTextbox.insert(END, output)
 
def onFrameConfig (canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))
 
window = tk.Tk()
#start = App(window)
window.wm_title("Database Phase 2 GUI")
window.geometry('750x1000')


#---------------------------------------------------------------------------------------------
#scrollbar = Scrollbar(window).pack( side = "right", fill = "y" )
current_row = 0
#self.insertionSection(window)
#self.deleteSection(window)
#self.querySection(window)
        
        
#---------------------------------------------------------------------------------------------
canvas = Canvas(window, borderwidth=0)
top_frame = Frame(canvas)
windowScrollbar = Scrollbar(window, orient="vertical", command=canvas.yview)
canvas.configure(width=2000, height=1000, yscrollcommand=windowScrollbar.set)
windowScrollbar.pack( side = "right", fill = "y" )
canvas.pack(expand="yes")
canvas.create_window((10, 10), window=top_frame, anchor="nw")
top_frame.bind("<Configure>", lambda event, canvas=canvas:onFrameConfig(canvas))
#top_frame.pack(expand="yes")

insertHeading = Label(top_frame,text='INSERTIONS', fg="white", bg="gray").pack(pady=20, fill="x")#grid(row=self.current_row, column=0, rowspan="5")

insertLabel = Label(top_frame, text='Please enter an Input file with insertion data and select the insert type:').pack()

insertInput_text = StringVar()
insertInput = Entry(top_frame, textvariable=insertInput_text).pack()
        
singleInsert = Button (top_frame, text="Single Line Insert").pack()
multipleInsert = Button (top_frame, text="Multile Line Insert").pack()
loadInsert = Button (top_frame, text="Load Data Insert").pack()

     
#---------------------------------------------------------------------------------------------

queryHeading = Label(top_frame,text='QUERY', fg="white", bg="gray").pack(pady=20, fill="x")
queryLabel = Label(top_frame, text='Please enter the name of the table you would like to query:').pack()
queryInput_text = StringVar()
queryInput = Entry(top_frame, textvariable=queryInput_text).pack()
queryButton = Button (top_frame, text="Query Database", highlightcolor="green", highlightthickness=4, command=getQuery).pack()
#print(output)
queryTextbox = Text(top_frame, height=25, width=100, relief= "ridge", borderwidth= 6)
queryTextbox.pack()


#---------------------------------------------------------------------------------------------

        #delete
deleteHeading = Label(top_frame,text='DELETIONS', fg="white", bg="gray").pack(pady=20, fill="x")
deleteLabel = Label(top_frame, text='Enter the name of the table that will be deleted').pack()
deleteInput_text = StringVar()
deleteInput = Entry(top_frame, textvariable=deleteInput_text).pack()

delete_button = Button (top_frame, text="Delete table").pack()


window.mainloop()

            

            #print(query)
#---------------------------------------------------------------------------------------------
# Define an main function to create GUI and send it to App class
    




