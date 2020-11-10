#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 19:00:35 2020

@author: davidv
"""


class Filmoteka:
    """ filmoteka sadrži osnoven filmove """
    def __init__(self, name, godina):
        self.name = name
        self.godina = godina
        self.filmovi = []

    
    # objekt sa __len__ i __getitem__ sada mozemo vrtiti kroz for petlju
    def __len__(self):
        return len(self.filmovi)
    
    def __getitem__(self, a):
        return self.filmovi[a]
    
    def __repr__(self):
        return f'Filmoteka: {self.name},{self.godina},{self.filmovi}.'
    
    @classmethod
    def tip(cls):
        print(type(cls))


    @property
    def ispis(self):
        return self.filmovi
    
    
class Serija(Filmoteka):
    """ proširenje Filmoteke za serije sa sezonama"""
    def __init__(self, name, godina, sezona):
        super().__init__(name, godina)
        self.sezona = sezona
    
    def __repr__(self):
        return f'Serija: {self.name},{self.godina},{self.filmovi}, {self.sezona}.'
    

class Tst:
    def __init__(self, s):
        self.s = s
        
        
    def ta(self, x):
        return x+1
    
    
    @classmethod
    def ti(cls,x):
        return x+1
    

class UncountableError(ValueError):
    """ primjer obicne greske """
    def __init__(self, n):
        super().__init__(f"Invalid valid for n, {n}. n must be greater than 0.'")
    def __repr__(self):
        return "obicna UncaountableError"

while True:
    try:
        num = int(input("unesi broj: "))
    except ValueError:
        print("unos mora biti broj")
        continue
    finally:
        print(("broj {} je {}").format(num, "neparan" if num%2 else "paran"))
        odluka = input("jos jedan krug?(y/n):")
        if odluka == "n":
            break
        elif odluka != "y":
            print("Nepoznat odgovor idemo jos jedan krug :)")

            
    