import paramiko
import os
import sys
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

server1=Server('srdl','ser21','192.168.107.66')
local='/home/srdl/serverPanel/c2.py'
remote='/home/srdl/c1.py'
server1.download(remote,local)

