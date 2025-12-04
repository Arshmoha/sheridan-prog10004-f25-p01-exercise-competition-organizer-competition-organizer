"""Defines the Competition class which manages competition/athlete data"""

from athelete import Athlete

class Competition:
    ATHLETE_DATA_FILE_NAME = "data/olympics.csv"
    MEDALISTS_DATA_FILE_NAME = "data/medalists.csv"

    def __init__(self):
        """Constructor method that defines the field variables for competition objects"""
        self._athleteList = [] # 1 to many (*) HAS-A relationship

    def load(self):
        """Loads the athlete data from a data file"""

        #open the file
        with open(Competition.ATHLETE_DATA_FILE_NAME, "r") as compFile:
            #read the text lines from the file -> list of lines (records)
            athlData = compFile.readlines()[1:] #skip the header line

            #for each athlete record
            for athleteRecord in athlData:
                #create the athlete object
                athlInitDataList = athleteRecord[:-1].split(",")
                athlete = Athlete(athlInitDataList)

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

        #open the file
        with open(Competition.MEDALISTS_DATA_FILE_NAME, "w") as medFile:
            #write the header
            medFile.write("Name, Gender, Age, Team, Event, Medal\n")

            #go through each athlete in the competition
            for athlete in self._athleteList:
                #compose a CSV record with the athlete information if the athlete has a medal
                if athlete.hasMedal():
                    #write the record to the file
                    athleteRecord = f"{athlete.getName()}, {athlete.getGender()}, {athlete.getAge()} , {athlete.getTeam()} , {athlete.getEvent()} , {athlete.getMedal()}"

                    medFile.write(athleteRecord)

                    #go the the next line in the file
                    medFile.write("\n")
