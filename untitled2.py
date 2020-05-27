#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 16:03:12 2020

@author: davidv
"""

""" čisti listu po n kriteriju i vraća istu listu ! napraviti kao list comprehension

a = ["md",3,4,23,"kd",34,"odo","dkk",7]
print(a)

def cisti_listu(lista):
    brojac = 0
    for el in lista:
        if isinstance(el, str) == False:
            lista[brojac] = el
            brojac += 1
    del lista[brojac:]

cisti_listu(a)
print(a)
"""
