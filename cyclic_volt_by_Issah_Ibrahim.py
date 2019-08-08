import csv
import numpy as np
import math as kobby
import matplotlib.pyplot as plt
from potentiostat import Potentiostat

""" ISSAH IBRAHIM BLOOD-GLUCOSE PROGRAMMING USING CYYCLIC VOLTAMMETRY 
    codes for blood-glucose analysis
                                  """

port = '/dev/tty.usbmodem3649241' # Serial Port for potentiostat device
datafile = 'CVdata.txt'       # Output file for time, curr, volt data
test_name = 'cyclic'        # The name of the test to run
curr_range = '1000uA'        # The name of the current range [-100uA, +100uA]
sample_rate = 10.0       # The number of samples/second to collect

volt_min = -0.1             # The minimum voltage in the waveform (V)
volt_max =  1.0             # The maximum voltage in the waveform (V)
volt_per_sec = 0.070        # The rate at which to transition from volt_min to volt_max (V/s)
num_cycles = 1          # The number of cycle in the waveform

# Convert parameters to amplitude, offset, period, phase shift for triangle waveform
amplitude = (volt_max - volt_min)/2.0            # Waveform peak amplitude (V) 
offset = (volt_max + volt_min)/2.0               # Waveform offset (V) 
period_ms = int(1000*4*amplitude/volt_per_sec)   # Waveform period in (ms)
shift = 0.0                                     # Waveform phase shift - expressed as [0,1] number
                                                 # 0 = no phase shift, 0.5 = 180 deg phase shift, etc.

# Create dictionary of waveform parameters for cyclic voltammetry test
test_param = {
        'quietValue' : 0.0,
        'quietTime'  : 0,
        'amplitude'  : amplitude,
        'offset'     : offset,
        'period'     : period_ms,
        'numCycles'  : num_cycles,
        'shift'      : shift,
        }

# Create potentiostat object and set current range, sample rate and test parameters
dev = Potentiostat(port)     
dev.set_curr_range(curr_range)   
dev.set_sample_rate(sample_rate)
dev.set_param(test_name,test_param)

# Run cyclic voltammetry test
t,volt,curr = dev.run_test(test_name,display='pbar',filename=datafile)

#converting results received into concentration using the Nernst equation
voltage = []
concentration = []
current = []
time = []

R = 8.314  #R = gas constant in joules/mol
T = 310.15 #T = absolute temperature in Kelvin
Z = int(input("The Num of ions with respect to charge ions: "))    #Z = number of elementary ions with respect to the charge in question, Assumptions is that its is Potassium ion K+
F = 96486.0 #F is the Faraday constant, equal to 96,485 coulombs·mol−1 or J·V−1·mol−1
fraction = np.divide(np.multiply(Z, F), np.multiply(R, T))

#print Cyclic volatammetry and checking if file is exisiting 

try:
   with open('CVdata.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        voltage.append(float(row[1]))
        concentration.append(kobby.pow(kobby.e, float(row[1])*fraction))
        time.append(float(row[0]))
        current.append(float(row[2]))
except IOError:

    print("File not found:: Try again")

finally:
    print("Cyclic Voltammetry Calculating the concentration : Developed by Issah Ibrahim")
    
      

# plot results using matplotlib
plt.figure(1)
plt.subplot(211)
plt.plot(t,volt)
plt.ylabel('potential (V)')
plt.grid('on')

plt.subplot(212)
plt.plot(t,curr)
plt.ylabel('current (uA)')
plt.xlabel('time (sec)')
plt.grid('on')

plt.figure(2)
plt.plot(volt,curr)
plt.xlabel('potential (V)')
plt.ylabel('current (uA)')
plt.grid('on')

plt.figure(3)
plt.subplot(211)
plt.plot(voltage,concentration, label='blood concentration vrs Vm')
plt.xlabel('Voltage (Vm)')
plt.ylabel('Concentration (mol/dm^-3)')
plt.title('Concentration vrs potential graph')
plt.grid('on')

plt.subplot(212)
plt.plot(concentration,current, label='blood concentration vrs current')
plt.xlabel('current (mA)')
plt.ylabel('Concentration (mol/dm^-3)')
plt.title('Concentration vrs current graph')
plt.grid('on')

plt.figure(4)
plt.plot(time,concentration, label='blood concentration vrs time')
plt.xlabel('time(ms)')
plt.ylabel('Concentration (mol/dm^-3)')
plt.title('Concentration vrs time graph')
plt.grid('on')
plt.show()
