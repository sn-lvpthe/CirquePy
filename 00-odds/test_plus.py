# variable

a = 30
b = 20
c = 90

print(str("We berekenen uitkomst van " + str(c) + " - " + str(a) + " + " + str(b) ))
print(float(c - (a + b)))


# strings, phrases, words and quotes

a = "Waar"
b = "sta jij"
c = "hier?"

print(str("\nA is: -" + str.upper(a) + "- B is: -"+ str.upper(b) + "- en C is: -" + str.upper(c)+"-" ))
print() # empty line
print(str("\t== Een eenvoudige samenvoeging."))
print(a + b + c)

print(str.upper("\nWe bekijken reultaten van spaties en aanhalingstekens."))
print(str("+---------------+"))
print(str("De 1st vraag is:"), (a + b + c))

#de spaties tussenvoegen
print(str("\t== De spaties tussenvoegen."))
print(str("De 2de vraag is: "), (a + " " + b + " " + c))

#enkele quote
print(str("\t== De enkele quote."))
print(str("De 3de vraag is: "), ('a + " " + b + " " + c'))

#dubbele quote
print(str("\t== De dubbele quote."))
print(str("De 4DE vraag is: "), ("a + " " + b + " " + c"))

#quotes buiten de haken
print(str("\t== De quotes buiten de haken. Eerst dubbele, dan enkele"))
print(str("De 5de vraag is: "), "(a + " " + b + " " + c)")
print(str("De 6de vraag is: "), '(a + " " + b + " " + c)')
print("""\n-----------
Dat was het
-----------
""")

'''

# deleting variable
a = "\neen string"
print(a)
del a
print("\nGewiste a zal foutmelding geven\n")
print(a)

# variatie met twee var
a = int(input("Geef getal: "))
b = int(input("Tweede getal: "))

print(str(a),"en",str(b) )

print(str("Wissen van a, enkel nog b uitprinten:"), str(b) )

del a

print(str(b), ('Geeft geen probleem! a zal error geven!'))
print()
print(a)


# seconden in de week
minuut = int(60)
uur = int(60*minuut)
dag = int(24*uur)
week = int(7*dag)
seconden = int(week)
print (seconden)

# strings
print( "tot"+ " " + "ziens" + " " + str(1) + " " +"keer")
print( 3*"hallo ")
print( "tot ziens "*3 )

# modulo het is 14 uur hoe laat is het 535 uren verder
# bij kalenderberekeningen te gebruiken
print( str( (14 + 535) % 24 ) + ".00" )
'''
