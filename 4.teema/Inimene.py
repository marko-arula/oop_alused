from random import randint

class Inimene():
    jk = 0 # jäjekorra Nr. Vaikimisi 0
    def __init__(self):
        self.id = Inimene.jk + 1
        Inimene.jk += 1 # suurendame jk väärtus 1 võrra
    # info
    def info(self):
        print("Inimese id = " + str(self.id))
        print()