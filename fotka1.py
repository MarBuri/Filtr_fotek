from PIL import Image

# Otevření obrázku
obrazek = Image.open("f1.jpg")

# Inverzní změna barev pro každý pixel
obrazek = Image.eval(obrazek, lambda x: 255 - x)

# Zobrazení upraveného obrázku
obrazek.show()