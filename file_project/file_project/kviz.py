# -*- coding: utf-8 -*-

def kviz():
    print("dobrodošli u kviz.")
    ime = input("vaše ime je:")
    print("krenimo:")
    
    pitanja = open("kviz.txt", "r")
    lista_pitanja = [x.strip() for x in pitanja.readlines()]
    pitanja.close()
    
    rezultat = 0
    total = len(lista_pitanja)
    
    for pitanje in lista_pitanja:
        p,o = pitanje.split("=")
        odg = input(f"{p} ")
        if odg == o:
            rezultat += 1
    
    rez = open("rezultat.txt", "a")
    rez.write(f"{ime}: {rezultat}/{total}\n")
    rez.close()
    
kviz()    