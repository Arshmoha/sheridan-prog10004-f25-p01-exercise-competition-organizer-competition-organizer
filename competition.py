"""Defines the Competition class which manages competition/athlete data"""

from athelete import Athlete

class Competition:
    ATHLETE_DATA_FILE_NAME = "data/olympics.csv"

    def __init__(self):
        """Constructor method that defines the field variables for competition objects"""
        self._athleteList = [] # 1 to many (*) HAS-A relationship

    def load(self):
        """Loads the athlete data from a data file"""
        pass

    def save(self):
        """Saves the athlete data to a data file"""
        pass

    def printCompetitors(self):
        """Prints the list of competitors that participate in the competition"""
        pass

    def saveMedalists(self):
        """Exports a new file with the althelets that won a medal"""
        pass