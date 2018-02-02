#! /usr/bin/python3
# -*- coding: utf-8 -*-
import math

class SingleRegression:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def fit(self):
        #Compute mean
        self.x_mean = self.x.mean()
        self.y_mean = self.y.mean()

        #Compute x, y diff mean
        self.x_diff = (self.x - self.x_mean)
        self.y_diff = (self.y - self.y_mean)

        #Compute b
        self.b = (self.x_diff * self.y_diff).sum() / (self.x_diff**2).sum()
        self.a = self.y_mean - self.b * self.x_mean

        return self.a, self.b

    def residual(self):
        self.e = self.y - self.a - self.x * self.b

        return self.e

    def R_square(self):
        self.residual()
        self.R_2 = 1 - (self.e**2).sum() / (self.y_diff**2).sum()

        return self.R_2

    def s_square(self):
        self.residual()
        self.s_2 = ((self.e - self.e.mean())**2).sum() / (len(self.e) - 2)

        return self.s_2

    def SEb(self):
        self.SEb = math.sqrt(self.s_2 / (self.x_diff**2).sum())

        return self.SEb
