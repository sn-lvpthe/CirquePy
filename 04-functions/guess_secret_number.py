#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def main():
    secret = random.randint(1, 50)

    while True:
        guess = int(input("Zoek een geheim getal tussen 1 an 50: "))

        if guess == secret:
            print( "Geraden - We zochten het getal %s :)" % secret)
            print("Tot ziens.")
            break
        elif guess > secret:
            print ("Ai, dit is te hoog geraden.. Probeer nog 'n keer.")
        elif guess < secret:
            print( "Ai, dit is te laag geraden.. Probeer nog 'n keer.")


if __name__ == "__main__":  # this means that if somebody ran this Python file, execute only the code below
    main()
