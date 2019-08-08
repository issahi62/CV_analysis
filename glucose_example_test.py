from potentiostat import Potentiostat
import matplotlib.pyplot as plt

port = '/dev/tty.usbmodem3649241'    
datafile = 'data.txt'    

dev = Potentiostat(port)
dev.set_curr_range('100uA')
dev.set_sample_period(10)

name = 'chronoamp'
test_param = {
        'quietValue' : 0.0,
        'quietTime'  : 1000,
        'step'       : [ 
            (0,0.0),     # Step 1 (duration ms, voltage) 
            (29000,0.5), # Step 2 (duration ms, voltage)
            ],
        }

dev.set_param(name,test_param)
t,volt,curr = dev.run_test(name,display='pbar',filename=datafile)

plt.subplot(211)
plt.title('Voltage and current vs time')
plt.plot(t,volt)
plt.ylabel('potential (V)')
plt.ylim(0,max(volt)*1.1)
plt.grid('on')

plt.subplot(212)
plt.plot(t,curr)
plt.ylabel('current (uA)')
plt.xlabel('time (sec)')
plt.grid('on')

plt.show()

