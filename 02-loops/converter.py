

print("-----------\nOmzetten van lengte-eenheden - Kilometers naar miles.\n")

while True:
    print ("Geef de kilometers in die naar miles moeten omgezet.\nGebruik alleen getallen!")
    km = str(input("Kilometers: "))

    try:
        km = float(km.replace(",", "."))  # replace comma with dot, if user entered a comma

        miles = round(km * 0.621371, 2)

        print ("----> [{0}] kilometers zijn gelijk aan [{1}] miles. ---".format(km, miles))
    except Exception as e:
        print ("Opgelet gebruik enkel getallen! Geen tekst.")

    choice = input("Wil je nog een omzetting doen? y/n : ")

    if choice.lower() != "y" and choice.lower() != "yes":
        break

