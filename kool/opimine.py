class Andmed():
    def __init__(self, *info):
        self.info = list(info)
    def __getitem__(self, i):
        return self.info[i]

class Opilane():
    def __init__(self, nimi):
        self.nimi = nimi
        self.teadmised = []

    def opib(self, teema):
        self.teadmised.append(teema)

    def kirjeldus(self):
        print("Opilase " + self.nimi + " teadmised:")
        for teema in self.teadmised:
            print(teema)

    def unustamine(self, teema):
        self.teadmised.remove(teema)

class Opetaja():
    def opetab(self, teema, *opilased):
        for opilane in opilased:
            opilane.opib(teema)
    def __init__(self, nimi):
        self.nimi = nimi