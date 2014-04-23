#!/usr/bin/python
import unittest
from serf import serf
import time

class test_serf(unittest.TestCase):
    
    serf_network = None
    
    def setUp(self):
        self.serf_network = serf();
        pass

    def testPIDNotEmptyString(self):
        not_expected = ""
        actual = self.serf_network.get_pid()
        self.assertNotEqual(not_expected, actual)

    def test_get_message_from_stdout_when_serf_is_not_running(self):
        expected = ""
        actual = self.serf_network.get_std_out()
        self.assertEqual(expected, actual)
        
    def test_get_message_from_stdout_when_serf_is_running(self):
        self.serf_network.start_agent_thread()
        expected = "==> Starting Serf agent...\n"
        actual_1 = self.serf_network.get_std_out()
        self.assertEqual(expected, actual_1)
        
        for x in range(0, 10):
          print self.serf_network.get_std_out()
          time.sleep(1)
        
        self.serf_network.leave_agent()
        
        for x in range(0, 20):
          print self.serf_network.get_std_out()
          time.sleep(2) 

if __name__ == '__main__':
    unittest.main()