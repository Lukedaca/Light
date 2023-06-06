import pygame
import sys

# Inicializace Pygame
pygame.init()

# Nastavení rozměrů okna
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Načtení obrázku žárovky
bulb_on = pygame.image.load('light on.png')
bulb_off = pygame.image.load('light off.png')

# Změna rozměru obrázků
bulb_on = pygame.transform.scale(bulb_on, (300, 300))
bulb_off = pygame.transform.scale(bulb_off, (300, 300))

# Výpočet pozice pro obrázek
bulb_width, bulb_height = bulb_on.get_size()
bulb_x = (width - bulb_width) / 2
bulb_y = (height - bulb_height) / 2

# Stav žárovky
bulb_state = False

# Definování tlačítek
button_on = pygame.Rect(50, 50, 100, 50)  # x, y, šířka, výška
button_off = pygame.Rect(200, 50, 100, 50)

# Hlavní smyčka
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            # Zjistíme, na které tlačítko bylo kliknuto
            if button_on.collidepoint(event.pos):
                bulb_state = True
            elif button_off.collidepoint(event.pos):
                bulb_state = False

    # Vykreslení pozadí
    screen.fill((0, 0, 0))

    # Vykreslení tlačítek
    pygame.draw.rect(screen, (0, 255, 0), button_on)  # Zelené tlačítko pro zapnutí
    pygame.draw.rect(screen, (255, 0, 0), button_off)  # Červené tlačítko pro vypnutí

    # Vykreslení žárovky
    if bulb_state:
        screen.blit(bulb_on, (bulb_x, bulb_y))
    else:
        screen.blit(bulb_off, (bulb_x, bulb_y))

    # Aktualizace obrazovky
    pygame.display.flip()
