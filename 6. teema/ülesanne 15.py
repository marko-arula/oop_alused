from Kasutaja import Kasutaja

Kasutaja1 = Kasutaja("Juhan", "Liivi", "LiivJuhan")
Kasutaja2 = Kasutaja("Edgar", "Saar", "Saaregar")
Kasutaja3 = Kasutaja("Jüri", "Promet", "Promri")

Kasutaja1.kontrolli_parool("qwertyu1234567")
Kasutaja2.kontrolli_parool("Seeonparimparool")
Kasutaja3.kontrolli_parool("qwer12435")





Kasutaja1.kirjelda_kasutaja()
Kasutaja2.kirjelda_kasutaja()
Kasutaja3.kirjelda_kasutaja()

Kasutaja1.tervita_kasutaja()
Kasutaja2.tervita_kasutaja()
Kasutaja3.tervita_kasutaja()