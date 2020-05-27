#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 11:12:50 2020

@author: davidv
"""
while True:
    try:
        year = int(input("Unesi godine:"))
        break
    except ValueError:
        print("unos treba biti godina")


def rasp(year):
    mj  = year*12
    dan = year*365 
    raspodjela = dict(god = year, mj = mj, dan = dan)
    return raspodjela

ispis =  """
              imaš {godina} godine
              imaš {mjeseci} mjeseci
              imaš {dana} dana
        """

det = rasp(year)
#print(rasp(year))

print(ispis.format(godina=det["god"],mjeseci=det["mj"],dana=det["dan"]))


####
'''
ispis1 = f"""S obzirom da imaš {year:^5} godina
                   dakle imaš: {mj:^5} mjeseca
                  {dana:^5} dana
                  {sati:^5} sati
                  {sek} sekundi"""
print(ispis1)
# ili
                  
ispis2 = """S obzirom da imaš {year:^5} godina
                   dakle imaš: {mj:^5} mjeseca
                  {dana:^5} dana
                  {sati:^5} sati
                  {sek} sekundi"""

print(ispis2.format(year=year,mj=mj,dana=dana,sati=sati,sek=sek))

'''

