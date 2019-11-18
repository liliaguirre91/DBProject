from faker import Faker
import sys
from random import *
import random

def teamGenerator():
    x = randint(1,32)
    return str(x)

def teamNameGenerator(index):
    teams = ["Cardinals", "Falcons", "Ravens", "Bills", "Panthers", "Bears", "Bengals", "Browns", "Cowboys",
             "Broncos", "Lions", "Packers", "Texans", "Colts", "Jaguars", "Chiefs", "Chargers", "Rams",
             "Dolphins", "Vikings", "Patriots", "Saints", "Giats", "Jets", "Raiders", "Eagles", "Steelers",
             "49ers", "Seahawks", "Buccaneers", "Titans", "Redskins"]
    return teams[index-1]
    
def cityGenerator(index):
    cities = ["Arizona", "Atlanta", "Baltimore", "Buffalo", "Carolina", "Chicago", "Cincinnati",
              "Cleveland", "Dallas", "Denver", "Detroit", "Green Bay", "Houston", "Indianapolis",
              "Jaksonville", "Kansas City", "Los Angeles", "Los Angeles", "Miami", "Minnesota",
              "New England", "New Orleans", "New York", "New York", "Oakland", "Philadelphia", "Pittsburgh",
              "San Francisco", "Seattle", "Tampa Bay", "Tennessee", "Washington"]
    return cities[index-1]
    
def positionGenerator():
    positions = ["QB", "RB", "WR"]
    position = sample(positions, 1)
    return position[0]
    
def resultGenerator():
    results = ["W", "L", "T"]
    result = sample(results, 1)
    return result[0]
    
def stadiumGenerator():
    stadiums = ["Arrowhead Stadium", "AT&T Stadium", "Oakland Alameda Coliseum", "Lambeau Field",
                "CenturyLink Stadium", "Lincoln Financial Field", "Heinz Field", "MetLife Stadium",
                "Sports Authority Field", "M&T Bank Stadium", "University of Phoenix Stadium",
                "Ralph Wilson Stadium ", "Paul Brown Stadium", "FirstEnergy Stadium", "Lucas Oil Stadium",
                "Bank of America Stadium", "Raymond James Stadium", "NRG Stadium", "Levi’s Stadium",
                "Gillette Stadium", "Nissan Stadium", "TCF Bank Stadium", "EverBank Field", "Ford Field",
                "Mercedes Benz Superdome", "Qualcomm Stadium", "FedEx Field", "Georgia Dome",
                "Edward Jones Dome", "SunLife Stadium", "Soldier Field"]
    stadium = sample(stadiums, 1)
    return stadium[0]
    
def CreatePlayers(size):
 
    
    #starttime = time.time()
    row = int(size)
    File = open( str(row) + "_Players" + ".txt", "w")
    ID = 0 #PlayerID from 0
    comma = ','
    f = Faker()

    for i in range(row):
        #Random Name
        firstName = f.first_name_male()
        lastName = f.last_name_male()
        ID += 1
        playerID = str(ID).zfill(8)
        teamID = teamGenerator().zfill(3)
        position = positionGenerator()
        touchdowns = str(f.random_int(0,300))
        totalYards = str(f.random_int(-100,500))
        salary = str(round(random.uniform(100000, 1000000), 2))
       
        data = (playerID + comma + firstName + comma + lastName + comma + teamID + comma + position + comma + touchdowns + comma + totalYards + comma + salary)
        File.write(str(data) + "\n")
    #Close the file
    File.close()

def CreateGames(size):

    row = int(size)
    File = open(str(row) + "_Games"+".txt", "w")

    ID = 0 #PlayerID from 0
    comma = ','
    f = Faker()

    for i in range(row):

        #GameID = 1,2,3...
        ID += 1
        gameID = str(ID).zfill(8)
        date = f.date(pattern="%Y-%m-%d")
        stadium = stadiumGenerator()
        result = resultGenerator()
        attendance = str(f.random_int(0,150000))
        ticketRevenue = str(round(random.uniform(1000, 9999999), 2))
  
        data = (gameID + comma + date + comma + stadium + comma + result + comma + attendance + comma + ticketRevenue)
        #write row
        print (data)
        File.write(str(data) + "\n")
    #Close the file
    File.close()
    
def CreateTeams(size):

  row = int(size)
  File = open(str(row) + "_Teams"+".txt", "w")

  ID = 0 #PlayerID from 0
  comma = ','
  f = Faker()

  for i in range(row):

      #GameID = 1,2,3...
      ID += 1
      teamID = str(ID).zfill(8)
      teamName = teamNameGenerator(ID)
      teamCity = cityGenerator(ID)
      
      data = (teamID + comma + teamName + comma + teamCity)
      #write row
      print (data)
      File.write(str(data) + "\n")
  #Close the file
  File.close()
  
def CreatePlay(size):
    
    row = int(size)
    #open file
    File = open(str(row) + "_Play" + ".txt", "w")
  
    ID = 0
    comma = ','
    f = Faker()
  
    for i in range(row):
        ID += 1
        gameID = str(ID).zfill(8)
        playerIDs = sample(range(1,row), 53)
        #playerIDs = playerIDs.split(",")
        #print (playerIDs)
        for i in range(53):
            playerID = str(playerIDs[i]).zfill(8)
            #print (playerID)
            data = (playerID + comma + gameID)
            File.write(str(data) + "\n")
            #print (data)
    
    File.close()



if sys.argv[1].lower() == "players":
    CreatePlayers(sys.argv[2])
elif sys.argv[1].lower() == "games":
    CreateGames(sys.argv[2])
elif sys.argv[1].lower() == "teams":
    CreateTeams(sys.argv[2])
elif sys.argv[1].lower() == "play":
    CreatePlay(sys.argv[2])
