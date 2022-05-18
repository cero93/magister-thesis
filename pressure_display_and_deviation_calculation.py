import cv2
import time
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import pylab
import itertools
import decimal
from scipy.interpolate import spline
from scipy.signal import convolve
from scipy.signal import find_peaks
data1=np.loadtxt('C:\\Python35\\PROGRAMS_fluktuacije_tlaka\\dobra\\3000_3_2,24.txt')
data2=np.loadtxt('C:\\Python35\\PROGRAMS_fluktuacije_tlaka\\srednja\\3000_3_2,21.txt')
data3=np.loadtxt('C:\\Python35\\PROGRAMS_fluktuacije_tlaka\\slaba\\3000_3_2,06.txt')
plt.title('fluktuacije tlaka na izstopu iz črpalke - 1 obrat \n pogoji obratovanja pri 3 bar in 3000/min')	
plt.xlabel('zasuk rotorja elektromotorja [°]')
plt.ylabel('absolutni tlak [bar]')
X=list(range(0,500000))
XX=np.array(X)/500000
XXX=XX*18000
bar1=data1*(1/0.36)+3
bar2=(data2/10)*(1/0.36)+3
bar3=data3*(1/0.36)+3
XXX1=XXX[0:10000]
bar11=bar1[50500:60500]
XXX2=XXX[0:10000]
bar22=bar2[31200:41200]
XXX3=XXX[0:10000]
bar33=bar3[30600:40600]
plt.plot(XXX1,bar11,linewidth=0.8)
plt.plot(XXX2,bar22,linewidth=0.8)
plt.plot(XXX3,bar33,linewidth=0.8)
MAX1=max(bar11)
MIN1=min(bar11)
avg1=sum(bar11)/len(bar11)
MAX_vse1=[MAX1]*(10000)
MIN_vse1=[MIN1]*(10000)
AVERAGE_vse1=[avg1]*(10000)
dev_y1=np.std(bar11)+avg1
dev_y_vse1=[dev_y1]*(10000)
dev_y_21=(avg1-np.std(bar11))
dev_y_2_vse1=[dev_y_21]*(10000)
p11=max(bar11[0:1428])
p12=max(bar11[1428:2857])
p13=max(bar11[2857:4285])
p14=max(bar11[4285:5713])
p15=max(bar11[5713:7141])
p16=max(bar11[7141:8569])
p17=max(bar11[8569:10000])
avg_p1=(p11+p12+p13+p14+p15+p16+p17)/7
dev_p1_=[p11,p12,p13,p14,p15,p16,p17]
dev_p1_max=max(dev_p1_)
dev_p1_max_vse=[dev_p1_max]*10000
dev_p1_min=min(dev_p1_)
dev_p1_min_vse=[dev_p1_min]*10000
delta_peaks1_max=dev_p1_max-dev_p1_min
plt.plot(XXX1,dev_p1_max_vse,linestyle='--',color='b',linewidth=1.0)
plt.plot(XXX1,dev_p1_min_vse,color='b',linewidth=1.0)
MAX2=max(bar22)
MIN2=min(bar22)
avg2=sum(bar22)/len(bar22)
MAX_vse2=[MAX2]*(10000)
MIN_vse2=[MIN2]*(10000)
AVERAGE_vse2=[avg2]*(10000)
dev_y2=np.std(bar22)+avg2
dev_y_vse2=[dev_y2]*(10000)
dev_y_22=avg2-np.std(bar22)
dev_y_2_vse2=[dev_y_22]*(10000)
p21=max(bar22[0:1428])
p22=max(bar22[1428:2857])
p23=max(bar22[2857:4285])
p24=max(bar22[4285:5713])
p25=max(bar22[5713:7141])
p26=max(bar22[7141:8569])
p27=max(bar22[8569:10000])
avg_p2=(p21+p22+p23+p24+p25+p26+p27)/7
dev_p2_=[p21,p22,p23,p24,p25,p26,p27]
dev_p2_max=max(dev_p2_)
dev_p2_max_vse=[dev_p2_max]*10000
dev_p2_min=min(dev_p2_)
dev_p1_min_vse=[dev_p2_min]*10000
delta_peaks2_max=dev_p2_max-dev_p2_min
plt.plot(XXX2,dev_p2_max_vse,linestyle='--',color='C1',linewidth=1.0)
plt.plot(XXX2,dev_p1_min_vse,color='C1',linewidth=1.0)
plt.plot(XXX2,AVERAGE_vse2,linestyle='-.',color='black',linewidth=1)
MAX3=max(bar33)
MIN3=min(bar33)
avg3=sum(bar33)/len(bar33)
MAX_vse3=[MAX3]*(10000)
MIN_vse3=[MIN3]*(10000)
AVERAGE_vse3=[avg3]*(10000)
dev_y3=np.std(bar33)+avg3
dev_y_vse3=[dev_y3]*(10000)
dev_y_23=avg3-np.std(bar33)
dev_y_2_vse3=[dev_y_23]*(10000)
p31=max(bar33[0:1428])
p32=max(bar33[1428:2857])
p33=max(bar33[2857:4285])
p34=max(bar33[4285:5713])
p35=max(bar33[5713:7141])
p36=max(bar33[7141:8569])
p37=max(bar33[8569:10000])
avg_p3=(p31+p32+p33+p34+p35+p36+p37)/7
dev_p3_=[p31,p32,p33,p34,p35,p36,p37]
dev_p3_max=max(dev_p3_)
dev_p3_max_vse=[dev_p3_max]*10000
dev_p3_min=min(dev_p3_)
dev_p3_min_vse=[dev_p3_min]*10000
delta_peaks3_max=dev_p3_max-dev_p3_min
plt.plot(XXX3,dev_p3_max_vse,linestyle='--',color='g',linewidth=1.0)
plt.plot(XXX3,dev_p3_min_vse,color='g',linewidth=1.0)
plt.grid(True)
pylab.legend(['dobra','srednja','slaba','maksimum','st. dev ','maksimum','st. dev ','povprecje','maksimum','st. dev '], loc=8, bbox_to_anchor=(0.5, -0.4),ncol=4)
pylab.savefig('fixed.png',bbox_inches='tight')
plt.show()
