"""

A Pythonic interface to the ECMWF GRIB API.

See also:
https://software.ecmwf.int/wiki/display/GRIB/Releases

"""


__version__ = 0.1


def read(file):
    
    if isinstance(file, basestring):
        file = open(file, "rb")
        
#     while True:
#         so.
        
        
        
        
# new function in 1.10.0:
#    grib_is_defined




if __name__ == "__main__":

    from message import Message

    message = Message(from_samples="GRIB2")
    print message.edition
