#!/usr/bin/python3
# -*- Coding: utf-8 -*-

from datetime import datetime
d = datetime.now().strftime("%Y-%m-%d") # de datum
fd = ("weekmenu_" + d +".txt") # creatie van het bestand met tijdstempel
print("bestaat:", fd) # controle

print ("\nMenumaker Programma.\n")

menu = {}

while True:
    dish_name = str(input("Naam van het gerecht: "))
    dish_price = float(input("Prijs van '%s': " % dish_name))  # optionally you can ttransform price from string to float
    menu[dish_name] = dish_price

    new = input("Wil je nog een gerecht opslaan? (yes/no) ")

    if new.lower() == "no" or new.lower() == "n" or new.lower() == "neen":
        break
# controle data
print ("Menu: %s" % menu)
# wegschrijven naar bestand
with open("menu.txt", "w+") as menu_file:  # open the file for writing and overwrite the previous file (w+)
        for dish in menu:
            menu_file.write("%s: %s EUR\n" % (dish, menu[dish]))  # write this text into the file and add a new line at the end (\n)

# visuele controle van het weggeschreven bestand
print ("Ons menu")
with open("menu.txt", "r") as ons_menu:
    for item in ons_menu:
        print("-- ", item)

# een wekelijks bestand met datum wegschrijven als archief en broodtekst voor publishing
with open(fd, "w+") as weekmenu:
    weekmenu.write("\n\t\t\tLekkerbekje\n\t== Het menu voor deze week ==\n")
with open(fd, "a+") as weekmenu:
    for item in menu:
        weekmenu.write("\n\t\t %s -- %s EUR\n" % (item, menu[item]))

print ("Einde van het programma.")
