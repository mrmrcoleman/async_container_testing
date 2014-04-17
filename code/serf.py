#!/usr/bin/python
import subprocess
import threading

def start_agent():
    cmd_string = 'serf agent'
    cmd_args = cmd_string.split()
    proc = subprocess.Popen(cmd_args, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    proc.wait()
    if proc.returncode != 0:
        raise Exception('Error code was %d' % (proc.returncode))

class serf:

    def __init__(self, name=""):
        self.name = name

    def get_pid(self):
        return 1
        
    # def start_agent(self):
        # cmd_string = 'serf agent'
        # cmd_args = cmd_string.split()
        # proc = subprocess.Popen(cmd_args, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
        # proc.wait()
        # if proc.returncode != 0:
            # raise Exception('Error code was %d' % (proc.returncode))

    def start_agent_thread(self):
        t = threading.Thread(target=start_agent)
        t.daemon = True
        t.start()