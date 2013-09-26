

import c_interface


class GribMessage(object):

    def __init__(self, from_samples=None, from_file=None):
        
        if from_file:
            self.grib_handle = load(from_file)
            
        elif from_samples:
            self.grib_handle = c_interface.grib_handle_new_from_samples(from_samples)
            
        else:
            raise ValueError("Please supply a file or sample name")
        
    def load(self, file):
        assert(0)
    
    def __getattr__(self, key):
        
        # is the key defined?
        if not c_interface.grib_is_defined(self.grib_handle, key):
            raise ValueError("Key {} not defined".format(key))
        
        # what is the native type of the key?
        key_type = c_interface.grib_get_native_type(self.grib_handle, key)
        
        if key_type == 1:
            result = self.get_long(key)
        elif key_type == 2:
            result = self.get_double(key)
        elif key_type == 3:
            result = self.get_string(key)
        else:
            raise ValueError("Unhandled key type {}".format(key_type))
        
        return result
    
    def __setattr__(self, key, value):

        # Are we trying to set an actual instance attribute of this object?
        if key in ["grib_handle"]:
            object.__setattr__(self, key, value)
            return

        # is the key defined in the grib message?
        if not c_interface.grib_is_defined(self.grib_handle, key):
            raise ValueError("Key {} not defined".format(key))
        
        # what is the native type of the key?
        key_type = c_interface.grib_get_native_type(self.grib_handle, key)
        if key_type == 1:
            c_interface.grib_set_long(self.grib_handle, key, value)
        elif key_type == 2:
            c_interface.grib_set_double(self.grib_handle, key, value)
        elif key_type == 3:
            c_interface.grib_set_string(self.grib_handle, key, value)
        else:
            raise ValueError("Unhandled key type {}".format(key_type))

#     # These methods let us set values from specific types.
#     # How useful is this though?
#     def get_long(self, key):
#         return c_interface.grib_get_long(self.grib_handle, key)
#     
#     def get_double(self, key):
#         return c_interface.grib_get_double(self.grib_handle, key)
#     
#     def get_string(self, key):
#         return c_interface.grib_get_string(self.grib_handle, key)
#     
#     def set_long(self, key, value):
#         c_interface.grib_set_long(self.grib_handle, key, value)
#         
#     def set_double(self, key, value):
#         c_interface.grib_set_double(self.grib_handle, key, value)
#         
#     def set_string(self, key, value):
#         c_interface.grib_set_string(self.grib_handle, key, value)
