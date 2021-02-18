class Restoraan():

    def __init__(self, nimi, tyyp):
        self.restoraani_nimi = nimi
        self.soogi_tyyp = tyyp
    def restoraani_kirjeldus(self):
        print("Restoraani nimi on " + str(self.restoraani_nimi) + ", söögi tüüp on " + str(self.soogi_tyyp))

    def ava_restoraan(self):
        print("Restoraan on avatud")

class JaatiseKiosk(Restoraan):

    def jaatise_valik(self, valik):
        self.jaatise_valik = valik

    def naita_jaatise_valik(self):
        valikud = self.jaatise_valik.replace(", ", "\n")
        print(valikud)
