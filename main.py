import os
# funkce pro hledaní
def hledani():
  podle_nazvu =  input("zadejte název souboru nebo složky: ")
  return podle_nazvu

# funkce pro ověření
def overeni(cesta):
    return os.path.exists(cesta)

def hledani_v_podslozkach(start_cesta, hledany_nazev):

    seznam = []
    for aktualni_cesta, slozky, soubory in os.walk(start_cesta):
        if hledany_nazev in slozky or hledany_nazev in soubory:
            cesta = os.path.join(aktualni_cesta, hledany_nazev)
            seznam.append(cesta)
    return seznam

# řídicí kod pro funkce
podle_nazvu = hledani()
start_cesta = "C:\\"
nalezeno = hledani_v_podslozkach(start_cesta, podle_nazvu)

# výpis bud s uspěsným nalezem nebo negatvním
if nalezeno:
    for index, hodnota in enumerate(nalezeno,1):
        print(index,hodnota)

    volba = input("vyber číslo:")
    index = int(volba) - 1

    os.startfile(nalezeno[index])
    print("Soubor nebo složka byla nalezena")
else:
    print("Soubor ani složka nebyly nalezeny")