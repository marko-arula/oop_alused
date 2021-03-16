from opimine import *

aine_teemad = Andmed("OOP pohimotted", "Klassid ja objektid", "Konstruktor")
print("Aine teema")
for teema in aine_teemad:
    print(teema)
print("-------------")
kadi = Opilane("Kadi")
mati = Opilane("Mati")
anna = Opetaja()
anna.opetab(aine_teemad[0], kadi, mati)

print(kadi.teadmised)
print(mati.teadmised)

