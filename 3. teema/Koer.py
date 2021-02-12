class Koer():

    # konstruktor
    def __init__(self, h, v = 0):
        self.hyydnimi = h
        self.vanus = v
        self.saba = True
    # dekonstruktor
    def __del__(self):

        print("Kahjuks koer juba nii vana, et läheb ära")
    # meetod
    def kirjeldus(self):
        print("Koer nimega " + self.hyydnimi + " on " + str(self.vanus) + " aastat vana")


