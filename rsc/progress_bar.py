# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 01:03:44 2024

@author: lcuev
"""
import sys
L = 50


def progress_bar(name, score, iter, max):
    pgs = L*iter//max

    print('[' + '▮'*pgs + '-' * (L - pgs) + ']', end = '\r',file = sys.stdout, flush = True)

