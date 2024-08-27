import time
MAX = 130

class Pb:
    def __init__(self, it, prefix='', suffix='', size=60):
        self.it = it
        self.pref = prefix
        self.suff = suffix
        self.size = size
    
    def __iter__(self): 
        count = len(self.it)
        start = time.time() # time estimate start
        def show(j):
            x = int(self.size*j/count)
            # time estimate calculation and string
            remaining = ((time.time() - start) / j) * (count - j)        
            mins, sec = divmod(remaining, 60) # limited to minutes
            time_str = f"{int(mins):02}:{sec:03.1f}"
            end_string = f"{self.pref}[{'■'*x}{('-'*(self.size-x))}] ({time_str}) {self.suff}"
            if len(end_string) >= MAX:
                end_string = end_string[:MAX]
            print(end_string, end='\r', flush=True)
        show(0.1) # avoid div/0 
        for i, item in enumerate(self.it):
            yield item
            show(i+1)
        print('\r',flush=True,end='\r')
        
    def complete(self,string):
        if len(string) < MAX:
            string += ' ' * (MAX - len(string))
        else:
            string = string[:MAX]
        print(string,flush=True)
        
        
    

        
        

    


