"""Defines the Competition class which manages competition/athlete data"""

from athelete import Athlete

class Competition:
    ATHLETE_DATA_FILE_NAME = "data/olympics.csv"

    def __init__(self):
        """Constructor method that defines the field variables for competition objects"""
        self._athleteList = [] # 1 to many (*) HAS-A relationship

    def load(self):
        """Loads the athlete data from a data file"""
        #open the file
        compFile = open(Competition.ATHLETE_DATA_FILE_NAME, "r")

        #read the text lines from the file -> list of lines (records)
        athlData = compFile.readlines()[1:] #skip the header line

        #for each athlete record
        for athleteRecord in athlData:
            #read the record information
            athlInfo = athleteRecord.split(",")

            #create the athlete object
            athlete = Athlete()

            #set all the athlete information
            athlete.setName(athlInfo[0])
            athlInfo.setGender(athlInfo[1])

            #add the athlete to the list

        #close the file

    def save(self):
        """Saves the athlete data to a data file"""
        pass

    def printCompetitors(self):
        """Prints the list of competitors that participate in the competition"""
        pass

    def saveMedalists(self):
        """Exports a new file with the althelets that won a medal"""
        pass