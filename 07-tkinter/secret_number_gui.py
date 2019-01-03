#!/usr/bin/env python2.7
# _*_ coding: utf-8 _*_

import Tkinter
import tkMessageBox
import random

secret = random.randint(1, 100)

window = Tkinter.Tk()
window.title("Welkom bij ons raadspel")
window.geometry('400x240')

# greeting text
greeting = Tkinter.Label(window, text="Raad een geheim nummer!\nTussen 1 en 100", font=("Courier", 20), fg="green" )
greeting.pack()

# guess entry field
guess = Tkinter.Entry(window)
guess.pack()


# check guess
def check_guess():
    if int(guess.get()) == secret:
        result_text = "CORRECT! Maar er is geen prijs."
    elif int(guess.get()) > secret:
        result_text = "FOUT! Te hoog gegokt."
    else:
        result_text = "FOUT! Te laag gegokt."

    tkMessageBox.showinfo("Je keuze is ...", result_text)  # message box

# submit button
submit = Tkinter.Button(window, text="Bevestig",font=("Courier", 16), command=check_guess)  # check_guess, not check_guess()
submit.pack()

window.mainloop()
