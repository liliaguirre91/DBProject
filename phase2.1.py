
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
        con = MySQL.connect('localhost', 'root', 'Databases19', 'ProjectDB')

        with con:
            cur = con.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            desc = cur.description      #this gets the attribute names
            if (tableName.lower() == "players"):
                #output = "\n   Player ID | First Name | Last Name | Team ID | Position | Touchdowns | Total Yards | Salary"
                #output = output + "\n   ----------+------------+-----------+---------+----------+------------+-------------+---------\n"
                #for row in rows:
                #    output = output + "    " + str(row[0]) + "\t " + row[1] + " \t   " + row[2] + "\t   " + str(row[3]) + " \t    " + row[4] + "   \t  " + str(row[5]) + "   \t   " + str(row[6]) + "   \t " + str(row[7]) + "\n"
                #print(output)
                      #prints column names
                
                #print (rows)
                output = ("{0:>0} {1:>10} {2:>12} {3:>8} {4:>12} {5:>12} {6:>12} {7:>10}".format(desc[0][0], desc[1][0], desc[2][0], desc[3][0], desc[4][0], desc[5][0], desc[6][0], desc[7][0])) + "\n" #8 columns
                for row in rows:    
                    output = output + ("{0:>0} {1:>10} {2:>15} {3:>8} {4:>12} {5:>12} {6:>12} {7:>10}".format(row[0], row[1], row[2], row [3], row[4], row[5], row[6], row[7])) + "\n"
       
                
            elif (tableName.lower() == "games"):
                #print ("\n   Game ID\t|\tDate\t|\tStadium\t|\tResult\t|\tAttendance\t|\tTicket revenue")
                output = ("{0:>0} {1:>10} {2:>35} {3:>10} {4:>15} {5:>15}".format(desc[0][0], desc[1][0], desc[2][0], desc[3][0], desc[4][0], desc[5][0])) + "\n" #6 attributes
                for row in rows:    
                    output = output + ("{0:>0} {1:} {2:>35} {3:>10} {4:>15} {5:>15}".format(row[0], row[1], row[2], row [3], row[4], row[5])) + "\n"
       
                
            elif (tableName.lower() == "teams"):
               #print ("\n   Team ID\t|\tTeam Name\t|\tCity")
               output = ("{0:>0} {1:>12} {2:>15}".format(desc[0][0], desc[1][0], desc[2][0])) + "\n" #8 columns
               for row in rows:    
                    output = output + ("{0:>0} {1:>15} {2:>15} ".format(row[0], row[1], row[2])) + "\n"
       
               
            elif (tableName.lower() == "play"):
                #print ("\n   PlayerID\t|\tGame ID")
                output = ("{0:>0} {1:>7}".format(desc[0][0], desc[1][0])) + "\n" #8 columns
                for row in rows:    
                    output = output + ("{0:>0} {1:>10}".format(row[0], row[1])) + "\n"
       
    queryTextbox.insert(END, output)
 #---------------------------------end getQuery()---------------------------
def getAverage():
    tableName     = findAvgTableInput_text.get()
    attributeName = attributeInput_text.get()
    averageQuery  = ''
    output        = ''
    
    if (tableName.lower() != "players" and tableName.lower() != "games"):
        tk.messagebox.showinfo("Table Alert", "Please enter a valid table:\n players or games")
        
    else:
        if(tableName.lower() == 'players'):
            #-----------------------------player attributes-------------------------------
            if (attributeName.lower() != 'touchdowns' and attributeName.lower() != 'totalyards' and attributeName.lower() != 'salary'):
                tk.messagebox.showinfo("Attribute Alert", "Please enter a valid attribute from the Players table:\n touchdowns, totalyards, salary")
            else:
                averageQuery = "SELECT avg(" + attributeName + ") as " + attributeName + " FROM " + tableName + ";"
                    #------------------------------games attribute-------------------------------------          
        if(tableName.lower() == 'games'):
            if (attributeName.lower() != 'attendance' and attributeName.lower() != 'ticketrevenue'):
                tk.messagebox.showinfo("Attribute Alert","Please enter a valid attribute from the Games table:\n attendance, ticketrevenue")
            else:
                averageQuery = "SELECT avg(" + attributeName + ") as " + attributeName + " FROM " + tableName + ";"
            
        con = MySQL.connect('localhost', 'root', 'Databases19', 'ProjectDB')
        with con:
            cur = con.cursor()
            cur.execute(averageQuery)
            rows = cur.fetchall()
            desc = cur.description
            
            #output = attributeName
            output = ("{0:>0}".format(desc[0][0])) + "\n"
            for row in rows:    
                output = output + str(row[0])
    #print(output)
    avgTextbox.insert(END, output )
#------------------end getAverage()----------------------     
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
queryTextbox = Text(window, height=5, width=100, relief= "ridge", borderwidth= 6)
queryTextbox.pack()


#---------------------------------------------------------------------------------------------

#delete
deleteHeading = Label(window,text='DELETIONS', fg="white", bg="gray").pack(pady=20, fill="x")
deleteLabel = Label(window, text='Enter the name of the table that will be deleted').pack()
deleteInput_text = StringVar()
deleteInput = Entry(window, textvariable=deleteInput_text).pack()

delete_button = Button (window, text="Delete table").pack()


 #---------------------------------------------------------------------------------------------
findAvgHeading = Label (window, text = 'FIND AVERAGE', fg = 'white', bg = 'gray').pack(pady = 10, fill = 'x')
findAvgLabel = Label(window, text='Enter the table and attribute you would like to access').pack()

findAvgTableLabel = Label(window, text = 'Table:     ').pack()
findAvgTableInput_text = StringVar()
findAvgTableInput      = Entry(window, textvariable = findAvgTableInput_text).pack()

attributeLabel = Label(window, text = 'Attribute:').pack()
attributeInput_text = StringVar()
attributeInput = Entry(window, textvariable = attributeInput_text).pack()

average_button = Button (window, text="Find Average", highlightcolor = 'green', highlightthickness = 4, command = getAverage).pack()

avgTextbox = Text(window, height=2, width=100, relief= "ridge", borderwidth= 6)
avgTextbox.pack()

window.mainloop()

            

            #print(query)
#---------------------------------------------------------------------------------------------
# Define an main function to create GUI and send it to App class
    































