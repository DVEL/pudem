#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 11:43:22 2020

@author: davidv
"""


import numpy as np
import matplotlib.pyplot as plt

# fig = plt.figure()
# ax = plt.axes()

fig, ax =  plt.subplots()

plt.style.use("seaborn-whitegrid")

x = np.linspace(5, 28, 120)

ax.plot(x,x+6,"--c", label="gornja")
ax.plot(x, np.cos(x), ":", label="donja")


"""
ax.set_ylim(-5,45)
ax.set_xlim(5,31)
ax.set_title("Testiranje library-a")
ax.set_xlabel("standardna ljestvica")
ax.set_ylabel("skala")
ax.legend()
"""


ax.set(
       xlim = (5,31),
       ylim = (-5,45),
       xlabel = "standardna",
       ylabel = "skala",
       title = "Testiranje library-a",
       )

ax.legend()

plt.show()