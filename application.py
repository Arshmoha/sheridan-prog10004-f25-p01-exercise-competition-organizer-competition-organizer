"""Application module defines the Application class and the main run() method which
   drives the user interaction
"""

from competition import Competition

class Application:
    def __init__(self):
        #implement the HAS-A relationship between Application and Competition
        self._competition = Competition()

    def run(self):
        """Provides the main interaction loop of the program"""
        #ask the competition to load the athletes data from its file
        self._competition.load()

        #ask the competition to print the athlete roster
        self._competition.printCompetitors()

        #ask the competition to export a new file of medalists
        self._competition.saveMedalists()

        #TODO: Write interaction code to register
        #athletes into the competition
