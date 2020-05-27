#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 21:22:19 2020

@author: davidv
"""
''' posjecene zemlje

zemlje = dict()

unos = input("""
            Welcome to country visited program:
            
            If you wish to enter new entry press a
            if you wish to quite enter q:""")
            
while unos != "q": 
    
    if unos == "a": 
        koris_zemlja = input("Naziv zemlje je:")
        datum = input("Datum posjete:")
        zemlje["zemlja"] = koris_zemlja datum))

    elif unos == "i":
        for zem in zemlje:
            print(f"\n {zem[0]} posjećena {zem[1]}")

    else:
        print("nepostojeći unos")
        
    unos= input("Sljedeće (a, i ili q): ")
'''
""" dvije while za pogadjanje broja

my_number = 5

def pisi():
    while True:
        try:
            unos = int(input("Enter a number: "))
            return unos
        except ValueError:
            print("Treba biti broj!")


while True:
    user_number = pisi()
    
    if   my_number == user_number:
            print("Pogodio si!")
            break
    elif my_number < user_number:
            print("Prevelik je tvoje broj!")
    elif my_number > user_number:
            print("Premali broj si unio!")
    else:
        raise "Koja greska?"

"""

''' lutrija
lottery_numbers = {13, 21, 22, 5, 8}

igraci = [
    {
     "name": "Petar",
     "numbers": {1,2,3,4,5}
     },
    {
     "name": "Marin",
     "numbers": {13,21,22,23,24}
     }
]

for igrac in igraci:
    broj = len(igrac["numbers"].intersection(lottery_numbers))
    kraj = "broj" if broj == 1 else "broja"
    print(f"Igrač {igrac['name']} je pogodio {broj} {kraj}.")
'''

""" prim brojevi ... primitivan način
while True:
    try:
        s = int(input("do kojeg broja da izračunamo primove?:"))
        break
    except ValueError:
        print("mora biti cijeli broj.")
        
for x in range(2,s+1):
    for a in range(2,x):
        if not x % a:
            print(f"{x} nije prim")
            break
    else:
        print(f"{x} je prim broj")
"""

"""lutrija 2
import random

broj_lutrij  = set(random.sample(range(22), 6))

igraci = [
    {"ime": "Petar", "brojevi" : {1,2,3,4,5,6}},
    {"ime": "Marko", "brojevi" : {10,12,13,14,15,16}},
    {"ime": "Marin", "brojevi" : {7,8,9,10,5,6}},
    {"ime": "Juda", "brojevi" : {1,2,11,14,9,6}},
    {"ime": "Ivan", "brojevi" : {18,12,19,14,15,16}}
     ]


for x in igraci:
    igracevi_brojevi = x["brojevi"]
    pogodjenih_br = igracevi_brojevi.intersection(broj_lutrij)
    iznos = len(pogodjenih_br)*100
    print(f"{x['ime']} je osvojio/la {iznos} kuna" )

"""

