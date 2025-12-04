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
            #create the athlete object
            athlInitDataList = athleteRecord[:-1].split(",")
            athlete = Athlete(athlInitDataList)

            #add the athlete to the list
            self._athleteList.append(athlete)

        #close the file
        compFile.close()

    def save(self):
        """Saves the athlete data to a data file"""
        pass

    def printCompetitors(self):
        """Prints the list of competitors that participate in the competition"""
        pass

    def saveMedalists(self):
        """Exports a new file with the althelets that won a medal"""
        pass