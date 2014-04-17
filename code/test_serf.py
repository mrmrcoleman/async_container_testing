#!/usr/bin/python
import unittest
from serf import serf

class test_serf(unittest.TestCase):
    
    serf_network = None
    
    def setUp(self):
        self.serf_network = serf();
        pass

    def testPIDNotEmptyString(self):
        not_expected = ""
        actual = self.serf_network.get_pid()
        self.assertNotEqual(not_expected, actual)

    def testStartAgent(self):
        expected = 0
        actual = self.serf_network.start_agent_thread()

if __name__ == '__main__':
    unittest.main()