#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import sys

def calc_egr(phi,k,phie,n,h=3.76):
    """
    Routine solves mass fraction composition of mixture. You need to 
    define following parameters:
        phi  - equivalence ratio (always 0)
        k    - mass fraction of EGR gases
        phie - equivalence ration of EGR
        n    - number of carbon atoms in fuel (C_n H_{2n+2})
        h    - volume ratio N2/O2 in oxydizer
        Output: mf - array with 4 elements (CO2, H2O, O2, N2)
    """
    mf = np.zeros(4,'d')
    wm = np.array([44.,18.,32.,28.])
    a = np.zeros(4,'d')
    a[0] = phie * n
    a[1] = phie * (n + 1)
    a[2] = (1.-phie) * (1.5*n+0.5)
    a[3] = h * (1.5*n+0.5)
    a *= wm
    asumm = np.sum(a)
    a *= k / asumm
    b = np.zeros(4,'d')
    b[2] = wm[2] / (wm[2] + h * wm[3])
    b[3] = wm[3] * h / (wm[2] + h * wm[3])
    b *= (1.0-k)
    a += b
    
    return a

if __name__ == "__main__":
    print calc_egr.__doc__
    phi = 0.0
    k = 0.233
    phie = 0.5606
    n = 12
    h = 3.76
    y = np.zeros(4,'d')
    names = ['CO2','H2O','O2','N2']
    y = calc_egr(phi,k,phie,n,h)
    for i,nm in enumerate(names):
        print nm,y[i]
    print "summ = %e" %(np.sum(y))
