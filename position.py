import unittest

from movement import Spacecraft


class ValueTestCase(unittest.TestCase):

    def valid_position(self):

        ct=Spacecraft([0,0,0],'N')
        result= Spacecraft.execute_commands(ct,['f', 'r', 'u', 'b', 'l'])
        self.assertEqual(result.position,[0,-1,1])
        self.assertEqual(result.direction, 'N')