#! /usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib as mp
mp.use('Agg')
import pandas as pd
import math
import os
import sys
sys.path.append(os.path.abspath('..'))

import ExerHelper.ExerRegression as ER

df = pd.read_csv('TestExer-1-sales-round1.txt', sep='\t')
del df['Observ.']

#Scatter
plt = df.plot(x='Advert.', y='Sales', kind='scatter').get_figure()
plt.savefig('TestExer-1-sales-round1_scatter.png')
plt.clear()

#Compute mean, x=Game, y=Time
r = ER.SingleRegression(df['Advert.'], df['Sales'])
a, b = r.fit()

print('a = ', a, ' b= ', b)

e = r.residual()

SEb = r.SEb()
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
r = ER.SingleRegression(df['Advert.'], df['Sales'])
a, b = r.fit()

print('a = ', a, ' b= ', b)

#SEb
SEb = r.SEb()

print('SEb = ', SEb)

#tb
tb = b / SEb

print('tb = ', tb)
