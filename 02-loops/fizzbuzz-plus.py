
print ("Dit is het FIZZBUZZbiss spel!")

end = input("""\nWe gaan even na of een getal deelbaar is door 3 OF 5 OF 7.\nOf door 3 EN 5 EN 7.\n
Geef een geheel getal in tussen 1 en 100: """)

# try-except statement:
# if the code inside try fails, the program automatically goes to the except part.

try:
    end = int(end)  # convert string into number

    for num in range(1, end+1):
        if num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
            print ("FIZZBUZZBISS-359")
        elif num % 3 == 0:
            print ("\tfizz-3")
        elif num % 5 == 0:
            print ("\t\tbuzz-5")
        elif num % 7 == 0:
            print ("biss-7")

        else:
            print(num)

except Exception as e:
    print("Sorry. Ik lust alleen HELE getallen!")

