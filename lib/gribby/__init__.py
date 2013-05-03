"""

A Pythonic interface to the ECMWF GRIB API.

See also:
https://software.ecmwf.int/wiki/display/GRIB/Releases

"""

import ctypes


__version__ = 0.1


so = ctypes.CDLL("/data/local/itbb/grib/grib_api-1.10.0/lib/libgrib_api.so")

print so

print so.grib_samples_new_from_file("GRIB2")

def read(file):
    
    if isinstance(file, basestring):
        file = open(file, "rb")
        
#     while True:
#         so.
        
        
        
        
# new function in 1.10.0: grib_is_defined