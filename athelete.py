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
            self._name = initData["Name"]
            self._gender = initData["Gender"]
            self._age = int(initData["Age"])
            self._team = initData["Team"]
            self._event = initData["Event"]
            
            #read the medal data which is either NA or an actual medal.
            #if the medal is NA, initialize the medal to None
            medalData = initData["Medal"]
            self._medal = medalData if medalData != "NA" else None

    def toDict(self):
        """Transform the athlete object into a dictionary to be used in JSON serializtion"""
        return {
            "Name" : self._name,
            "Gender" : self._gender,
            "Age": self._age,
            "Team": self._team,
            "Event": self._event,
            "Medal": "NA" if self._medal == None else self._medal
        }

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

    