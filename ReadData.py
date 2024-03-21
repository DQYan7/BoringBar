import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

SolidBar_1_raw = pd.read_excel('./DQ_BoringBar/SolidBar_1/SolidBar_1_FRF.xlsx')

SolidBar_1_x = SolidBar_1_raw['Freq(Hz)']
SolidBar_1_y_real = SolidBar_1_raw['Real(m/N)']
SolidBar_1_y_img  = SolidBar_1_raw['Imag(m/N)']

fig,ax = plt.subplots()
ax.plot(SolidBar_1_x,SolidBar_1_y_real,
        SolidBar_1_x,SolidBar_1_y_img)
ax.set_xscale('log')

plt.show()
