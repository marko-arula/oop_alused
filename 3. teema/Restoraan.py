class Restoraan():

    def __init__(self, nimi, tyyp, teenindatud_kylastajad):
        self.restoraani_nimi = nimi
        self.soogi_tyyp = tyyp
        self.teenindatud_kylastajad = teenindatud_kylastajad
    def restoraani_kirjeldus(self):
        print("Restoraani nimi on " + str(self.restoraani_nimi) + ", söögi tüüp on " + str(self.soogi_tyyp))

    def ava_restoraan(self):
        print("Restoraan on avatud")

    def maara_teenindatud_kylalised(self, tk):
        print("Ennem oli teenindatud ", self.teenindatud_kylastajad)
        self.teenindatud_kylastajad = tk
        print("külaliste arv on määratud nüüdseks ", tk)

    def suurenda_teenindatud_kylalised(self, tk):
        print("Teenindatud külaliste arv oli ennem ", self.teenindatud_kylastajad)
        self.teenindatud_kylastajad = self.teenindatud_kylastajad + tk
        print("Teenindatud külaliste arv on nüüd ", self.teenindatud_kylastajad)