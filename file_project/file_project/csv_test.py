# -*- coding: utf-8 -*-
'''
import json


podaci = open("csv_pod.txt", "r")
podaci_list = podaci.readlines()
podaci.close()


linije = [i.strip() for i in podaci_list]
kljucevi = linije[0].split(",")
linije = linije[1:]

cs = [dict(zip(kljucevi, i.split(","))) for i in linije]
    
js_vozila = open("csv_u_json.txt", "w")
json.dump(cs, js_vozila)
js_vozila.close()


'''


import json
import csv
import moj_paket.file_manager as fm

with open("csv_pod.txt", "r") as f_csv:
    citac = list(csv.DictReader(f_csv))

with open("csv_u_json2.txt","w") as f_json:
    json.dump(citac, f_json)

fm.brisi("testinjo.txt")

for ime in citac:
    # fm.save_to_file(ime["name"], "testinjo.txt")
    fm.save_to_file(citac, "testinjo.txt")

print(fm.read_from_file("testinjo.txt"))

