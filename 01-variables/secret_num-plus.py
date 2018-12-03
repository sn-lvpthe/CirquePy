#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
secret = "22"
guess = int(input("Geef een getal tussen 1 en 30: "))
# get user's input and convert it from string into integer (number)

if guess == secret:
    print("Fantastisch, je hebt het juist! Het geheim getal was 22!")
else:
    print("Sorry, fout gegokt. We zochten niet naar het getal", str(guess))


#loops WHILE
secret = 22
guess = 0

while guess != secret:

    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("You guessed it - congratulations! It's number 22!")
    else:
        print("Sorry, your guess is not correct... Secret number is not",str(guess))
'''
#loops FOR
secret = 12

print("Je hebt VIJF kansen om een geheim nummer te vinden")

for x in range(5):
    guess = int(input("Geef een nummer in (tussen 1 en 30): "))

    if guess == secret:
        print("Gevonden. - Gefeliciteerd! - Het was [12]")
        break

    elif x <= 3:
        print("Sorry, foute keuze... het geheim nummer is niet", str(guess))
        print("Dit was poging ", str(x + 1))
    elif x == 4:
        print("Jammer, het geheim nummer is ook niet", str(guess))
        print("Dit was de", str(x + 1)+"de en laatste poging.")

'''
#loop WHILE met BREAK
secret = 22

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("You guessed it - congratulations! It's number 22 !")
        break
    else:
        print("Sorry, your guess is not correct... Secret number is not", str(guess))

#loop WHILE BREAK met aanwijzingen
secret = 22

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("You guessed it - congratulations! It's number 22!")
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
'''
