from random import randrange

S = 498
N = 4
NN = N*(N+1)//2

class Trainer:
    def __init__(self):
        self.weights = [[[0 for k in range(S)] for j in range(S)] for i in range(NN)]
        
    def grade(self, climb, weights = None):
        roles = climb.roles()
        if weights is None:
            weights = self.weights
            
        grade = 0
        for l in range(NN):
            u, v = self._unflatten_(l)
            for x in roles[u]:
                for y in roles[v]:
                    grade += weights[l][x][y]
                            
        return grade
        
    def project(self, climb, sesh_length = 10):
        self.low_score = self._score_(climb)
        
        for t in range(sesh_length):
            self._send_(climb)
            
        return self.low_score
    
    def _send_(self, climb, step_size = 0.25):
        roles = climb.roles()
        new_weights = {}
        
        for l in range(NN):
            u, v = self._unflatten_(l)
            for x in roles[u]:
                for y in roles[v]:
                    old_weight = self.weights[l][x][y]
                    self.weights[l][x][y] += step_size * (-1) ** randrange(2)
                    this_score = self._score_(climb)
                    if this_score < self.low_score:
                        new_weights[(l,x,y)] = self.weights[l][x][y]
                        self.low_score = this_score
                    self.weights[l][x][y] = old_weight
                    
        self._update_(new_weights)
        
    def _update_(self, new_weights):
        for key,value in new_weights.items():
            l,x,y = key
            self.weights[l][x][y] = value
    
    def _score_(self, climb, weights = None):
        return abs(climb.grade - self.grade(climb, weights))
    
    def _unflatten_(self, l):
        g = int(0.5*(8*l + 1)**0.5 - 0.5)
        return g, l - g*(g + 1)//2
        
    def _copy_(self, arr):
        return [[[arr[i][j][k] for k in range(S)] for j in range(S)] for i in range(NN)]
    

            
    


                        
        
        
        
        
        
        