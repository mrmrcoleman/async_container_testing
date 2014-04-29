#!/usr/bin/python
# Test this with `echo "fuck fuck fuck" | ./event_handler.py`
import datetime
import os
import sys

logging_dir = "/tmp/logging"
testing_log = logging_dir + "/test.txt"

if __name__ == '__main__':
    if not os.path.exists(logging_dir):
        os.mkdir(logging_dir)
        
    payload = sys.stdin.read()
    timestamp = str(datetime.datetime.utcnow())
    
    if not os.path.exists(testing_log):
        with open(testing_log, "w+") as testlog:
            testlog.write(timestamp + " PAYLOAD: " + payload)
    else:
        with open(testing_log, "a") as testlog:
            testlog.write(timestamp + " PAYLOAD: " + payload)