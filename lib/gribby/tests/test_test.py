
import unittest

import gribby
import gribby.tests

from gribby.message import Message


class TestMessage(unittest.TestCase):
    
    def test_from_sample(self):
        mesage = Message(from_samples="GRIB2")
        print message.message_id

        
if __name__ == "__main__":
    unittest.main()
