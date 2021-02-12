class Kasutajad():
    kasutajanimi = ""
    roll = "tavakasutaja"
    def __init__(self, e, p):
        self.eesnimi = e
        self.perenimi = p
    def kirjelda_kasutaja(self):
        print("Kasutaja eesnimi on " + (self.eesnimi))
        print("Perenimi on " + self.perenimi)
        print("Kasutajanimi on " + self.kasutajanimi)
        print("Kasutaja on " + self.roll)
    def maara_kasutaja_nimi(self, k):
        self.kasutajanimi = k
