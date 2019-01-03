#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# beatifulsoup4

from urllib.request import urlopen
from bs4 import BeautifulSoup

topic_url = 'http://quotes.yourdictionary.com/theme/marriage/'
topic_html = urlopen(topic_url).read()

temp = open("topic.html", "w+")

''' 
# test om de output naar terminal in file te onderzoeken
print (topic_html)
temp.write(str(topic_html))
'''

topic_soup = BeautifulSoup(topic_html, "html.parser")
# print (topic_soup.prettify())   # even kijken of er een resultaat is dan wat opschonen
pretty = topic_soup.prettify()
# de output wordt 'prettify' weggeschreven  als controle
temp.write(str(pretty))

# find all paragraphs that have a class "quoteContent"
quotes = topic_soup.findAll('p', attrs={'class': 'quoteContent'})

# vind al de auteurs van de quote
for note in topic_soup.findAll("div", attrs={"class":"QuotesAndNotes"}):
    for name in note.findAll("a", attrs={"class":"author_link_tag"}) :

        author = name.string
        print(author)   # test bestaan auteur

'''
 Wat gebeurt er hier?
 We krijgen de lijst van de auteurs, maar die wordt steeds dezelfde bij de print van de quote.
 Meer nog, bij elke nun  verandert nde naam van de auteur!!!
 En het programma geeft een foutloze exite code 0
'''
for quote in quotes:
    print ("-- ", quote.text, "\n\t\t- ", author)

with open("qoutes_plus,txt ", "w+") as all_quotes:
    for quote in quotes:
        all_quotes.write("\n-----\n%s\n\t%s" % (quote.text, author))




