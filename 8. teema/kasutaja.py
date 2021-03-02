class Kasutajad():

    def __init__(self, e, p, privileeg):
        self.eesnimi = e
        self.perenimi = p
        self.privileeg = privileeg

    def kirjelda_kasutaja(self):
        print("Kasutaja eesnimi on " + (self.eesnimi))
        print("Perenimi on " + self.perenimi)
        print("Privileegid " + self.privileeg)

    def tervita_kasutaja(self):
        print("Tere! " + str(self.eesnimi) + " " + str(self.perenimi) + ".")