class Kasutaja():
    eesnimi = ""
    perenimi = ""
    kasutaja_nimi = ""
    parool = ""
    def kirjelda_kasutaja(self):
        print("Kasutaja eesnimi on " + (self.eesnimi) + ", perenimi on " + self.perenimi + ", kasutajanimi on " + self.kasutaja_nimi + " ja parool on " + self.parool + ".")
    def tervita_kasutaja(self):
        print("Tere tulemast " + self.eesnimi + self.perenimi)