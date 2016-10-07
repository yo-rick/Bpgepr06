import os

def tekst(bestand_naam):
    infile = open(bestand_naam, "r")
    inhoud = infile.readlines()
    infile.close
    index = 0
    while index < len(inhoud):
        inhoud[index] = inhoud[index].rstrip('\n')
        index += 1
    return inhoud

def terminal(commando):
    for x in commando:
        os.system(x)
    print "alle commando's zijn uitgevoerd"

def main():
    print "Bestand met gencode's wordt nu aangemaakt"
    gencommands = "uitvoercommando_gen.txt"
    eiwitcommands = "uitvoercommando_eiwit.txt" 
    commando = tekst(gencommands)
    terminal(commando)
    print "Text bestand met gencode's en namen is aangemaakt."
    print "Bestand met eiwitnamen wordt nu aangemaakt."
    commando2 = tekst(eiwitcommands)
    terminal(commando2)
    print "Bestand met eiwitcode's en namen is aangemaakt." 
    
main()
