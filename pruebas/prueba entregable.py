# import cv2 as cv

# src1=cv.imread('cell')


# retval, response	=	cv.phaseCorrelate(	src1, src2[, window]	)

from __future__ import print_function
from __future__ import division
import cv2 as cv
import cv2
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import argparse
# parser = argparse.ArgumentParser(description='Code for Histogram Comparison tutorial.')
# parser.add_argument('D\USUARIO\Desktop\Parcial4Info\Imagenes\bacr.jpg', help='Path to input image 1.')
# parser.add_argument('D\USUARIO\Desktop\Parcial4Info\Imagenes\bacr.jpg', help='Path to input image 2.')
# parser.add_argument('D\USUARIO\Desktop\Parcial4Info\Imagenes\bacr.jpg', help='Path to input image 3.')
# args = parser.parse_args()
src_base = cv.imread('blanco.jpg')
src_test1 = cv.imread('cell2.png')
src_test2 = cv.imread('cell.jpeg')


if src_base is None or src_test1 is None or src_test2 is None:
    print('Could not open or find the images!')
    exit(0)
hsv_base = cv.cvtColor(src_base, cv.COLOR_BGR2HSV)
hsv_test1 = cv.cvtColor(src_test1, cv.COLOR_BGR2HSV)
hsv_test2 = cv.cvtColor(src_test2, cv.COLOR_BGR2HSV)
hsv_half_down = hsv_base[hsv_base.shape[0]//2:,:]
h_bins = 50
s_bins = 60
histSize = [h_bins, s_bins]
# hue varies from 0 to 179, saturation from 0 to 255
h_ranges = [0, 180]
s_ranges = [0, 256]
ranges = h_ranges + s_ranges # concat lists
# Use the 0-th and 1-st channels
channels = [0, 1]
hist_base = cv.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
cv.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
hist_half_down = cv.calcHist([hsv_half_down], channels, None, histSize, ranges, accumulate=False)
cv.normalize(hist_half_down, hist_half_down, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
hist_test1 = cv.calcHist([hsv_test1], channels, None, histSize, ranges, accumulate=False)
cv.normalize(hist_test1, hist_test1, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
hist_test2 = cv.calcHist([hsv_test2], channels, None, histSize, ranges, accumulate=False)
cv.normalize(hist_test2, hist_test2, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
for compare_method in range(4):
    base_base = cv.compareHist(hist_base, hist_base, compare_method)
    base_half = cv.compareHist(hist_base, hist_half_down, compare_method)
    base_test1 = cv.compareHist(hist_base, hist_test1, compare_method)
    base_test2 = cv.compareHist(hist_base, hist_test2, compare_method)
    print('Method:', compare_method, 'Perfect, Base-Half, Base-Test(1), Base-Test(2) :',\
          base_base, '/', base_half, '/', base_test1, '/', base_test2)

cv2.namedWindow('Ventana', 0)  
cv2.imshow('Ventana',hsv_base )       
cv2.waitKey(0)                
cv2.destroyAllWindows()