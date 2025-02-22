# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#%% import modules
import IPython as IP
IP.get_ipython().magic('reset -sf')
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import os as os
import numpy as np
import scipy as sp
from scipy.interpolate import griddata
from matplotlib import cm
import time
import subprocess
import pickle
import scipy.io as sio
import sympy as sym
from matplotlib import cm
import re as re
from scipy import signal
from scipy import fft
import json as json
from mpl_toolkits import mplot3d
import mpl_toolkits.mplot3d as mp3d


# set default fonts and plot colors
plt.rcParams.update({'text.usetex': True})
plt.rcParams.update({'image.cmap': 'viridis'})
plt.rcParams.update({'font.serif':['Times New Roman', 'Times', 'DejaVu Serif',
 'Bitstream Vera Serif', 'Computer Modern Roman', 'New Century Schoolbook',
 'Century Schoolbook L',  'Utopia', 'ITC Bookman', 'Bookman', 
 'Nimbus Roman No9 L', 'Palatino', 'Charter', 'serif']})
plt.rcParams.update({'font.family':'serif'})
plt.rcParams.update({'font.size': 10})
plt.rcParams.update({'mathtext.rm': 'serif'})
plt.rcParams.update({'mathtext.fontset': 'custom'}) # I don't think I need this as its set to 'stixsans' above.

cc = plt.rcParams['axes.prop_cycle'].by_key()['color']


plt.close('all')




#%% Plot data

D1 = np.loadtxt('VI1.txt',skiprows=23,delimiter=',')
tt = D1[:,0]


fft_out = []
PSD_out = []
for i in range(3):
    aa = D1[:,i+1]

    # Number of sample points
    N = D1.shape[0]
    T = tt[1]-tt[0]
    # sample spacing
    fs=1/T
    yf = sp.fft.fft(aa)
    YY = 2.0/N * np.abs(yf[0:N//2])
    xf = sp.fft.fftfreq(N, T)[:N//2]
    frequencies, psd = signal.welch(aa,fs=fs,window='hann', nperseg=6000, noverlap=None)

    fft_out.append(YY)
    PSD_out.append(psd)

YY = np.mean(np.asarray(fft_out),axis=0)
psd = np.mean(np.asarray(PSD_out),axis=0)

plt.figure()
plt.plot(xf,YY)
plt.xlabel('frequency (Hz)')
plt.ylabel('acceleration [m/s$^2$]')
plt.xlim([0,100])
plt.grid(True)
plt.tight_layout()


plt.figure()
plt.plot(frequencies, psd)
plt.xlabel('frequency (Hz)')
plt.ylabel('power spectral density [m$^2$/(s$^4 \cdot$ Hz)]')
plt.xlim([0,100])
plt.grid(True)
plt.tight_layout()



fig, ax1 = plt.subplots(figsize=(6, 3))
ax2 = ax1.twinx()
ax1.set_xlim([0,85])
ax1.plot(xf,YY,color=cc[0],lw=0.5)
ax2.plot(frequencies, psd,color=cc[1])
ax1.set_xlabel("frequency (Hz)")
ax1.set_ylabel('acceleration [m/s$^2$]', color=cc[0])
ax1.tick_params(axis="y", labelcolor=cc[0])
ax2.set_ylabel("power spectral density [m$^2$/(s$^4 \cdot$ Hz)]", color=cc[1])
ax2.tick_params(axis="y", labelcolor=cc[1])
ax1.set_ylim([0,0.003])
ax2.set_ylim([0,0.000011])
plt.tight_layout()

plt.savefig('Bridge A.jpg',dpi=200)












