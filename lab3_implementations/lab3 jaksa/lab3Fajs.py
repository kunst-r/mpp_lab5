import numpy as np
import random
import csv
import matplotlib.pyplot as plt

# 1 - Igre - prosjecno trajnaje oko 90 minuta, https://www.statista.com/statistics/1339296/us-pc-gaming-session-length/
# 2 - Drustvene mreze - oko 3 minute prosjecno prije mijenjanja platforme https://www.statista.com/statistics/579411/top-us-social-networking-apps-ranked-by-session-length/
# 3 - Kupovina - 11 minuta prosjek https://www.statista.com/statistics/790897/unique-visitors-average-session-durations-retail-properties-us/ 

stanja = {1 : "Igre", 2 : "Drustvene mreze", 3 : "Kupovina"}



korak = 0 #broj koraka, 10000 je max

vjerojatnostPrijelaza = np.array([[0  , 0.6, 0.4], 
                                  [0.3, 0  , 0.7], 
                                  [0.8, 0.2, 0  ]]) #sansa za prijelaz iz jednog stanja u drugo, ne mogu u isto!

matricaGustoce = np.array([[-1/90,  1/150,  1/225], 
                           [ 1/10, -1/3  ,  7/30 ], 
                           [ 4/55,  1/55 , -1/11 ]])

lambdas = np.array([1/90, 1/3, 1/11])

def sample_from_rate(state):
    #state je value u rjecniku
    if state == "Igre":
        return random.expovariate(1/90)
    if state == "Drustvene mreze":
        return random.expovariate(1/3)
    if state == "Kupovina":
        return random.expovariate(1/11)


pocetnoStanje = random.randrange(1, 3)
prijasnjeStanje = pocetnoStanje
listaVremena = []
listaVremena.append(sample_from_rate(stanja[pocetnoStanje]))
listaVremenaZaIgre = []
listaVremenaZaDrustvenemreze = []
listaVremenaZaKupovina = []
dictVremena = {1 : listaVremenaZaIgre, 2 : listaVremenaZaDrustvenemreze, 3 : listaVremenaZaKupovina}


while korak < 10000:
    korak += 1

    # simulator prelaska stanja
    trenutnoStanje = np.random.choice([1, 2, 3], p=vjerojatnostPrijelaza[prijasnjeStanje - 1])
    vrijemeTrajanja = sample_from_rate(stanja[trenutnoStanje])
    listaVremena.append(vrijemeTrajanja)
    dictVremena[trenutnoStanje].append(vrijemeTrajanja)
    prijasnjeStanje = trenutnoStanje



stacionarneVrijednosti = [0.3644, 0.2881, 0.3475]
stacionarneVrijednosti2 = [0.87497, 0.02306, 0.10197]
ukupnoVrijeme = sum(listaVremena)
stacionarneVrijednostiSimulacije = [sum(dictVremena[1]) / ukupnoVrijeme, sum(dictVremena[2]) / ukupnoVrijeme, sum(dictVremena[3]) / ukupnoVrijeme]

print("Matrica prijelaza")
print(vjerojatnostPrijelaza)

print("Matrica gustoce")
print(matricaGustoce)

print("Stacionarne vrijednosti bez kontinuarane varijable")
print(stacionarneVrijednosti)

print("Stacionarne vrijednosti sa kontinuaranom varijablom")
print(stacionarneVrijednosti2)

print("Udio vremena u simulaciji")
print(stacionarneVrijednostiSimulacije)

#pisanje podataka u csv fajl
with open('lab3.csv', "w") as csv:
    csv.write("Igre,DrustveneMreze,Kupovina\n")
    for i in range(10000):
        row = ""
        if (i < len(listaVremenaZaIgre)):
            row += f"{listaVremenaZaIgre[i]},"
        else:
            row += "/,"
        
        if (i < len(listaVremenaZaDrustvenemreze)):
            row += f"{listaVremenaZaDrustvenemreze[i]},"
        else:
            row += "/,"

        if (i < len(listaVremenaZaKupovina)):
            row += f"{listaVremenaZaKupovina[i]}\n"
        else:
            row += "/\n"
        
        csv.write(row)
