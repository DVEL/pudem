#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 11:57:55 2020

@author: davidv
"""
import pprint
pp = pprint.PrettyPrinter()

users = [
       { "id": 0, "name": "Hero" },
       { "id": 1, "name": "Dunn" },
       { "id": 2, "name": "Sue" },
       { "id": 3, "name": "Chi" },
       { "id": 4, "name": "Thor" },
       { "id": 5, "name": "Clive" },
       { "id": 6, "name": "Hicks" },
       { "id": 7, "name": "Devin" },
       { "id": 8, "name": "Kate" },
       { "id": 9, "name": "Klein" }
]


friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


for user in users:
    user["friends"] = []


def dodaj(x,y):
    """

    Parameters
    ----------
    arg : list
        Takes tuples with friend connections and add them accordingly to friends.

    Returns
    -------
    None.

    """
    for user in users:
        if user["id"] == x: 
            user["friends"].append(y)
        elif user["id"] == y:
            user["friends"].append(x)


def number_of_friends(user):
    """ number of friends, a person has """
    return len(user["friends"])


def total_connections():
    """ ukupan broj prijatelja koji postoje """
    total_connections = sum(number_of_friends(user) for user in users)
    return total_connections


def av_connections():
    """ average number of connections """
    average_connections = total_connections() / len(users)
    return average_connections    

    
def povezanost():
    """ lista povezanosti po imenima """
    p_povezanost = [(user["name"], number_of_friends(user)) for user in users]
    s_povezanost = sorted(p_povezanost,
                          key=lambda user : user[1],
                          reverse=True)
    return(s_povezanost)

for connection in friendships:
    x,y = connection
    dodaj(x,y)

def foaf():
    lista_frendova = []
    for user in users:
        lista_frendova.append(user["name"])
        for friend in user["friends"]:
            lista_frendova.append(friend["friends"])
    print(lista_frendova)

print(foaf())
'''
print(f"""
        ukupna povezanost: {total_connections()},
        prosječna povezanost: {av_connections()},
        povezanost pojedinaca: {povezanost()}
      """)
'''
