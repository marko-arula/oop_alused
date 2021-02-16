class Kasutajad():
    kasutajanimi = ""
    roll = "tavakasutaja"
    def __init__(self, e, p, ssl):
        self.eesnimi = e
        self.perenimi = p
        self.sisselogimiskatsed = ssl
    def kirjelda_kasutaja(self):
        print("Kasutaja eesnimi on " + (self.eesnimi))
        print("Perenimi on " + self.perenimi)
        print("Kasutajanimi on " + self.kasutajanimi)
        print("Kasutaja on " + self.roll)
    def tervita_kasutaja(self):
        print("Tere! " + str(self.eesnimi) + " " + str(self.perenimi) + ".")

    def maara_kasutaja_nimi(self, k):
        self.kasutajanimi = k

    def suurenda_sisselogimiskatsed(self):
        self.sisselogimiskatsed = self.sisselogimiskatsed + 1
        print("Antud kasutajal on ", self.sisselogimiskatsed, " sisselogimise katset")

    def reset_sisselogimiskatsed(self):
        self.sisselogimiskatsed = 0
        print("Kasutaja sisselogimisekatsed on taastatud")