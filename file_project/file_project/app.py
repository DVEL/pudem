#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 10:16:37 2020

@author: davidv
"""


def menu():
    """ upit za unos korisnika """
    prijatelji = input("Upisite barem tri prijatelja: ")
    prijatelji = set(prijatelji.split(","))
    
    if len(prijatelji) > 3:
        raise TypeError("mora biti 3 prijatelja odvojena zarezom")

    else:
        lst = ispis(prijatelji)
        for i in lst: print(i)
        upis(lst)
        
def ispis(prijatelji):
    """ ispisuje zajednicke prijatelje iz dokumenta lista_ljudi.txt i unosa korisnika """
    usp_pr = cisti(prijatelji)
    lju_pored = cisti(ljudi())
    return usp_pr.intersection(lju_pored)
    
def cisti(imena):
    """ cisti set podataka da bi se mogli usporediti """
    imena = set((i.strip()).lower() for i in imena)
    return imena

def ljudi():
    """ vraća set imena iz dokumenta lista_ljudi.txt """
    dok = open("lista_ljudi.txt", "r")
    ljudi_pored = set(dok.readlines())
    dok.close()
    return ljudi_pored

def upis(pr):
    """ upisuje imena prijatleja u dokument pr_pored.txt """
    dok = open("pr_pored.txt", "w")
    for ime in pr:
        dok.write(ime.title())
        dok.write("\n")
    dok.close()    
    
menu()