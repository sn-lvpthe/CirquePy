#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# beatifulsoup

from urllib.request import urlopen
from bs4 import BeautifulSoup

# open or create CSV file
csv_file = open("email_list.csv", "w")

url = 'https://scrapebook22.appspot.com/'

response = urlopen(url).read()

#print (response)

soup = BeautifulSoup(response, 'html.parser')

print (soup.html.head.title.string)


for link in soup.findAll("a"):
    if link.string == "See full profile":
        person_url = "https://scrapebook22.appspot.com" + link["href"]
#        print(person_url)
        person_html = urlopen(person_url).read()
#        print (person_html)
        person_soup = BeautifulSoup(person_html, 'html.parser')
# instaed of print in stdout , write to the created csv file at linenumber[9]
#        print (person_soup.find('span', attrs={"class":"email"}).string)
        email = person_soup.find("span", attrs={"class": "email"}).string
        csv_file.write(email+"\n")  # \n will create a new line

# close CSV file
csv_file.close()








