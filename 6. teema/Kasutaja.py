class Kasutaja():

    def __init__(self, e, p, kasutajanimi, parool="qwerty"):
        self.eesnimi = e
        self.perenimi = p
        self.kasutajanimi = kasutajanimi
        self.parool = parool




    def maara_parool(self, par):
        self.parool = par


    def naita_parool(self):
        print(self.parool)

    def kontrolli_parool(self, par):
        if len(par) >= 6 and len(par) < 10:
            print("Parool on edukalt vahetatud.")
            self.maara_parool(par)
        else:
            print("Parooli vahetamine on kahjuks ebaõnnestunud.")
            print("Probleem on parooli pikkuses")



    def kirjelda_kasutaja(self):
        print("Kasutaja eesnimi on " + (self.eesnimi))
        print("Perekonnanimi on " + self.perenimi)
        print("Kasutajanimi : " + self.kasutajanimi)
        print("Parool : " + self.parool)

    def tervita_kasutaja(self):
        print("Tere! " + str(self.eesnimi) + " " + str(self.perenimi) + ".")

'''
    def __setattr__(self, maara_parool, parool):
        if maara_parool == 'parool':
            self.__dict__[maara_parool] = parool
        else:
            raise AttributeError

    def __getattr__(self, item):
        print(self.parool)
'''



