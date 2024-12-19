def kysy_tiedostonimi():
    tiedosto = input("Anna tiedot sisältävän tiedoston nimi: ")
    if not tiedosto.strip():
        tiedosto = "L06T4D1.txt"
    return tiedosto

def palautus_tiedosto(pienin, suurin, summa):
    tiedosto1 = input("Anna tallennettavan tiedoston nimi: ")
    with open(tiedosto1, "w", encoding="utf-8") as tiedosto1:
        tiedosto1.write(f"Pienin askelmäärä oli {pienin} askelta.\n")
        tiedosto1.write(f"Suurin askelmäärä oli {suurin} askelta.\n")
        tiedosto1.write(f"Yhteensä askelia oli {summa} askelta.\n")
        
    



def askeleet_summa(tiedostonimi):
    askeleet_summa = 0
    with open(tiedostonimi, "r", encoding="utf-8") as tiedosto:
        rivit = tiedosto.readlines()
        for rivi in rivit:
            askeleet_summa += int(rivi)
    return askeleet_summa

def min_step(tiedostonimi):
    pieni_arvo = 0
    with open(tiedostonimi, "r", encoding="utf-8") as tiedosto:
        rivit = tiedosto.readlines()
        for rivi in rivit:
            rivi = rivi.strip() 
            if rivi.isdigit():
                arvo = int(rivi)
                if pieni_arvo == 0 or arvo < pieni_arvo:
                    pieni_arvo = arvo
        return pieni_arvo

def max_step(tiedostonimi):
    suuri_arvo = 0
    with open(tiedostonimi, "r", encoding="utf-8") as tiedosto:
        rivit = tiedosto.readlines()
        for rivi in rivit:
            rivi = rivi.strip()
            if rivi.isdigit():
                arvo = int(rivi)
                if suuri_arvo == 0 or arvo > suuri_arvo:
                    suuri_arvo = arvo
        return suuri_arvo
         

    

def main():
    tiedostonimi = kysy_tiedostonimi()
    pienin = min_step(tiedostonimi)
    suurin = max_step(tiedostonimi)
    summa = askeleet_summa(tiedostonimi)
    palautus_tiedosto(pienin, suurin, summa)
    print(f"Pienin askelmäärä oli {pienin} askelta.")
    print(f"Suurin askelmäärä oli {suurin} askelta.")
    print(f"Yhteensä askelia oli {summa} askelta.")
    print("Kiitos ohjelman käytöstä.")

    


if __name__ == "__main__":
    main()