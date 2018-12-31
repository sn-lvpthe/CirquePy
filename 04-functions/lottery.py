#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def generate_lottery_numbers(quantity):
    num_list = []

    while True:
        if len(num_list) == quantity:  # when the length of the list reaches the desired quantity, stop choosing new numbers
            break

        lot_num = random.randint(1, 50)

        if lot_num not in num_list:  # if the chosen number is not in the list yet, add it to it (this helps avoiding duplicates)
            num_list.append(lot_num)

    return num_list


def main():
    print ("Maak je loterijnummers automatisch aan!\n" )

    quantity_question = input("Hoeveel willekeurige getallen wil je: ")

    try:
        quantity_num = int(quantity_question)
        print (generate_lottery_numbers(quantity_num) )
    except ValueError:
        print ("Opgelet... Er is een aantal nodig!." )

    print ("\n\t- EINDE. -" )

if __name__ == "__main__":  # this means that if somebody ran this Python file, execute only the code below
    main()
