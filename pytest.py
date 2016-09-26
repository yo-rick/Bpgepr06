def verdubbel(getal1, getal2):
    dubbel1 = getal1 * 2
    dubbel2 = getal2 * 2
    return dubbel1, dubbel2

def keer(getal1, getal2):
    keer1 = getal1 * getal2
    return keer1


def main():
    print("Dit programma doet iets met getallen.")
    vraag1 = int(input("Geef een getal op: "))
    vraag2 = int(input("Geef nog een getal op: "))
    uitkomst1, uitkomst2 = verdubbel(vraag1, vraag2)
    print('getal 1', uitkomst1)
    print("Getal 2 dubbel =", uitkomst2)
    getalkeer = keer(vraag1, vraag2)
    print("het getaal keer het andere getal =", getalkeer)
    print("klaar")


main()
