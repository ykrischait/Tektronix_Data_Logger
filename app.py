################################
#   Oscilloscope Data Logger   #
# Written by Krishna Chaitanya #
#         Loh Lab 2021         #
################################

# Importing Packages 

import matplotlib.pyplot as plt
import numpy as np
from Oscilloscope import Oscilloscope
import time 
import pandas as pd
from parameters import * 
import datetime

# Initializing File Path
filepath = Data_FilePath+'\\'+Data_FileName

file = open(filepath, 'w+') # opens file and creates new one if the file does not exist

#Calling the Oscillscope Class
osc = Oscilloscope()

#Initializing logging arrays
volts1 = np.array([])
volts2 = np.array([])
volts3 = np.array([])
volts4 = np.array([])

#Setting up loop parameters
time_end = time.time()+ (time_duration*60*60)
loop_counter = 0
time_counter = 0
print(f"Logging Data. Please wait...")
while time.time() < time_end:
    now = datetime.datetime.now()
    print("")
    print (f'Loop {loop_counter+1}: {now.strftime("%Y-%m-%d %H:%M:%S")}')
    start = time.time()

    #Getting data from all the channels
    v1 = osc.get_channel_data_fast(1)
    v2 = osc.get_channel_data_fast(2)
    v3 = osc.get_channel_data_fast(3)
    v4 = osc.get_channel_data_fast(4)
    volts1 = np.append(volts1,v1)
    volts2 = np.append(volts2,v2)
    volts3 = np.append(volts3,v3)
    volts4 = np.append(volts4,v4)
    t_axis = np.linspace(time_counter,(loop_counter+1)*time_scale,len(v1))
    #Appending data to file
    df = pd.DataFrame(np.hstack((t_axis[:,None], v1[:,None], v2[:,None], v3[:,None], v4[:,None])))
    df.to_csv(file,mode='a',header=False)
    end = time.time()
    time.sleep(time_scale-(end-start))
    end2 = time.time()
    print(f"Runtime = {end2-start} seconds")
    loop_counter = loop_counter+1
    time_counter = time_counter+time_scale

#Closing file for editing access outside python
file.close()

#Plotting all data
time_axis = np.linspace(0,loop_counter*time_scale,len(volts1))

#Storing Data in a CSV file after all data is logged#
# df = pd.DataFrame(np.hstack((time_axis[:,None], volts1[:,None], volts2[:,None], volts3[:,None], volts4[:,None])))
# df.to_csv(filepath)

plt.plot(time_axis,volts1)
plt.plot(time_axis,volts2)
plt.plot(time_axis,volts3)
plt.plot(time_axis,volts4)
plt.xlabel('Time Elapsed (seconds)')
plt.ylabel('Voltage (V)')
plt.title('Oscilloscope Data Plot')
plt.show()
