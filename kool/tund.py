from opimine import *

def menuu():
    print("Tunni programm")
    print("1 - lisa aine teema")
    print("2 - trüki aine teemad")
    print("3 - lisa õpilased")
    print("4 - õpeta teemad õpilastele")
    print("5 - kontrolli õpilaste teadmised")
    print("6 - lase õpilasel unustada teemat")
    valik = int(input("Vali sobilik tegevus: "))
    return valik

def lisa_teemad():
    teemad = Andmed()
    while(True):
        teema = input("Sisesta teema: ")
        if(teema == ""):
            break
        teemad.lisa_info(teema)
    return teemad

def valjasta_teemad(aine_teemad):
    if(len(aine_teemad.info) == 0):
        print("Teemad on veel sisestamata")
    else:
        print("Aine teemad: ")
        for teema in aine_teemad:
            print(teema)
        print("-----------------")

# katsed
aine_teemad = []
while(True):
    valik = menuu()
    if(valik == 1):
        aine_teemad = lisa_teemad()
    if(valik == 2):
        valjasta_teemad(aine_teemad)
    if(valik > 6 or valik < 1):
        break



'''
aine_teemad = Andmed("OOP põhimotted", "Klassid ja objektid", "Konstruktor")
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
'''
