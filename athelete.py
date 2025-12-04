"""Defines the Athlete class and its associate information and functionality"""

class Athlete:
    """Defines the athlete information and functionality related to it"""
    
    def __init__(self, initData = None):
        """Creates an athlete object that is empty or loaded from teh supplied list of values"""
        if initData == None:
            self._name = ""
            self._gender = ""
            self._age = 0
            self._team = ""
            self._event = ""
            self._medal = ""
        else:
            #initilize the athlete with init data if supplied            
            self._name = initData[0]
            self._gender = initData[1]
            self._age = int(initData[2])
            self._team = initData[3]
            self._event = initData[4]
            self._medal = initData[5] if initData[5] != "NA" else None

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
        assert self._medal != None, "This athlete does not have a medal. Call hasMedal() to check first"
        return self._medal
    
    def setMedal(self, medal):
        """Sets the medal for this athlete"""
        self._medal = medal

    def hasMedal(self):
        return self._medal != None

    