#! /usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib as mp
mp.use('Agg')
import pandas as pd

#Price to Sales
df = pd.read_csv('Dataset1.txt', sep='\t')
del df['Observ.']
plt = df.plot(x='Price', y='Sales', kind='scatter').get_figure()
plt.savefig('Dataset1_scatter.png')

#Group by Price, Avarage for Sales
grouped = df.groupby('Price')
df2 = grouped.mean()
plt = df2.plot().get_figure()
plt.savefig('Dataset1_avarage.png')
