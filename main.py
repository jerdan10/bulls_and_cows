import random
import string

def generovani_cisla():
    '''Funkce slouží k vygenerování čtyřmístného čísla'''
    first_digit = random.choice(string.digits[1:])
    remaining_digits = set(string.digits)
    remaining_digits.remove(first_digit)
    digits = [first_digit] + random.sample(remaining_digits, 3)
    n = int(''.join(digits))
    return str(n)

def je_tip_validni(hracovo_cislo): 
    if len(hracovo_cislo) != 4:
        return False
    elif not hracovo_cislo.isdigit():
        return False
    elif len(set(hracovo_cislo)) != 4:
        return False
    else:
        return True
    
def logika_kontrolovani(generovane_cislo, hracovo_cislo):
    hracovo_cislo = str(hracovo_cislo)
    bull_cow = [0,0]
    for i,j in  zip(generovane_cislo, hracovo_cislo):
        if j in generovane_cislo:
            if j == i:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1
    return bull_cow
            
generovane_cislo = generovani_cisla()
#print(generovane_cislo)
oddelovac = "-----------------------------------------------"
print("Hi there!")
print(oddelovac)
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
print(oddelovac)

smycka = True


while smycka:
    hracovo_cislo = input("Enter a number: ")
    print(oddelovac)
    if je_tip_validni(hracovo_cislo):
        pocet_pokusu = 1
        bull_and_cows = logika_kontrolovani(generovane_cislo,hracovo_cislo)
        print(f"{bull_and_cows[0]} bulls, {bull_and_cows[1]} cows")
        print(oddelovac)
        while bull_and_cows[0] != 4:
            hracovo_cislo = input("Enter a number: ")
            print(oddelovac)
            if je_tip_validni(hracovo_cislo):
                bull_and_cows = logika_kontrolovani(generovane_cislo, hracovo_cislo)
                print(f"{bull_and_cows[0]} bulls, {bull_and_cows[1]} cows")
                print(oddelovac)
                pocet_pokusu += 1
        print(f"Correct, you've guessed the right numberin {pocet_pokusu} guesses!")
        smycka = False
    else:
        
        print("Špatně zadané číslo")
        #hracovo_cislo = input("Enter a number: ")
        print(oddelovac)