#!/usr/bin/env python

import pexpect
import pxssh

class SSHConnection(object):

     def __init__(self,hostIP, hostUser, hostPass):

          self.user=hostUser
          self.host=hostIP
          self.userpass=hostPass
          #self.rootpass=password
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
                    a=self.userClient.before
                    print self.userClient.before
                    self.serverFiles=a.split()
                    #self.userClient.prompt()
                    for i in range(len(self.serverFiles)):
                         print self.serverFiles[i]

if __name__ == "__main__":

     myclass=SSHConnection()
     myclass.connection_builder()
