#! /usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib as mp
mp.use('Agg')
import pandas as pd
import math


df = pd.read_csv('TestExer-1-sales-round1.txt', sep='\t')
del df['Observ.']

#Scatter
plt = df.plot(x='Advert.', y='Sales', kind='scatter').get_figure()
plt.savefig('TestExer-1-sales-round1_scatter.png')
plt.clear()

#Compute mean, x=Game, y=Time
x_mean = df['Advert.'].mean()
y_mean = df['Sales'].mean()

#Compute x, y diff mean
x_diff = (df['Advert.'] - x_mean)
y_diff = (df['Sales'] - y_mean)

#Compute b
b = (x_diff * y_diff).sum() / (x_diff**2).sum()
a = y_mean - b * x_mean

print('a = ', a, ' b= ', b)


#residuals
e = df['Sales'] - a - df['Advert.'] * b

#s Square
s_square = ((e - e.mean())**2).sum() / (len(e) - 2)

#SEb
SEb = math.sqrt(s_square / (x_diff**2).sum())

print('SEb = ', SEb)

#tb
tb = b / SEb

print('tb = ', tb)

#histogram of residuals
plt = e.plot.hist(bins=19).get_figure()
plt.savefig('TestExer-1-sales-round1_histogram.png')
plt.clear()

df.drop([13,], inplace=True)

#Compute mean, x=Game, y=Time
x_mean = df['Advert.'].mean()
y_mean = df['Sales'].mean()

#Compute x, y diff mean
x_diff = (df['Advert.'] - x_mean)
y_diff = (df['Sales'] - y_mean)

#Compute b
b = (x_diff * y_diff).sum() / (x_diff**2).sum()
a = y_mean - b * x_mean

print('a = ', a, ' b= ', b)


#residuals
e = df['Sales'] - a - df['Advert.'] * b

#s Square
s_square = ((e - e.mean())**2).sum() / (len(e) - 2)

#SEb
SEb = math.sqrt(s_square / (x_diff**2).sum())

print('SEb = ', SEb)

#tb
tb = b / SEb

print('tb = ', tb)
