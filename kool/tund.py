from opimine import *

aine_teemad = Andmed("OOP pohimotted", "Klassid ja objektid", "Konstruktor")
print("Aine teema")
for teema in aine_teemad:
    print(teema)

print("-------------")

kadi = Opilane("Kadi")
mati = Opilane("Mati")
anna = Opetaja("Anna")

kadi.kirjeldus()
kadi.opib(aine_teemad[0])

mati.kirjeldus()
mati.opib(aine_teemad[0])


anna.opetab(aine_teemad[0], kadi, mati)
kadi.kirjeldus()
mati.kirjeldus()

kadi.unustamine()
kadi.kirjeldus()
mati.unustamine()
mati.kirjeldus()

