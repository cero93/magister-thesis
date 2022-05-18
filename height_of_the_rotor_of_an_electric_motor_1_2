import cv2
import time
import numpy as np
import matplotlib
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
import itertools
import decimal
start_time = time.time()
t=0
f= open("12383_5621_3_17_ref_200_visina_in_referenca.txt","w+")
for s in range(1,110000):
	if s in range (1,9):
		img = cv2.imread('D:\\Kolektor2_18_10_2018\\12383_5621_3_17\\12383_5621_3_1700000'+str(s)+'.png',0)
	elif s in range (10,99):
		img = cv2.imread('D:\\Kolektor2_18_10_2018\\12383_5621_3_17\\12383_5621_3_170000'+str(s)+'.png',0)
	elif s in range (100,999):
		img = cv2.imread('D:\\Kolektor2_18_10_2018\\12383_5621_3_17\\12383_5621_3_17000'+str(s)+'.png',0)
	elif s in range (1000,9999):
		img = cv2.imread('D:\\Kolektor2_18_10_2018\\12383_5621_3_17\\12383_5621_3_1700'+str(s)+'.png',0)
	elif s in range (10000,99999):
		img = cv2.imread('D:\\Kolektor2_18_10_2018\\12383_5621_3_17\\12383_5621_3_170'+str(s)+'.png',0)
	elif s in range (100000,999999):
		img = cv2.imread('D:\\Kolektor2_18_10_2018\\12383_5621_3_17\\12383_5621_3_17'+str(s)+'.png',0)	
	OSTRINA_ISKANJA_VISINE_max=256
	OSTRINA_ISKANJA_VISINE_min=254
	A=0
	B=0
	saved =[]
	y0=200 
	y1=240 	
	for x in range(25,225): 
		for y in range(y0,y1): 
			pxy=img[y,x] 
			if pxy in range (OSTRINA_ISKANJA_VISINE_min,OSTRINA_ISKANJA_VISINE_max):
				A=A+1
				saved.append(A)
		B=B+1
	popvp_vis_rot=256-y1+(y1-y0)-(A/B)
	C=0
	D=0
	saved =[]
	y00=0
	y11=40
	for xx in range(25,225):
		for yy in range(y00,y11):
			pxxyy=img[yy,xx]
			if pxxyy in range (OSTRINA_ISKANJA_VISINE_min,OSTRINA_ISKANJA_VISINE_max):
				C=C+1
				saved.append(C)
		D=D+1	
	glob_ref=256-y11+(C/D)
	delta=glob_ref-popvp_vis_rot
	print(delta)
	f.write(str(popvp_vis_rot)	+ '\t' + str(glob_ref)+ '\t'+str(delta)+'\r\n')
print("-------------- %s seconds ---------------" % (time.time() - start_time))
