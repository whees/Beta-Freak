# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 17:03:42 2024

@author: lcuev
"""
import csv
import librarian as lib

N = 4
NN = N * (N + 1)//2
S = 498

class BetaFreak:
    def __init__(self):
        in_path = 'wts/weights_1-100.csv'
        with open(in_path) as f:
            reader = csv.reader(f)
            self.weights = list(reader)[0]
        
        for i, weight in enumerate(self.weights):
            self.weights[i] = float(weight)
        
        
    def grade(self, climb, weights = None):
        if weights is None:
            weights = self.weights
            
        roles = climb.roles()
        grade = 0
        for x, places_x in enumerate(roles):
            for i, place_x in enumerate(places_x):
                for place_y in places_x[:i+1]:
                    u = self._square_(x,place_x)
                    v = self._square_(x,place_y)
                    l = self._symm_(u,v)
                    grade += weights[l]
                    
            for y, places_y in enumerate(roles[:x]):
                for place_x in places_x:
                    for place_y in places_y:
                        u = self._square_(x,place_x)
                        v = self._square_(y,place_y)
                        l = self._symm_(u,v)
                        grade += weights[l]
                            
        return grade
    
    def _square_(self, x, y):
        return x*S + y
    
    def _symm_(self, x, y):
        return x*(x + 1)//2 + y
    
    
l = lib.Librarian()
bf = BetaFreak()

        

climb = l.get_climb('pur')
print('actual grade:', climb.grade)
print('est. grade:', bf.grade(climb))

