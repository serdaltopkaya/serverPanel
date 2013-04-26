#!/usr/bin/env python

import os
import paramiko

class sshClass(object):

    def __init__(self,server1, username1, pasword1):   
        self.server=server1
        self.username=username1
        self.password=pasword1
        self.userClient=paramiko.SSHClient()
	self.stdin=''
	self.stdout=''
	self.stderr=''
	self.path=''

    def connection_builder(self):
        self.userClient.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
	

    def test(self):
	self.connection_builder()
        try:
            self.userClient.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
            self.userClient.connect(self.server, username=self.username, password=self.password)
            self.stdin,self.path,self.stderr = self.userClient.exec_command('pwd')
            self.path=self.path.read()
            while True:
                cmd = raw_input("Command to run: ")
                if cmd == "":
                    print "its complated";
	            print "current directory: ",self.path
		    self.userClient.close()
	            break

                print "running '%s'" % cmd
                self.stdin,self.stdout,self.stderr = self.userClient.exec_command(cmd)
                print self.stdout.read().strip()
                print "current directory: ",self.path

	finally:
	    self.userClient.close()        

    
myclass=sshClass('192.168.1.34','srdl','ser21')
myclass.test()
