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

def filtr3():
    # Funkce pro převedení pixelu na odstín šedé
    def prevest_na_odstin_sede(pixel):
    # Pokud je pixel None (prázdný), vrátíme None
        if pixel is None:
            return None
    
    # Pokud pixel není prázdný, získáme jeho hodnotu
        r, g, b = pixel
    
    # Výpočet průměru hodnot složek (šedá)
        odstin_sede = (r + g + b) // 3
    
    # Návrat nové barvy pixelu
        return (odstin_sede, odstin_sede, odstin_sede)

# Otevření obrázku
    obrazek = Image.open("idk.jpg")

# Získání rozměrů obrázku
    sirka, vyska = obrazek.size

# Procházení všech pixelů obrázku a aplikace filtru
    for x in range(sirka):
        for y in range(vyska):
        # Získání hodnot barev pixelu na daných souřadnicích
            pixel = obrazek.getpixel((x, y))
        # Aplikace filtru na aktuální pixel
            nova_barva = prevest_na_odstin_sede(pixel)
        # Pokud je nová barva None (prázdná), přeskočíme tento pixel
            if nova_barva is not None:
            # Nastavení nové barvy pixelu
                obrazek.putpixel((x, y), nova_barva)

# Zobrazení upraveného obrázku
    obrazek.show()
    return


### menu




while True:
    cislo = int(input("""
    -------------------------------------------
        Zvolte si filtr mezi čísly 1-3:  """))

    if 1 <= cislo <= 3:
        print(cislo)
    
        if cislo == 1:
            filtr1()
    
        elif cislo == 2:
            filtr2()
        elif cislo == 3:
            filtr3()
    
        time.sleep(1)

    else:
        print("Zadali jste číslo mimo povolený rozsah (1-2).")

    


### cyklus / uživatelská volba / aktivace funkce / návrat?
