class Ristkülik():
    def __init__(self, korgus, laius, symbol):
        self.laius = int(laius)
        self.korgus = int(korgus)
        self.symbol = str(symbol)

    def __str__(self):
        ruut = []
        for i in range(self.korgus):
            ruut.append(self.symbol * self.laius)
        ruut = '\n'.join(ruut)
        return ruut

    def __add__(self, x):
        self.laius = self.laius + x.laius
        self.korgus = self.korgus + x.korgus
        self.symbol = self.symbol + x.symbol


kujund1 = Ristkülik(10, 3, '*')
print(kujund1)
kujund2 = Ristkülik(8, 3, 'z')
print(kujund2)

kujund1.__add__(kujund2)

print(kujund1)

# Marko