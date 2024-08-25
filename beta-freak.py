# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 17:03:42 2024

@author: lcuev
"""
import pandas as pd
import librarian as l
N = 4
S = 498

class BetaFreak:
    def __init__(self):
        df = pd.read_csv('wts/weights_10-10.csv')
        self.weights = df.values.tolist()
        
        
    def grade(self, climb):
        grade = 0
        roles = climb.roles()    
        
        for i, rx in enumerate(roles):
            for j, ry in enumerate(roles[:i + 1]):
                u = self.flatten(i,j)
                for n, px in enumerate(rx):
                    for py in rx[:n + 1]:
                        v = self.flatten(px,py)
                        grade += self.weights[u][v]
                        
        return grade
    
    def flatten(self,px,py):
        return px * (px + 1) // 2 + py
    
    
lib = l.Librarian()
bf = BetaFreak()
climb = lib.look_up('Rose Drop')
print('actual grade:', climb.grade)
print('est. grade:', bf.grade(climb))