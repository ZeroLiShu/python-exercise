#! /usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib as mp
mp.use('Agg')
import pandas as pd

#Age to Expenditures
df = pd.read_csv('TrainExer11.txt', sep='\t')
del df['Observ.']

#Histogram
plt = df['Age'].plot.hist(bins=26).get_figure()
plt.savefig('TrainExer11_Age_His.png')
plt.clear()

plt = df['Expenditures'].plot.hist(bins=26).get_figure()
plt.savefig('TrainExer11_Expenditures_His.png')
plt.clear()

#Scatter
plt = df.plot(x='Age', y='Expenditures', kind='scatter').get_figure()
plt.savefig('TrainExer11_scatter.png')

#Sample mean of expenditures
print('Expenditures sample mean = ', df['Expenditures'].mean())

#Sample mean of expenditures of clients' age >= 40
print('Expenditures sample mean of client\'s age >= 40', df[df['Age'] >= 40]['Expenditures'].mean())

#Sample mean of expenditures of clients' age < 40
print('Expenditures sample mean of client\'s age < 40', df[df['Age'] < 40]['Expenditures'].mean())
