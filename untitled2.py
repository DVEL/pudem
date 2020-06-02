#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:41:41 2020

@author: davidv
"""


"""
[x] initial state of char, item => keys ...dict
[x] values => number of items, empty key, default coin : 10
[x] adding item to dict
[x] list spec item in inventory and quantity
[x] print all inventory
[x] removing item from inventory
[] adding several items at once

"""

invent = dict()


def menu():
    izbor = input("Za ispis cijelog inv 'i' za ispis pojedinog pred 'p', dodavanje 'd', micanje 'r', izlaz 'q': ")
    while izbor != "q":
        if izbor in opcije:
            nar = opcije[izbor]
            nar()
        else:
            print("nepoznata naredba!")
        
        izbor = input("Za ispis cijelog inv 'i' za ispis pojedinog pred 'p', dodavanje 'd', micanje 'r', izlaz 'q': ")
    
    if izbor == "q": print("Kraj!")


def ispis():
    for k,v in invent.items():
        print(f"predmet {k} => količina {v}")


def ispisp():
    k = input("koji predmet trzis?").lower()
    if k in invent:
        print(f"predmet {k} ima {invent[k]} u inventoriju.")


def dodavanje():
    predmet = [input("sta zelis dodati?").lower()]
     
    
    if predmet == [""]:
        ubaci()
    else:
        for i in predmet:
            try:
                kolicina = int(input("količina:"))
            except ValueError:
                kolicina = 0
                
            ubaci(i, kolicina)
    
    
def ubaci(predmet="coin", kolicina=10):
    if predmet in invent: 
        invent[predmet] += kolicina
    else:
        invent[predmet] = kolicina

   
def micanje():
    k = input("sta želiš izbrisati?:").lower()

    if k in invent: 
        v = int(input("za koliko?"))
        if invent[k] - v <= 0:
            invent[k] = 0
        else:
            invent[k] -= v
    else:
        print("Predmet nije u inventoriju!")


opcije = {
    "i" : ispis,
    "p" : ispisp,
    "d" : dodavanje,
    "r" : micanje   
    }

menu()
print(invent)