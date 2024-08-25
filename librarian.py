import sqlite3 as sql
import rsc.climb as c

class LibError(Exception):
    pass

N = 4
    
class Librarian:
    roles = {5:1,6:2,7:3,8:0}

    def __init__(self):
        self.con = sql.connect('dbs/Tension.sqlite')
        self.cur = self.con.cursor()
        self.places = self._places_()
        
    def __del__(self):
        self.con.close()
        
    def get_climb(self, name):
        query = f"""select climbs.frames,climb_stats.difficulty_average from climbs 
        inner join climb_stats on climbs.uuid=climb_stats.climb_uuid 
        where climbs.layout_id=11 and climb_stats.angle=40 and climbs.name="{name}";"""
        try:
            fetch =  self.cur.execute(query).fetchone()
            roles = self._unpack_(fetch[0])
            grade = fetch[1]
        except:
            raise LibError
        result = c.Climb(name, roles, grade)
        return result
    
    def get_names(self):
        query = """select name from climbs where layout_id=11 and angle=40;"""
        result = []
        names =  self.cur.execute(query).fetchall()
        for name in names:
            result += [name[0]]
        return result
        
    def _unpack_(self, roles):
        result = [[] for j in range(N)]
        
        for pr in roles[1:].split('p'):
            place, role = pr.split('r')
            place, role = int(place), int(role) 
            role = self.roles[role]
            index = self.places[place]
            result[role] += [index]
            
        return result
    
    def _places_(self):
        result = {}
        query = """select id from placements where layout_id=11;"""
        
        fetches = self.cur.execute(query).fetchall()
        for i,fetch in enumerate(fetches):
            result[fetch[0]] = i
        return result
    
            
    

        
