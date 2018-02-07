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

#Age to Expenditures
df = pd.read_csv('TrainExer21.txt', sep='\t')

r = ER.SingleRegression(df['Female'], df['LogWage'])
a, b = r.fit()

print('a = ', a, ' b = ', b)

e = r.residual()

#e on a constant and education
r1 = ER.SingleRegression(df['Educ'], e)
a1, b1 = r1.fit()

print('a1 = ', a1, ' b1 = ', b1)

#e on a constant and the part-time job dummy
r2 = ER.SingleRegression(df['Parttime'], e)
a2, b2 = r2.fit()

print('a2 = ', a2, ' b2 = ', b2)
