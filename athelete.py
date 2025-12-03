"""Defines the Athlete class and its associate information and functionality"""

class Athlete:
    """Defines the athlete information and functionality related to it"""
    
    def __init__(self):
        self._name = ""
        self._gender = ""
        self._age = 0
        self._team = ""
        self._event = ""
        self._medal = ""

    def getName(self):
        """Returns the name of the athlete"""
        return self._name
    
    def setName(self, name):
        """Set the name of the atlhete to the given name"""
        self._name = name

    def getGender(self):
        """Returns the gender of the atlhete"""
        return self._gender
    
    def setGender(self, gender):
        """Sets the gender of the athelete"""
        self._gender = gender

    def getAge(self):
        """Returns the age of the athlete"""
        return self._age
    
    def setAge(self, age):
        """Sets the age of the athlete"""
        self._age = age

    def getTeam(self):
        """Returns the team the athlete is representing"""
        return self._team
    
    def setTeam(self, team):
        """Sets the team the athlete is representing"""
        self._team = team

    def getEvent(self):
        """Returns the event the athlete is participating in"""
        return self._event
    
    def setEvent(self, event):
        """Sets the event the athlete is participating in"""
        self._event = event

    def getMedal(self):
        """Returns the medal the althlete has earned or None if they have no medal"""
        return self._medal
    
    def setMedal(self, medal):
        """Sets the medal for this athlete"""
        self._medal = medal

    