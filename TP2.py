# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:08:59 2020

@author: gabin
"""

import numpy as np
import matplotlib.pyplot as plt
import math

a=2
b=3

def dichotomie(a,b,e):
    x=(a+b)/2
    while (b-a)>e:
        if (a**(3)-4*a-8.95)*(x**(3)-4*x-8.95)<0:
            b=x
        else:
            a=x
        x=(a+b)/2
    fa=a**(3)-4*a-8.95
    fb=b**(3)-4*b-8.95
    return (fa,fb,a,b)
e=0.01
fa,fb,a,b=dichotomie(a,b,e)
print (fa)
print (fb)
print (a)
print (b)
