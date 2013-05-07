

import c_interface


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
        
        # is the key defined?
        if not c_interface.grib_is_defined(self.grib_handle, key):
            raise ValueError("Key {} not defined".format(key))
        
        # what is the native type of the key?
        key_type = c_interface.grib_get_native_type(self.grib_handle, key)
        
        if key_type == 1:
            result = c_interface.grib_get_long(self.grib_handle, key)
        elif key_type == 2:
            result = c_interface.grib_get_double(self.grib_handle, key)
        elif key_type == 3:
            result = c_interface.grib_get_string(self.grib_handle, key)
        else:
            raise ValueError("Unhandled key type {}".format(key_type))
        
        return result
    
