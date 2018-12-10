#!/usr/bin/python3
# -*- Coding: utf-8 -*-

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

# een wekelijks bestand wegschrijven als archief en broodtekst voor publishing
with open("weekmenu.txt", "w+") as weekmenu:
    weekmenu.write("\n\t\t\tLekkerbekje\n\t== Het menu voor deze week ==\n")
with open("weekmenu.txt", "a+") as weekmenu:
    for item in menu:
        weekmenu.write("\n\t %s -- %s EUR" % (item, menu[item]))

print ("Einde van het programma.")
