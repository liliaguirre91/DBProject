#CS 482: Database
#Project Phase 2: Fall 2019
#Team 6:
#Liliana Esparza
#Bianca
#Anaira Quezada

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# This must be run using Python 3
# File names will include the table they are inserting into

from tkinter import *
from tkinter import messagebox
import tkinter as tk

import pymysql as MySQL
import time
import datetime
import re
import os
        
#------------------------------------------------------------------------------
#This function is used to connect python to mySQL 
#returns the cursor and connection if connection is successful
#print an error message in window if unsuccessful
def connectToDB():

    try:
        #con = MySQL.connect('localhost', 'root', 'databaseTeam#6', 'OffensiveNFLPlayers', local_infile=1)
        con = MySQL.connect('localhost', 'root', 'Databases19', 'ProjectDB')
        #con = MySQL.connect('localhost', 'root', 'B1ahB1ah@563130', 'nflplayers')

        cur = con.cursor()
        return (cur, con)
    except Exception as e:
         tk.messagebox.showinfo("Alert Message", "Could not connect to database:\n" + str(e))
#----------------------------end connectToDB#----------------------------

#This function is used to insert data in a bulk format
#this reads and inserts data as a whole instead of line by line
#if load is successful message is printed in output box
#timing functionaity is called and is displayed after each successful implementation
def loadDataInsert():
    success = True
    (cur, conn) = connectToDB()
    
    #check to see if table name is valid in our database
    filename = insertInput_text.get()
    if "players" in filename.lower():
        tableName = "players"
        flag = True
    elif "games" in filename.lower():
        tableName = "games"
        flag = True
    elif "play" in filename.lower():
        tableName = "play"
        flag = True
    elif "teams" in filename.lower():
        tableName = "teams"
        flag = True
    else:
        tk.messagebox.showinfo("Alert Message", "Please enter a valid table:\n players, games, teams, or play!")
        flag = False
    
    if flag == True:
        cur.execute("SET SQL_SAFE_UPDATES = 0;")
        cur.execute("DELETE from " + tableName + ";")
        cur.execute("SET SQL_SAFE_UPDATES = 1;")
        try:
            starttime = time.time()
            
            #filename = "/tmp/" + filename
            print (filename)
            #line format has ',' between attribute values therefore use "fields terminated by"
            command = "LOAD DATA LOCAL INFILE '" + filename + "' INTO TABLE " + tableName + " fields terminated BY ',' lines terminated BY '\n';"
            print (command)
            cur.execute(command)
        except Exception as e:
            tk.messagebox.showinfo("Alert Message", "Something went wrong:\n" + str(e))
            cur.execute("SET SQL_SAFE_UPDATES = 0;")
            cur.execute("DELETE from Players;")
            cur.execute("SET SQL_SAFE_UPDATES = 1;")
            success = False
    cur.close()
    conn.commit()
    conn.close()
    endtime = time.time()
    #if opperation was correct print message in textbox
    if success:
        print ('Insert data successful!')
        result = "Insert into " + tableName + " successful!\n" "\nRun time: %.7f Second"%(endtime-starttime)
        tk.messagebox.showinfo(title='Result', message=result)        
#--------------------------------end loadDataInsert----------------------------
        
#This function  inserts data from a text file line by line
#An individual query will be run on each line that is being inserted
#if load is successful message is printed in output box
#timing functionaity is called and is displayed after each successful implementation
def singleInsert():
    #delete all entries in players first
    success = True
    (cur, conn) = connectToDB()
        
    filename= insertInput_text.get()
    if "players" in filename.lower():
        tableName = "players"
        flag = True
    elif "games" in filename.lower():
        tableName = "games"
        flag = True
    elif "play" in filename.lower():
        tableName = "play"
        flag = True
    elif "teams" in filename.lower():
        tableName = "teams"
        flag = True
    else:
        tk.messagebox.showinfo("Alert Message", "Please enter a valid table:\n players, games, teams, or play!")
        flag = False
        
    if flag == True:
        cur.execute("SET SQL_SAFE_UPDATES = 0;")
        cur.execute("DELETE from " + tableName + ";")
        cur.execute("SET SQL_SAFE_UPDATES = 1;")
        f = open(filename, "r")
        line = f.readline()
        starttime = time.time()
        
        while line:
            line = line.strip('\n')
            value = line.split(",")
            command = "INSERT INTO " + tableName + " VALUES (" + line + ");"
            #command = "INSERT INTO " + tableName + " VALUES (" + value[0] + value[1] + value[2] + value[3] + value[4] + value[5] + value[6] + ");"
            #cur.execute( command) #, [value[0], value[1], value[2], value[3], value[4], value[5], value[6]])
            try:
                if tableName == "players":
                    cur.execute("INSERT INTO " + tableName + " values(%s,%s,%s,%s,%s,%s,%s,%s)",
                    [value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7]])
                elif tableName == "games":
                    cur.execute("INSERT INTO " + tableName + " values(%s,%s,%s,%s,%s,%s)",
                    [value[0], value[1], value[2], value[3], value[4], value[5]])
                elif tableName == "play":
                    cur.execute("INSERT INTO " + tableName + " values(%s,%s)", [value[0], value[1]])
                else:
                    #print (value)
                    cur.execute("INSERT INTO " + tableName + " values(%s,%s,%s)", [value[0], value[1], value[2]])
                    
                #print (command)
                line = f.readline()
            
            except Exception as e:
                tk.messagebox.showinfo("Alert Message", "Something went wrong:\n" + str(e))
                cur.execute("SET SQL_SAFE_UPDATES = 0;")
                cur.execute("DELETE from Players;")
                cur.execute("SET SQL_SAFE_UPDATES = 1;")
                success = False
                break
        #else:
         #   tk.messagebox.showinfo("Alert Message", "Please enter a valid file that contains a table name!")

    f.close()
    cur.close()
    conn.commit()
    conn.close()
    endtime = time.time()
    if success:
        print ('Insert data successful!')
        result = "Insert into " + tableName + " successful!\n" "\nRun time: %.7f Second"%(endtime-starttime)
        tk.messagebox.showinfo(title='Result', message=result)
#------------------------------------end singleInsert--------------------------

#This function is used to insert data in a series of linked lines
#this reads and inserts data as a whole instead of line by line
#if load is successful message is printed in output box
#timing functionaity is called and is displayed after each successful implementation
def multiLineInsert():
    #delete all entries in players first
    success = True
    (cur, conn) = connectToDB()
        
    filename= insertInput_text.get()
    if "players" in filename.lower():
        tableName = "players"
        flag = True
    elif "games" in filename.lower():
        tableName = "games"
        flag = True
    elif "play" in filename.lower():
        tableName = "play"
        flag = True
    elif "teams" in filename.lower():
        tableName = "teams"
        flag = True
    else:
        tk.messagebox.showinfo("Alert Message", "Please enter a valid table:\n players, games, teams, or play!")
        flag = False
        
    if flag == True:
        cur.execute("SET SQL_SAFE_UPDATES = 0;")
        cur.execute("DELETE from " + tableName + ";")
        cur.execute("SET SQL_SAFE_UPDATES = 1;")
        
        f = open(filename, "r")
        line = f.readline()
        command = "INSERT INTO " + tableName + " VALUES "
        while line:
            line = line.strip('\n')
            values = line.split(",")
            tuple = ""
            for index in range(len(values)):
                if index == 0:
                    tuple += "('" + values[index] + "'"
                elif index == len(values) - 1:
                    tuple += ", '" + values[index] + "'),"
                else:
                    tuple += ",'" + values[index] + "'"
            
            command += tuple
            line = f.readline()
        command = command[:-1]
        starttime = time.time()
        try:
            if tableName == "players":
                cur.execute(command)
            elif tableName == "games":
                cur.execute(command)
            elif tableName == "play":
                cur.execute(command)
            else:
                cur.execute(command)
            
        except Exception as e:
            tk.messagebox.showinfo("Alert Message", "Something went wrong:\n" + str(e))
            success = False
    else:
        tk.messagebox.showinfo("Alert Message", "Please enter a valid file that contains a table name!")

    f.close()
    cur.close()
    conn.commit()
    conn.close()
    endtime = time.time()
    if success:
        print ('Insert data successful!')
        result = "Insert into " + tableName + " successful!\n" "\nRun time: %.7f Second"%(endtime-starttime)
        tk.messagebox.showinfo(title='Result', message=result)
#----------------------------------end multiLineInsert----------------------------------------

#this function will display all the tuples in a given table
#prints table tuples in textbox in formated form
#checks for valid table names: PLAYERS, GAMES, TEAMS, PLAY
#deletes the pervious query before new tuples are displayed
def getQuery():
    queryTextbox.delete('1.0','end')
    tableName = queryInput_text.get()
    if (tableName.lower() != "players" and tableName.lower() != "games" and tableName.lower() != "teams" and  tableName.lower() != "play"):
        tk.messagebox.showinfo("Alert Message", "Please enter a valid table:\n players, games, teams, or play!")
    else:
            
        query = "SELECT * FROM " + tableName + ";"
        (cur, conn) = connectToDB()
        cur.execute(query)
        rows = cur.fetchall()
        desc = cur.description      #this gets the attribute names
        if (tableName.lower() == "players"):
            output = ("{0:>8} {1:>15} {2:>12} {3:>8} {4:>12} {5:>12} {6:>12} {7:>10}".format(desc[0][0], desc[1][0], desc[2][0], desc[3][0], desc[4][0], desc[5][0], desc[6][0], desc[7][0])) + "\n" #8 columns
            for row in rows:
                output += ("{0:>8} {1:>15} {2:>14} {3:>7} {4:>11} {5:>11} {6:>10} {7:>15}".format(row[0], row[1], row[2], row [3], row[4], row[5], row[6], row[7])) + "\n"
            output += "\n"
            queryTextbox.insert(0.0, output)
                
        elif (tableName.lower() == "games"):
            #print ("\n   Game ID\t|\tDate\t|\tStadium\t|\tResult\t|\tAttendance\t|\tTicket revenue")
            output = ("{0:>0} {1:>10} {2:>30} {3:>16} {4:>15} {5:>15}".format(desc[0][0], desc[1][0], desc[2][0], desc[3][0], desc[4][0], desc[5][0])) + "\n" #6 attributes
            for row in rows:
                output += ("{0:>4} {1:>15} {2:>30} {3:>9} {4:>15} {5:>15}".format(row[0], str(row[1]), row[2], row [3], row[4], row[5])) + "\n"
            output += "\n"
            queryTextbox.insert(0.0, output)
                
        elif (tableName.lower() == "teams"):
            output = ("{0:>0} {1:>12} {2:>15}".format(desc[0][0], desc[1][0], desc[2][0])) + "\n" #8 columns
            for row in rows:
                output += ("{0:>4} {1:>15} {2:>15} ".format(row[0], row[1], row[2])) + "\n"
            output += "\n"
            queryTextbox.insert(0.0, output)
               
        elif (tableName.lower() == "play"):
            #print ("\n   PlayerID\t|\tGame ID")
            output = ("{0:>3} {1:>7}".format(desc[0][0], desc[1][0])) + "\n" #8 columns
            for row in rows:
                output += ("{0:>4} {1:>10}".format(row[0], row[1])) + "\n"
            output += "\n"
            queryTextbox.insert(0.0, output)
            cur.close()
            conn.close()
            
 #---------------------------------end getQuery()---------------------------
 
#This function gets and prints the average of a given attribute in a table
#Checks for valid tables and attributes
#Valide tables: PLAYERS and GAMES
#Valid attributes: TOUCHDOWNS, TOTALYARDS, SALARY, ATTENDANCE, TICKETREVENUE
#finds and displays time needed to expecture the average query
#result is a single tuple displayed in textbox
def getAverage():
    avgTextbox.delete('1.0','end')
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
            
        (cur, conn) = connectToDB()
        starttime = time.time()
        cur.execute(averageQuery)
        rows = cur.fetchall()
        endtime = time.time()
        
        desc = cur.description
        result = "Average calculation successful!\n" "\nRun time: %.7f Second"%(endtime-starttime)
        tk.messagebox.showinfo(title='Result', message=result)
        #output = "The average number of "
        output = ("{0:>0}".format(desc[0][0])) + " in the " + tableName + " table is:\n"
        for row in rows:
            output = output + str(row[0])
            
    output += "\n"
    avgTextbox.insert(0.0, output )
    cur.close()
    conn.close()
#----------------------------------------end getAverage()---------------------------------------------------------

#this function is used to delete the data inside a given table
#checks for valid tables
#constraints for PLAYERS, PLAYS, GAMES are delete on cascade from TEAM
#Alert message is displayed upon successful implimentation

def deleteTable():
    tablen = deleteInput_text.get()
    if (tablen.lower() != "players" and tablen.lower() != "games" and tablen.lower() != "teams" and  tablen.lower() != "play"):
        tk.messagebox.showinfo("Alert Message", "Please enter a valid table: players, games, teams, or play")
    else:
        query = "DELETE FROM " + tablen + ";"
        #table = tableName
        (cur, conn) = connectToDB()
        cur.execute("SET SQL_SAFE_UPDATES = 0;")
        cur.execute(query)
        cur.execute("SET SQL_SAFE_UPDATES = 1;")
        cur.close()
        conn.commit()
        conn.close()
    tk.messagebox.showinfo("Alert Message", "Table deleted successfully!")
#------------------------------end deleteTable-----------------------------------
    
#scrollbar = Scrollbar(window).pack( side = "right", fill = "y" )
#current_row = 0
#self.insertionSection(window)
#self.deleteSection(window)
#self.querySection(window)

#<<<<<<< HEAD
def onFrameConfig (canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

#------------------------------------Creating Window----------------------------      
window = tk.Tk()
#start = App(window)
window.wm_title("Database Phase 2 GUI")
window.geometry('770x700') 
       
canvas = Canvas(window, borderwidth=10)

#Creating scrollbar for entire 
windowScrollbar = Scrollbar(window, orient="vertical", command=canvas.yview)
canvas.configure(width=2000, height=650, yscrollcommand=windowScrollbar.set)
windowScrollbar.pack( side = "right", fill = "y" )
canvas.pack(expand="yes")
top_frame = Frame(canvas)
canvas.create_window((10, 10), window=top_frame, anchor="nw")
top_frame.bind("<Configure>", lambda event, canvas=canvas:onFrameConfig(canvas))
#top_frame.pack(expand="yes")

#Insertion GUI Portion #1
#Insetion Buttons: SINGLE LINE, MULTIPLE LINE, LOAD DATA
#insertion textboxL where to enter path location to file
insertHeading = Label(top_frame,text='INSERTIONS', fg="white", bg="gray").pack(pady=20, fill="x")#grid(row=self.current_row, column=0, rowspan="5")
insertLabel = Label(top_frame, text='Please enter an Input file with insertion data and select the insert type:').pack()
insertInput_text = StringVar()
insertInput = Entry(top_frame, textvariable=insertInput_text).pack()
singleInsert = Button (top_frame, text="Single Line Insert", command=singleInsert).pack()
multipleInsert = Button (top_frame, text="Multile Line Insert", command=multiLineInsert).pack()
loadInsert = Button (top_frame, text="Load Data Insert", command=loadDataInsert).pack()

     
#GetQuery GUI Portion #2
#getQuery Button: getQuer
#getQuery textbox where to enter name of table
queryHeading = Label(top_frame,text='QUERY', fg="white", bg="gray").pack(pady=20, fill="x")
queryLabel = Label(top_frame, text='Please enter the name of the table you would like to query:').pack()
queryInput_text = StringVar()
queryInput = Entry(top_frame, textvariable=queryInput_text).pack()
queryButton = Button (top_frame, text="Query Database", highlightcolor="green", highlightthickness=4, command=getQuery).pack()
queryScroll = Scrollbar(top_frame)
queryScroll.pack(side="right", fill="y")
queryTextbox = Text(top_frame, height=25, width=100, relief= "ridge", borderwidth= 6, yscrollcommand=queryScroll.set)
queryTextbox.pack()
queryScroll.config(command=queryTextbox.yview)


#deleteTable GUI Portion #3
#deleteTable Button: delete
deleteHeading = Label(top_frame,text='DELETIONS', fg="white", bg="gray").pack(pady=20, fill="x")
deleteLabel = Label(top_frame, text='Enter the name of the table that will be deleted').pack()
deleteInput_text = StringVar()
deleteInput = Entry(top_frame, textvariable=deleteInput_text).pack()
delete_button = Button (top_frame, text="Delete table", command = deleteTable).pack()


#findAverage GUI Portion #4
#findAverage: Buttons; TABLE, ATTRIBUTE
#findAverage textbox where to view the average of the given attribute
findAvgHeading = Label (top_frame, text = 'FIND AVERAGE', fg='white', bg='gray').pack(pady=10, fill='x')
findAvgLabel = Label(top_frame, text='Enter the table and attribute you would like to access').pack()
findAvgTableLabel = Label(top_frame, text = 'Table:     ').pack()
findAvgTableInput_text = StringVar()
findAvgTableInput = Entry(top_frame, textvariable = findAvgTableInput_text).pack()
attributeLabel = Label(top_frame, text = 'Attribute:').pack()
attributeInput_text = StringVar()
attributeInput = Entry(top_frame, textvariable = attributeInput_text).pack()
average_button = Button (top_frame, text="Find Average", highlightcolor='green', highlightthickness=4, command=getAverage).pack()
avgTextbox = Text(top_frame, height=2, width=40, relief= "ridge", borderwidth= 6)
avgTextbox.pack()

window.mainloop()

            































