import pandas as pd
from parameters import *
import matplotlib.pyplot as plt 
import numpy as np
df = pd.read_csv(Data_FilePath+'\\'+Data_FileName,delimiter=',',header=None)
df.columns=['Index','Time','Ch1','Ch2','Ch3','Ch4'] 
# plt.plot()
# print(df.head())
df=df.astype(float)

df.plot(subplots=True, figsize=(8, 8)); plt.legend()
# df.plot(x='Time',y=['Ch1','Ch2','Ch3','Ch4'])

df.loc[(df.Ch1 < -0.02),'Ch1']=np.nan #Provide low range to ignore the blanks in oscilloscope
df.loc[(df.Ch2 < -0.002),'Ch2']=np.nan
df.loc[(df.Ch3 < -0.002),'Ch3']=np.nan
df.loc[(df.Ch4 < -0.002),'Ch4']=np.nan
# df.drop(df.index[df['Ch1'] < -0.025], inplace = True)
df.plot(subplots=True, figsize=(8, 8)); plt.legend()
# plt.ylim([-0.025,0.025])
# plt.close(2)
plt.show()