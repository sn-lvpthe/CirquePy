#!/usr/bin/env python2.7

from Tkinter import *
import  Tkinter 
import tkMessageBox


window = Tkinter.Tk()
window.title("Dit is het FIZZBUZZ spel")
window.geometry('720x400')
#start tekst
uitleg = """\nWe gaan even na of een getal deelbaar is door 3 OF 5.\nOf door 3 EN 5.\n
Geef een GEHEEL getal in tussen 1 en 100: """
start = Tkinter.Label(window)
start = Tkinter.Label(window, text= uitleg, justify=Tkinter.CENTER, font=("Courier", 16), fg="red")
start.pack()

#end = input("""\nWe gaan even na of een getal deelbaar is door 3 OF 5.\nOf door 3 EN 5.\n
#Geef een geheel getal in tussen 1 en 100: """)

# keuze getal
end = Tkinter.Entry(window)
end.pack()



def buzzy_number():
    getal = end.get()
    getal = int(getal)

    for num in range(1, getal+1):
        if num % 3 == 0 and num % 5 == 0:
            deelbaar_door = "\n-------[ FIZZBUZZ-3-5 ]-------"
        elif num % 3 == 0:
            deelbaar_door = "\n----------[ fizz-3 ]----------"
        elif num % 5 == 0:
            deelbaar_door = "\n----------[ buzz-5 ]----------"

        else:
            deelbaar_door = "\n--------------[ " + str(num) +" ]--------------"

        tkMessageBox.showinfo("FIZZ-BUZZ-FIZZBUZZ", deelbaar_door)


# submit button
submit = Tkinter.Button(window, text="Bevestig",font=("Courier", 12), command=buzzy_number)
submit.pack()

window.mainloop()
