
import unittest

from message import GribMessage


class TestSimple(unittest.TestCase):
    # Test simple operations on a sample message.

#     def setUp(self):
#         self.sample

    def test_get(self):
        message = GribMessage("GRIB2")
        
        print message.localTablesVersion
        print message.latitudeOfFirstGridPointInDegrees
        print message.centre
    
    def test_set(self):
        message = GribMessage("GRIB2")
        
        message.localTablesVersion = 123
        message.latitudeOfFirstGridPointInDegrees = 123.456
        message.centre = "egrr"
        
        print message.localTablesVersion
        print message.latitudeOfFirstGridPointInDegrees
        print message.centre


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


class TestRead(unittest.TestCase):
    
    filename = "test.grib2"
    
    def test_filename(self):
        for message in read_messages(self.filename):
            print message

    def test_file_handle(self):
        with open(filename, "rb") as infile:
            for message in read_messages(infile):
                print message




if __name__ == '__main__':
    unittest.main()