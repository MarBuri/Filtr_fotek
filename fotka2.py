from PIL import Image

# Otevření obrázku
obrazek = Image.open("f1.jpg")

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