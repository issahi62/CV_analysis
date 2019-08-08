import matplotlib.pyplot as plt
import math as kobby
import numpy as np
from potentiostat import Potentiostat

outfile = open("files.txt", "w")

R = 8.314  #R = gas constant in joules/mol
T = 310.15 #T = absolute temperature in Kelvin
Z = 1.0     #Z = number of elementary ions with respect to the charge in question, Assumptions is that its is Potassium ion K+
F = 96486.0 #F is the Faraday constant, equal to 96,485 coulombs·mol−1 or J·V−1·mol−1

fraction = np.divide(np.multiply(Z, F), np.multiply(R, T))
emptyarray = []

with open("data.txt", "r") as file:
     data = file.readlines()
     for lsn in data:
         items = lsn.split()
         dataline = items[1]
         floatnumbers = np.fromstring(dataline, float, sep=",")
         topcalculation = floatnumbers + fraction
         Conc = kobby.pow(kobby.e, topcalculation)
         numbers = emptyarray.append(floatnumbers)
         outfile.write(dataline + "  " + items[2])
         #print(Conc)
#plt.plot(items[1], items[0])
plt.show()
