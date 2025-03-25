#tento kód nahoře tady nech a neopakuj ho
import random

#podokončení programu se zeptejte, zda chce uživatel celý program opakovat
#pokud ano spusťte znovu pokud ne ukončete program


zvirata = [
    "kočka", "pes", "slon", "žirafa", "lev", "tygr", "sova",
    "tučňák", "ježek", "králík", "myš", "medvěd", "vlk", "liška",
    "klokan", "chameleon", "opice", "panda", "lenochod", "velbloud"
]

nahodne_zvire = random.choice(zvirata)
print(f'Náhodné zvíře: {nahodne_zvire}')
 
while True:
    nahodne_zvire = random.choice(zvirata)
    print(f'Náhodné zvíře: {nahodne_zvire}')
    
    opakovat = input("Chcete program spustit znovu? (ano/ne): ").strip().lower()
    if opakovat != "ano":
        print("Program ukončen.")
        break