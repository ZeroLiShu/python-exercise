#! /usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib as mp
mp.use('Agg')
import pandas as pd

df = pd.read_csv('TrainExer13.txt', sep='\t')

#Compute mean, x=Game, y=Time
x_mean = df['Game'].mean()
y_mean = df['Winning time men'].mean()

#Compute x, y diff mean
x_diff = (df['Game'] - x_mean)
y_diff = (df['Winning time men'] - y_mean)

#Compute b
b = (x_diff * y_diff).sum() / (x_diff**2).sum()
a = y_mean - b * x_mean

print('a = ', a, ' b= ', b)

#R Square
e = df['Winning time men'] - a - df['Game'] * b
e_square = e**2
R_square = 1 - e_square.sum() / (y_diff**2).sum()

print('R_square = ', R_square)

#s Square
s_square = ((e - e.mean())**2).sum() / (len(e) - 2)

print('s_square = ', s_square)
