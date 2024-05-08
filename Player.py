class Player:

    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number
        self.attempts = 0
        self.kills = 0
        self.errors = 0
        self.he = 0.0

    def killScored(self):
        self.attempts+=1
        self.kills+=1
        self.HittingEfficiency()

    def hitInPlay(self):
        self.attempts+=1
        self.HittingEfficiency()

    def errorRecorded(self):
        self.attempts+=1
        self.errors+=1
        self.HittingEfficiency()

    def HittingEfficiency(self):
        self.he = round(((self.kills - self.errors) / self.attempts), 4)

    pass