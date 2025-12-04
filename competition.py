"""Defines the Competition class which manages competition/athlete data"""

import json
from athelete import Athlete

class Competition:
    ATHLETE_DATA_FILE_NAME = "data/olympics.json"
    MEDALISTS_DATA_FILE_NAME = "data/medalists.json"

    def __init__(self):
        """Constructor method that defines the field variables for competition objects"""
        self._athleteList = [] # 1 to many (*) HAS-A relationship

    def load(self):
        """Loads the athlete data from a data file"""

        #open the file
        with open(Competition.ATHLETE_DATA_FILE_NAME, "r") as compFile:
            #read the athlete data in JSON format
            athlData = json.load(compFile)

            #for each athlete record
            for athleteRecord in athlData:
                #create the athlete object
                athlete = Athlete(athleteRecord)

                #add the athlete to the list
                self._athleteList.append(athlete)

    def save(self):
        """Saves the athlete data to a data file"""
        pass

    def printCompetitors(self):
        """Prints the list of competitors that participate in the competition"""
        #go through the list of competitors and print their information
        for athlete in self._athleteList:
            print()
            print(f"Name: {athlete.getName()}")
            print(f"Gender: {athlete.getGender()}")
            print(f"Age: {athlete.getAge()}")
            print(f"Team: {athlete.getTeam()}")
            print(f"Event: {athlete.getEvent()}")
            if athlete.hasMedal():
                print(f"Medal: {athlete.getMedal()}")


    def saveMedalists(self):
        """Exports a new file with the althelets that won a medal"""

        #go through each athlete in the competition and constuct the JSON data store
        competitionData = [] #this is a list of dictionaries
        for athlete in self._athleteList:            
            if athlete.hasMedal():
                #convert the object into a dictionary
                athleteData = athlete.toDict()
                
                #add the dictionary to the competition data
                competitionData.append(athleteData)
                
        #write the competition data into the json file for medalists
        with open(Competition.MEDALISTS_DATA_FILE_NAME, "w") as medFile:
            json.dump(competitionData, medFile, indent=4)



           
