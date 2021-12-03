# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 18:16:41 2021

@author: brian
"""
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import fnmatch

########### Setting up ###############

file = r''
os.chdir(file)
cwd = os.getcwd()
print(cwd)
list1 = os.listdir(file)
print(list1)
data = pd.DataFrame()
data_MCD = pd.DataFrame()
data_Hysteresis = pd.DataFrame(np.zeros((3000, 1)))

######################################## Data cleaning ####################


for filename in list1:
    print(filename)
    if fnmatch.fnmatch(filename,'*.*'):
        pass
    elif fnmatch.fnmatch(filename,'*python*'):
        pass
    elif fnmatch.fnmatch(filename,'*Hysteresis*'):
        data = pd.read_csv(filename,delimiter='\t',header=None)
        data_Hysteresis['Field_'+filename] = data[0]
        data_Hysteresis['X_'+filename] = data[1]
        data_Hysteresis['Y_'+filename] = data[2]
        data_Hysteresis['XX_'+filename] = data[3]
        data_Hysteresis['YYY_'+filename] = data[4]
        data_Hysteresis['Hysteresis_'+filename] = data[5]
        plt.plot(data[0],data[5])
        plt.xlabel('Magnetic Field (T)')
        plt.ylabel('Raw Hysteresis signal')
        plt.title(filename)
        plt.show()
    elif fnmatch.fnmatch(filename,'*MCD*'):
        data = pd.read_csv(filename,delimiter='\t',header=None)
        data_MCD['Wavelength'] = data[0]
        data_MCD['X_'+filename] = data[1]
        data_MCD['Y_'+filename] = data[2]
        data_MCD['XX_'+filename] = data[3]
        data_MCD['YYY_'+filename] = data[4]
        data_MCD['MCD_'+filename] = data[5]
        plt.plot(data[0],data[5])
        plt.xlabel('Wavelength (nm)')
        plt.ylabel('Raw MCD signal')
        plt.title(filename)
        plt.show()
    else:
        pass
    
    
############### Plots and treatment ############

plt.xlabel('Wavelength (nm)')
plt.ylabel('Raw MCD signal')
plt.title(filename)
plt.axvline(x=556)
plt.axvline(x=604)
plt.axvline(x=663)
plt.axvline(x=761)
plt.axvline(x=845)
plt.savefig("MCD_together.pdf")
plt.show()

########################




treated_MCD_25T = data_MCD['MCD_25T'] - data_MCD['MCD_n25T']
treated_MCD_n25T = data_MCD['MCD_n25T'] - data_MCD['MCD_25T']


treated_MCD_20T = data_MCD['MCD_20T_up'] - data_MCD['MCD_n20T_up']
treated_MCD_15T = data_MCD['MCD_15T_up'] - data_MCD['MCD_n15T_up']
treated_MCD_10T = data_MCD['MCD_10T_up'] - data_MCD['MCD_n10T_up']
treated_MCD_7T = data_MCD['MCD_7T_up'] - data_MCD['MCD_n7T_up']
treated_MCD_5T = data_MCD['MCD_5T_up'] - data_MCD['MCD_n5T_up']
treated_MCD_2T = data_MCD['MCD_2T_up'] - data_MCD['MCD_n2T_up']
treated_MCD_0p5T = data_MCD['MCD_0p5T_up'] - data_MCD['MCD_n0p5T_up']



treated_MCD_n20T = -(data_MCD['MCD_20T_down'] - data_MCD['MCD_n20T_down'])
treated_MCD_n15T = -(data_MCD['MCD_15T_down'] - data_MCD['MCD_n15T_down'])
treated_MCD_n10T = -(data_MCD['MCD_10T_down'] - data_MCD['MCD_n10T_down'])
treated_MCD_n7T = -(data_MCD['MCD_7T_down'] - data_MCD['MCD_n7T_down'])
treated_MCD_n5T = -(data_MCD['MCD_5T_down'] - data_MCD['MCD_n5T_down'])
treated_MCD_n2T = -(data_MCD['MCD_2T_down'] - data_MCD['MCD_n2T_down'])
treated_MCD_n0p5T = -(data_MCD['MCD_0p5T_down'] - data_MCD['MCD_n0p5T_down'])


treated_MCD_0T = data_MCD['MCD_0T_down'] - data_MCD['MCD_0T_up']






###################################





plt.plot(data_MCD['Wavelength'],treated_MCD_25T)
plt.plot(data_MCD['Wavelength'],treated_MCD_n25T)

plt.plot(data_MCD['Wavelength'],treated_MCD_20T)
plt.plot(data_MCD['Wavelength'],treated_MCD_15T)
plt.plot(data_MCD['Wavelength'],treated_MCD_10T)
plt.plot(data_MCD['Wavelength'],treated_MCD_7T)
plt.plot(data_MCD['Wavelength'],treated_MCD_5T)
plt.plot(data_MCD['Wavelength'],treated_MCD_2T)
plt.plot(data_MCD['Wavelength'],treated_MCD_0p5T)

plt.plot(data_MCD['Wavelength'],treated_MCD_n20T)
plt.plot(data_MCD['Wavelength'],treated_MCD_n15T)
plt.plot(data_MCD['Wavelength'],treated_MCD_n10T)
plt.plot(data_MCD['Wavelength'],treated_MCD_n7T)
plt.plot(data_MCD['Wavelength'],treated_MCD_n5T)
plt.plot(data_MCD['Wavelength'],treated_MCD_n2T)
plt.plot(data_MCD['Wavelength'],treated_MCD_n0p5T)

plt.plot(data_MCD['Wavelength'],treated_MCD_0T)

plt.xlabel('Wavelength (nm)')
plt.ylabel('Raw MCD signal')
plt.title('treated MCD')
plt.savefig("treated_MCD_together.pdf")

plt.show()






###############################






data_MCD['treated_MCD_25T']= treated_MCD_25T
data_MCD['treated_MCD_n25T']= treated_MCD_n25T
                           
data_MCD['treated_MCD_20T']= treated_MCD_20T
data_MCD['treated_MCD_15T']= treated_MCD_15T
data_MCD['treated_MCD_10T']= treated_MCD_10T
data_MCD['treated_MCD_7T']= treated_MCD_7T
data_MCD['treated_MCD_5T']= treated_MCD_5T
data_MCD['treated_MCD_2T']= treated_MCD_2T
data_MCD['treated_MCD_0p5T']= treated_MCD_0p5T

data_MCD['treated_MCD_n20T']= treated_MCD_n20T
data_MCD['treated_MCD_n15T']= treated_MCD_n15T
data_MCD['treated_MCD_n10T']= treated_MCD_n10T
data_MCD['treated_MCD_n7T']= treated_MCD_n7T
data_MCD['treated_MCD_n5T']= treated_MCD_n5T
data_MCD['treated_MCD_n2T']= treated_MCD_n2T
data_MCD['treated_MCD_n0p5T']= treated_MCD_n0p5T

data_MCD['treated_MCD_0T']= treated_MCD_0T






##############################

data_MCD.to_csv("python_data_MCD")
#data_Hysteresis.to_csv("python_data_Hysteresis")

