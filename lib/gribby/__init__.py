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

    # MOVE THIS INTO THE TESTS, WHEN THEY CAN BE MADE TO RUN

    from message import Message
    message = Message(from_samples="GRIB2")

    print "test get"
    print message.localTablesVersion
    print message.latitudeOfFirstGridPointInDegrees
    print message.centre
    print ""
    
    print "test set"
    message.localTablesVersion = 123
    message.latitudeOfFirstGridPointInDegrees = 123.456
    message.centre = "egrr"
    print message.localTablesVersion
    print message.latitudeOfFirstGridPointInDegrees
    print message.centre
    print ""

    print "test get non-native type"
    print message.get_double("localTablesVersion")
    print message.get_long("latitudeOfFirstGridPointInDegrees")
    print message.get_long("centre")
    print ""

    print "test set non-native type"
    message.set_double("localTablesVersion", 234.0)
    message.set_long("latitudeOfFirstGridPointInDegrees", 4)
    message.set_long("centre", 7)
    print message.localTablesVersion
    print message.latitudeOfFirstGridPointInDegrees
    print message.centre
    print ""
