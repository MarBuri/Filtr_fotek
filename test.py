from PIL import Image
import time
def filtr1():
    # Otevření obrázku
    obrazek = Image.open("idk.jpg")

# Inverzní změna barev pro každý pixel
    obrazek = Image.eval(obrazek, lambda x: 255 - x)

# Zobrazení upraveného obrázku
    obrazek.show()

    return


def filtr2():
    # Otevření obrázku
    obrazek = Image.open("idk.jpg")

# Získání rozměrů obrázku
    sirka, vyska = obrazek.size

# Procházení všech pixelů obrázku
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
        # Získání hodnot barev pixelu
            r, g, b = obrazek.getpixel((x, y))
        
        # Modifikace červené a modré složky
            obrazek.putpixel((x, y), (r, g, r))
        
        # Přechod na další řádek
            y += 1
    # Přechod na další sloupec
        x += 1

# Zobrazení upraveného obrázku
    obrazek.show()

    return

### menu




while True:
    cislo = int(input("""
    -------------------------------------------
        Zvolte si filtr mezi číslem 1 a 2:  """))

    if 1 <= cislo <= 2:
        print(cislo)
    
        if cislo == 1:
            filtr1()
    
        if cislo == 2:
            filtr2()
    
        time.sleep(1)

    else:
        print("Zadali jste číslo mimo povolený rozsah (1-2).")

    


### cyklus / uživatelská volba / aktivace funkce / návrat?
