#!/usr/bin/python
import subprocess
import threading
import Queue

class serf:

    serf_thread = None
    serf_stdout = None
    serf_proc = None

    def __init__(self, name=""):
        self.name = name
        self.serf_stdout = Queue.Queue()

    def get_pid(self):
        if self.serf_proc == None:
            raise Exception("Serf network not running!")
        else:
            return self.serf_proc.pid
        
    def start_agent(self):
        cmd_string = 'serf agent'
        cmd_args = cmd_string.split()
        global self.serf_proc
        self.serf_proc = subprocess.Popen(cmd_args, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
        for line in iter(self.serf_proc.stdout.readline,''):
            self.serf_stdout.put(line)
        if serf_proc.returncode != 0:
            raise Exception('Error code was %d' % (proc.returncode))
            
    def kill_agent_thread(self):
        self.serf_thread.stop()

    def start_agent_thread(self):
        self.serf_thread = threading.Thread(target=self.start_agent)
        self.serf_thread.daemon = True
        self.serf_thread.start()

    def get_std_out(self):
        if self.serf_thread == None:
            return ""
        else:
            return self.serf_stdout.get()

    def __del__(self):
        if self.serf_proc != None:
            self.serf_proc.kill()
        