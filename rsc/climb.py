class Climb:
    def __init__(self, name, roles, grade):
        self.name = name
        self.feet,\
        self.start,\
        self.middle,\
        self.finish = roles
        self.grade = grade
       
    def roles(self):
        return [self.feet,self.start,self.middle,self.finish]
    
        
        

        