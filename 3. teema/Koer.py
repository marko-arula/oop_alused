class Koer():

    # konstruktor
    def __init__(self, h, v = 0):
        self.hyydnimi = h
        self.vanus = v
        self.saba = True
    # meetod
    def kirjeldus(self):
        print("Koer nimega " + self.hyydnimi + " on " + str(self.vanus) + " aastat vana")


