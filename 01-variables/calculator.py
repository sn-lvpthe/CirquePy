#strings en numbers verschillende printresultaten
'''
x = 5
y = 7

print (x + y)

x = input("Enter the value for x: ")
print (x)

y = input("Enter the value for y: ")
print (y)

print (x + y)

some_string = "Happy"
another_string = "Birthday"

print(some_string + str(" ") + another_string)

x = "3"
y = "8"
print (x + y)

x = int("3")
y = int("8")
print(x + y)


x = int(input("Enter the value for x: "))
print (x)

y = int(input("Enter the value for y: "))
print (y)

print(str("Resultaat SOM: ")+ " " +str(x + y))

'''
# calc - achter de komma (float)

x = float(input("Geef het eerste getal: "))
print("Eerste getal:",x)

y = float(input("Geef het tweede getal: "))
print ("Tweede getal:",y)

operation = input("Kies de berekening (+, -, *, / ): ")  # type: str
#print(operation)

if operation == "+":
    print("\nResultaat:",round(x + y, 3))
elif operation == "-":
    print("\nResultaat:",round(x - y, 3))
elif operation == "*":
    print("\nResultaat:",round(x * y, 3))
elif operation == "/":
    print("\nResultaat:",round(x / y, 3))


else:
    print("Je koos geen bruikbare operator.")

