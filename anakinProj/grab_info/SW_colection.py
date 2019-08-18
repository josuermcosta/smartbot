from anakinProj.grab_info import SW_lib

class data():
    def __init__(self):
        self.pilots = {}
        self.ships = {}
    
    def grab_pilot(self,name):
        if name in self.pilots:
            return
        else:
            aux = SW_lib.get_pilot(name)
            if(type(aux) == bool):
                self.pilots[name] = {'name':name,'vehicles':[],'status':'not_exists or bad connection.'}
            else:
                self.pilots[name] = aux
                self.pilots[name]['status'] = 'Pilot found'
            return            
        
    def grab_ships(self,pilot_name):
        self.pilots[pilot_name]['max_speed'] = 0.0
        for each in self.pilots[pilot_name]['vehicles']:
            if each in self.ships:
                continue
            else:
                aux = SW_lib.get_ship(each)
                if(type(aux) == bool):
                    self.ships[each] = {'max_atmosphering_speed':0,'status':'not_exists or bad connection.'}
                else:
                    self.ships[each] = aux
                    self.ships[each]['status'] = 'Ship found'

    def pilot_max_speed(self):
        for piloto in self.pilots:
            for ship in piloto['vehicles']:
                if piloto['max_speed'] < float(self.ships[ship]['max_atmosphering_speed']):
                    piloto['max_speed'] = float(self.ships[ship]['max_atmosphering_speed'])
            print(piloto['name'],piloto['max_speed'])