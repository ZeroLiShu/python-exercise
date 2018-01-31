#! /usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib as mp
mp.use('Agg')
import pandas as pd
import math
from ExerHelper import ExerRegression

df = pd.read_csv('TrainExer13.txt', sep='\t')

ER = ExerRegression(df['Game'], df['Winning time men'])
a, b = ER.fit()

print('a = ', a, ' b= ', b)

#R Square
R_square = ER.R_square()

print('R_square = ', R_square)

#s Square
s_square = ER.s_square()

print('s_square = ', s_square)

#SEb
SEb = ER.SEb()

print('SEb = ', SEb)

#b 95% prediction interval
lower = b - 2 * SEb
higher = b + 2 * SEb

print('95% prediction interval of b is [', lower, ',', higher, ']')

#Predict 2008, 2012, 2016
y_2008 = a + b * 19;
y_2012 = a + b * 23;
y_2016 = a + b * 27;

print('predict 2008 record = ', y_2008)
print('predict 2012 record = ', y_2012)
print('predict 2016 record = ', y_2016)
