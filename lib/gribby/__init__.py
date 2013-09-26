"""

A Pythonic interface to the ECMWF GRIB API.

See also:
https://software.ecmwf.int/wiki/display/GRIB/Releases

"""

import c_interface


__version__ = 0.1


def read_messages(infile):
# keep

    # if it's a filename, open it
    close_on_exit = False
    if isinstance(infile, basestring):
        infile = open(infile, "rb")
        close_on_exit = True

    #  yield each grib message
    while not infile.eof():
        grib_message = c_interface.so.grib_new_from_file(infile)
        yield grib_message
        
    if close_on_exit:
        infile.close()


        
        
        
        
# new function in 1.10.0:
#    grib_is_defined




if __name__ == "__main__":

    # MOVE THIS INTO THE TESTS, WHEN THEY CAN BE MADE TO RUN

    from message import GribMessage
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

#     print "test get non-native type"
#     print message.get_double("localTablesVersion")
#     print message.get_long("latitudeOfFirstGridPointInDegrees")
#     print message.get_long("centre")
#     print ""
# 
#     print "test set non-native type"
#     message.set_double("localTablesVersion", 234.0)
#     message.set_long("latitudeOfFirstGridPointInDegrees", 4)
#     message.set_long("centre", 7)
#     print message.localTablesVersion
#     print message.latitudeOfFirstGridPointInDegrees
#     print message.centre
#     print ""


    # Test file handle
    filename = "test.grib2"
    with open(filename, "rb") as infile:
        for message in read_messages(infile):
            print message

    # Test filename
    for message in read_messages(filename):
        print message

