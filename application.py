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
        pass