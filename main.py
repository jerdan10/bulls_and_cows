import random
import string
import time

def generovani_cisla():
    '''
    Funkce slouží k vygenerování čtyřmístného čísla
    '''
    prvni_cislice = random.choice(string.digits[1:])
    ostatni_cislice = set(string.digits)
    ostatni_cislice.remove(prvni_cislice)
    cislice = [prvni_cislice] + random.sample(ostatni_cislice, 3)
    n = int(''.join(cislice))
    return str(n)

def je_tip_validni(hracovo_cislo):
    '''
    Funkce slouží ke kontrole zdali číslo vložené uživatelem je ve správném formátu
    '''
    if len(hracovo_cislo) != 4:
        return False
    elif not hracovo_cislo.isdigit():
        return False
    elif len(set(hracovo_cislo)) != 4:
        return False
    elif hracovo_cislo[0] == "0":
        return False
    else:
        return True
    
def logika_kontrolovani(generovane_cislo, hracovo_cislo):
    '''
    Vrátí počet bulls a cows.
    '''
    hracovo_cislo = str(hracovo_cislo)
    bull_cow = [0,0]
    for i,j in  zip(generovane_cislo, hracovo_cislo):
        if j in generovane_cislo:
            if j == i:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1
    return bull_cow

def pluralize(bull_cow, word):
    '''
    Pokud je počet cows nebo bull větší než jedna přidá "s" jako množné číslo.
    '''
    if bull_cow > 1:
        words = word + "s"
        return words
    else:
        return word
    
def uvod_hry():
    '''
    Funkce slouží ke generování úvodu hry a generování náhodného čísla
    '''
    generovane_cislo = generovani_cisla()
    oddelovac = "-----------------------------------------------"
    print("Hi there!")
    print(oddelovac)
    print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
    print(oddelovac)
    return generovane_cislo, oddelovac
    
#spojení funkcí dohromady   
while True:
    generovane_cislo, oddelovac = uvod_hry()
    smycka = True
    while smycka:
        hracovo_cislo = input("Enter a number: ")
        print(oddelovac)
        if je_tip_validni(hracovo_cislo):
            #počítáno od chvíle, kdy hráč vložil číslo ve správném fotmátu
            start_time = time.perf_counter() 
            pocet_pokusu = 1
            bull_and_cows = logika_kontrolovani(generovane_cislo,hracovo_cislo)
            print(f"{bull_and_cows[0]} {pluralize(bull_and_cows[0], 'bull')}, {bull_and_cows[1]} {pluralize(bull_and_cows[1], 'cow')}")
            print(oddelovac)
            while bull_and_cows[0] != 4:
                hracovo_cislo = input("Enter a number: ")
                print(oddelovac)
                if je_tip_validni(hracovo_cislo):
                    bull_and_cows = logika_kontrolovani(generovane_cislo, hracovo_cislo)
                    print(f"{bull_and_cows[0]} {pluralize(bull_and_cows[0], 'bull')}, {bull_and_cows[1]} {pluralize(bull_and_cows[1], 'cow')}")
                    print(oddelovac)
                    pocet_pokusu += 1
                else:
                    print("Wrong entered number.")
                    print(oddelovac)
            smycka = False
            end_time = time.perf_counter()
            celkovy_cas = end_time - start_time
            print(f"Correct, you've guessed the right number in {pocet_pokusu} guesses and in time of {celkovy_cas:.1f} seconds!")
        else:
            print("Wrong entered number.")
            print(oddelovac)
    restart = input("Would you like to try again? Yes nebo No? ")
    restart = restart.lower()
    if restart == "no":
        print("The game is over.")
        break
    elif restart == "yes":
        continue