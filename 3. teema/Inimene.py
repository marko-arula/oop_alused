class Inimene():

    def __init__(self, e, p, kk = 1):
        self.eesnimi = e
        self.perenimi = p
        self.kutsekvalifikatsioon = kk

    def __del__(self):
        print("Kõige head, " + self.eesnimi + ", " + self.perenimi + "!")

    def tutvustus(self):
        print("Tere, olen " + self.eesnimi + " " + self.perenimi + "!")
