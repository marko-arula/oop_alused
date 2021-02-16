from Auto import Auto

ainari_uus_auto = Auto("Audi", "A6", 2017)
minu_uus_auto = Auto("Skoda", "Octavia", 2020)

print(ainari_uus_auto.kirjeldus())
ainari_uus_auto.odomeeter()
# 1 - objekti atribuuti otse väärtustamine
# ainari_uus_auto.odomeetri_nait = 2
ainari_uus_auto.uuenda_odomeeter(2)
ainari_uus_auto.odomeeter()
ainari_uus_auto.suurenda_odomeeter(30)
ainari_uus_auto.odomeeter()


print(minu_uus_auto.kirjeldus())
minu_uus_auto.odomeeter()