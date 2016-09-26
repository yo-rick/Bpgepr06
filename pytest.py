def kwadraad(getal1, getal2):
    kwadraad1 = getal1 * getal1
    kwadraad2 = getal2 * getal2
    return kwadraad1, kwadraad2

def verdubbel(getal1, getal2):
    dubbel1 = getal1 * 2
    dubbel2 = getal2 * 2
    return dubbel1, dubbel2

def keer(getal1, getal2):
    keer1 = getal1 * getal2
    return keer1

def delen(getal1, getal2):
    deling = getal1 / getal2
    return deling

def main():
    print("Dit programma doet iets met getallen.")
    vraag1 = int(input("Geef een getal op: "))
    vraag2 = int(input("Geef nog een getal op: "))
    uitkomst1, uitkomst2 = verdubbel(vraag1, vraag2)
    print('getal 1', uitkomst1)
    print("Getal 2 dubbel =", uitkomst2)
    getalkeer = keer(vraag1, vraag2)
    deel_getal = delen(vraag1, vraag2)
    print("het deelgetal =", deel_getal)
    print("het getaal keer het andere getal =", getalkeer)
    print("tralaladiela")
    kwadraad1, kwadraad2 = kwadraad(vraag1, vraag2)
    print("Kwadraad getal1 =", kwadraad1, "\nKwadraad getal2 =", kwadraad2)


main()
