#!/usr/bin/env python
import pexpect
import pxssh

class SSHConnection(object):
     def __init__(self):
          self.user="srdl"
          self.host="192.168.1.9"
          self.userpass="ser21"
          self.rootpass="ser21"
          self.userClient=pxssh.pxssh()

     def connection_builder(self):
          if not self.userClient.login(self.host, self.user,self.userpass):
               print("connection filed")
               print(s)
          else:
               print ("ssh session login  successfuly")
               while True:

                    cmd=raw_input("enter a command to run:   ")
                    if cmd =="" :
                         self.userClient.logout()
                         break
                    self.userClient.sendline(cmd)
                    self.userClient.prompt()
                    print self.userClient.before
                    #self.userClient.sendline("pwd")
                    #self.userClient.prompt()
                    #print "  after:   ",  self.userClient.after

myclass=SSHConnection()
myclass.connection_builder()
