class DistanceConverter(object):
    
    def __init__(self,entry_value) -> None:
        self.entry_value = entry_value
        
    def millimeter(self):
        
        return "{:e}".format(self.entry_value*1000)
    
    def kilometer(self):
        
        return round(self.entry_value/1000,4)
    
    def miles(self):
        
        return round(self.entry_value/1609.344,4)
    
    def inches(self):
        
        return self.entry_value*39.3701
    
    def yards(self):
        
        return self.entry_value*1.094

    def astronomical_units(self):
        
        return self.entry_value/1.496e+11
    
    def feet(self):
        
        return self.entry_value*3.281
    
    def nautical_mile(self):
        
        return round(self.entry_value/1852,4)
    
    def forlong(self):
        
        return round(self.entry_value/201.2,4)

    def cubit(self):
        
        return self.entry_value*2.161
    
    