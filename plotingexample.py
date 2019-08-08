import matplotlib.pyplot as plt
import csv
import numpy as np
import math as kobby

voltage = []
concentration = []
current = []
time = []

R = 8.314  #R = gas constant in joules/mol
T = 310.15 #T = absolute temperature in Kelvin
Z = 1.0     #Z = number of elementary ions with respect to the charge in question, Assumptions is that its is Potassium ion K+
F = 96486.0 #F is the Faraday constant, equal to 96,485 coulombs·mol−1 or J·V−1·mol−1

fraction = np.divide(np.multiply(Z, F), np.multiply(R, T))

with open('data.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        voltage.append(float(row[1]))
        concentration.append(kobby.pow(kobby.e, float(row[1])+fraction))
        time.append(float(row[0]))
        current.append(float(row[2]))
      
plt.figure(1)
plt.subplot(211)
plt.plot(voltage,concentration, label='blood concentration vrs Vm')
plt.xlabel('Voltage (Vm)')
plt.ylabel('Concentration (mol/dm^-3)')
plt.title('Concentration vrs potential graph')
plt.legend("BLOOD CONCENTRATION")

plt.subplot(212)
plt.plot(concentration,current, label='blood concentration vrs Vm')
plt.xlabel('current (mA)')
plt.ylabel('Concentration (mol/dm^-3)')
plt.title('Concentration vrs current graph')
plt.legend("BLOOD CONCENTRATIOIN")

plt.figure(2)
plt.plot(time,concentration, label='blood concentration vrs Vm')
plt.xlabel('time(ms)')
plt.ylabel('Concentration (mol/dm^-3)')
plt.title('Concentration vrs time graph')
plt.legend("BLOOD CONCENTRATION")
plt.show()
