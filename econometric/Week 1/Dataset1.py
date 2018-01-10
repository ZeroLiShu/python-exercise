#! /usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib as mp
mp.use('Agg')
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

#Price to Sales
df = pd.read_csv('Dataset1.txt', sep='\t')
del df['Observ.']

regr = linear_model.LinearRegression()
regr.fit(df['Price'].values.reshape(-1, 1), df['Sales'])
b, a = regr.coef_, regr.intercept_

#Price = 50, 58
print('Price = 50, Sales = ', a + b * 50)
print('Price = 58, Sales = ', a + b * 58)

plt.scatter(df['Price'], df['Sales'], color='blue')
plt.plot(df['Price'], regr.predict(df['Price'].values.reshape(-1, 1)), color='red')
plt.savefig('Dataset1_scatter.png')

#Group by Price, Avarage for Sales
grouped = df.groupby('Price')
df2 = grouped.mean()
plt2 = df2.plot().get_figure()
plt2.savefig('Dataset1_avarage.png')
