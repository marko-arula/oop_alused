class Kasutaja():
    eesnimi = ""
    perenimi = ""
    kasutaja_nimi = ""
    parool = ""
    def kirjelda_kasutaja(self):
        print("Kasutaja eesnimi on " + (self.eesnimi))
        print("Perenimi on " + self.perenimi)
        print("Kasutajanimi on " + self.kasutaja_nimi)
        print("Parool on " + self.parool + ".")
    def tervita_kasutaja(self):
        print("Tere tulemast " + self.eesnimi + self.perenimi)