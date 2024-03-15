from PIL import Image

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