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

class Privileegid():
    def __init__(self, privileegid = "lubatud lisada kasutajaid, lubatud eemaldada kasutajad, lubatud blokeerida kasutajad"):
        self.privileegid = privileegid
    def naita_privileegid(self):
        print(self.privileegid)


class Admin(Kasutajad, Privileegid):


    def privileegid(self, privileegid):
        self.privileegid = privileegid
