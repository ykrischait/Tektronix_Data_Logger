<h1> Tektronix Oscilloscope Data Logger </h1>

I could not find a program online that helps with logging long term data for Tektronix oscilloscopes. This program in python using PyVISA attempts to solve that for myself and hopefully others.

Known quirks about the programs:

1. User needs to use all the channels of the oscilloscope (assuming 4-channel). If less channels need to be used the program needs to be modified to comment out the required channels. If not done properly, a VISA Error shows up.