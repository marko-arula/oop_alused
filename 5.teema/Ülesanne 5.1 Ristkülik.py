class Ristkylik():
    def __init__(self, l, k, s):
        self.laius = l
        self.korgus = k
        self.symbol = s

    def __str__(self):
        ruut = []
        for i in range(self.korgus):
            symbolid = self.symbol * self.laius
            ruut.append(symbolid)
        ristkylik_tekstina = "\n".join(ruut)
        return ristkylik_tekstina

    def __add__(self, teine_ristkylik):
        uus_laius = self.laius + teine_ristkylik.laius
        uus_korgus = self.korgus + teine_ristkylik.korgus
        uus_symbol = self.symbol
        return Ristkylik(uus_laius, uus_korgus, uus_symbol)



kujund1 = Ristkylik(4, 2, "*")
print(kujund1)

kujund2 = Ristkylik(8, 3, 'o')
print(kujund2)

uus_kujund = kujund1 + kujund2
print(uus_kujund)




# Marko