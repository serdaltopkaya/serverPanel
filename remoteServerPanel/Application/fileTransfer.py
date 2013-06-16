import paramiko
import os
import sys
import edit1
class Server(object):

    def __init__(self, username, password, host, port=22):

        self.transport = paramiko.Transport((host, port))
        self.transport.connect(username=username, password=password)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)

    def upload(self, local, remote):
        if os.path.isfile(local):
            self.sftp.put(local, remote)
        else:
            raise IOError('Could not find localFile %s !!' % local)
            #self.sftp.put(local, remote)

    def download(self, remote, local):
    	  	
        self.sftp.get(remote, local)


    
    def openFile(self, remote):
    	notepad = edit1.Notepad(self.sftp.open(remote))
    

    def close(self):
        """
        Close the connection if it's active
        """

        if self.transport.is_active():
            self.sftp.close()
            self.transport.close()

    # with-statement support
    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.close()
if __name__=='__main__':

  server1=Server('srdl','ser21','192.168.1.45') 
  local='/home/srdl/transfer.py'
  remote='/home/srdl/transfer.py'
  server1.openFile(remote)

