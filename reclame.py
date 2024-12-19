from algemene_functies import mijn_functie_2
def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting=prijs * (1-korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro."
    return uitvoer

def inkomsten_totaal(inkomsten):
    inkomsten_som = sum(inkomsten)
    btw=inkomsten_som*0.09
    uitvoer = (f"Het totaal van alle inkomsten van deze week is {inkomsten_som} euro, waarover {btw} euro btw betaald dient te worden.")
    return uitvoer

def laag_en_hoog(mijn_lijst):
    return max(mijn_lijst), min(mijn_lijst)

def gemiddelde(mijn_lijst):
   gemiddelde = (sum(mijn_lijst)/len(mijn_lijst))
   uitvoer = f"De gemiddelfde inkomsten deze week zijn {gemiddelde} euro."
   return uitvoer

def meervoudig(invoer_lijst):
    hoog, laag = laag_en_hoog(invoer_lijst)
    return hoog, laag

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer