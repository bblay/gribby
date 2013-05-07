

import c_interface
from c_interface import so


class Message(object):

    def __init__(self, from_file=None, from_samples=None):
        
        if from_file:
            self.grib_handle = load(from_file)
            
        elif from_samples:
            self.grib_handle = c_interface.grib_handle_new_from_samples(from_samples)
            
        else:
            raise ValueError("Please supply a file or sample name")
        
    def load(self, file):
        pass
    
    def __getattr__(self, key):
        return c_interface.grib_get_long(self.grib_handle, key)
    
