#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 22:48:21 2020

@author: davidv
"""

filmovi = []


def meni():
    
    izbor = input("Videoteka izbornik: za unos 1, za ispis 2, za pretrazivanje 3, za izlaz q: ")
    
    while izbor != "q":
        
        if izbor == "1":
            print("Unos:")
            unos()
        elif izbor == "2":
            print("Ispis:")
            ispis_gl()
        elif izbor == "3":
            print("Pretraživanje:")
            pretrazivanje_meni()
        else:
            print("Nepostojeci odabir")
            
        izbor = input("Videoteka izbornik: za unos 1, za ispis 2, za pretrazivanje 3, za izlaz q: ")
        
    if izbor == "q" : print("Izlaz!")
    
    
def unos():
    try:
        r_br = max([br["r_br"] for br in filmovi])+1
    except ValueError:
        r_br = 1
        
    naziv = input("unesite naziv filma:")
    director = input("unesite redatelja:")
    year = input("unesite godinu:")
    
    filmovi.append(dict(
                    r_br        = r_br,
                    naziv       = naziv,
                    director    = director,
                    year        = year
                    ))


def ispis_gl():
    for film in filmovi:
        ispis(film)


def ispis(el):
    print(f"""
          Redni broj: {el['r_br']}.
          naziv: {el['naziv']}
          redatelj: {el['director']}
          godina: {el['year']}        
    """)


def pretrazivanje_meni(): 
    try:
        i = 1
        print("opcije po kojima možete pretraživati:")
        for el in filmovi[0]:
            print(f"{i}.  {el:>10}")
            i += 1
            
        pretk = str(input("pretraži po:"))# ako unese broj uzmem ga -1 je indeks!!!
        pretv = input("vrijednost koja se traži:")
        
        pretrazivanje(pretk, pretv)
        
    except IndexError:
        print("Nepostoji niti jedan unos!")
    
    
def pretrazivanje(pretk, pretv):
    for el in filmovi:
        if el[pretk] == pretv:
            ispis(el)
              
            
meni()
    