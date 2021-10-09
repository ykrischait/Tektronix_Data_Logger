<h1> Tektronix Oscilloscope Data Logger </h1>

I could not find a program online that helps with logging long term data for Tektronix oscilloscopes. This program in python using PyVISA attempts to solve that for myself and hopefully others.

<h2> Pre-requisites </h2>

The following python distribution and packages are required for the program to run

1. Python 3 (tested on versions 3.7.3 and 3.9.2)
2. NumPy
3. matplotlib
4. pyVISA
5. pandas

<h2> Installation/Usage </h2>

Clone the repository into a folder of your choice and run app.py in a python 3 distribution with the required packages mentioned in the pre-requisites section.

<h2> Known quirks/bugs </h2>

1. User needs to use all the channels of the oscilloscope (assuming 4-channel). If less channels need to be used the program needs to be modified to comment out the required channels. If not done properly, a VISA Error shows up.