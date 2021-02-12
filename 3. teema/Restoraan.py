class Restoraan():

    def __init__(self, nimi, tyyp):
        self.restoraani_nimi = nimi
        self.soogi_tyyp = tyyp
    def restoraani_kirjeldus(self):
        print("Restoraani nimi on " + str(self.restoraani_nimi) + ", söögi tüüp on " + str(self.soogi_tyyp))

    def ava_restoraan(self):
        print("Restoraan on avatud")