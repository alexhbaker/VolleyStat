class Player:

    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number
        self.attempts = 0
        self.kills = 0
        self.errors = 0
        self.he = 0.0
        self.kp = 0

    def killScored(self):
        self.attempts+=1
        self.kills+=1
        self.HittingEfficiency()
        self.killPercentage()

    def hitInPlay(self):
        self.attempts+=1
        self.HittingEfficiency()
        self.killPercentage()

    def errorRecorded(self):
        self.attempts+=1
        self.errors+=1
        self.HittingEfficiency()
        self.killPercentage()

    def HittingEfficiency(self):
        self.he = round(((self.kills - self.errors) / self.attempts), 4)

    def killPercentage(self):
        self.kp = (int) (round((self.kills/self.attempts), 2) * 100)

    pass