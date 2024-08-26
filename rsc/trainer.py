from random import random, randrange

S = 498
N = 4
SN = S*N
SSNN = SN*(SN + 1)//2

class Trainer:
    def __init__(self):
        self.weights = [0 for i in range(SSNN)]
        
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
        
    def project(self, climb, sesh_length = 10):
        self.low_score = self._score_(climb)
        self.sesh_length = sesh_length
        
        for t in range(sesh_length):
            self.t = t
            self._send_(climb)
            
        return self.low_score
    
    def _send_(self, climb, step_size = 0.125):
        roles = climb.roles()
        new_weights = {}
        
        for x, places_x in enumerate(roles):
            for i, place_x in enumerate(places_x):
                for place_y in places_x[:i+1]:
                    u = self._square_(x,place_x)
                    v = self._square_(x,place_y)
                    l = self._symm_(u,v)
                    old_weight = self.weights[l]
                    self.weights[l] += step_size * (-1) ** randrange(2)
                    this_score = self._score_(climb)
                    if this_score < self.low_score or random() < 3**(-self.t/self.sesh_length**0.5):
                        new_weights[l] = self.weights[l]
                        self.low_score = this_score
                    self.weights[l] = old_weight
                    
            for y, places_y in enumerate(roles[:x]):
                for place_x in places_x:
                    for place_y in places_y:
                        u = self._square_(x,place_x)
                        v = self._square_(y,place_y)
                        l = self._symm_(u,v)
                        old_weight = self.weights[l]
                        self.weights[l] += step_size * (-1) ** randrange(2)
                        this_score = self._score_(climb)
                        if this_score < self.low_score:# or random() < 2.7**(-self.t/self.sesh_length**0.5):
                            new_weights[l] = self.weights[l]
                            self.low_score = this_score
                        self.weights[l] = old_weight
    
        self._update_(new_weights)
        
    def _update_(self, new_weights):
        for key,value in new_weights.items():
            self.weights[key] = value
    
    def _score_(self, climb, weights = None):
        return abs(climb.grade - self.grade(climb, weights))
    
    def _unsymm_(self, l):
        g = int(0.5*(8*l + 1)**0.5 - 0.5)
        return g, l - g*(g + 1)//2
    
    def _square_(self, x, y):
        return x*S + y
    
    def _symm_(self, x, y):
        return x*(x + 1)//2 + y
        

t = Trainer()
print

    

            
    


                        
        
        
        
        
        
        