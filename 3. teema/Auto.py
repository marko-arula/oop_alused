class Auto():
    # lihtne auto mudel
    # tootja, mudel, aasta
    def __init__(self, t, m, a):
        self.tootja = t
        self.mudel = m
        self.aasta = a
        self.odomeetri_nait = 0

    def kirjeldus(self):
        pikk_nimi = str(self.aasta) + " " + self.tootja + " " + self.mudel
        return pikk_nimi.title()

    def odomeeter(self):
        print("Antud auto on sõitnud läbi " + str(self.odomeetri_nait) + " km.")
    # 2 - atribuuti väärtuse muutmine meetodi abil
    def uuenda_odomeeter(self, km):
        if km >= self.odomeetri_nait:
            self.odomeetri_nait = km
        else:
            print("Ei ole võimalik tagasi keerata odomeetri näitu")

    def suurenda_odomeeter(self, km):
        self.odomeetri_nait += km