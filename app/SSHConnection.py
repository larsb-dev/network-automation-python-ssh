from paramiko import SSHClient, AutoAddPolicy
from getpass import getpass
from time import sleep

class SSHConnection:
    def __init__(self):
        self.ssh_client = SSHClient()
        self.shell = None

    def accept_fingerprint(self):
        self.ssh_client.set_missing_host_key_policy(AutoAddPolicy())

    def invoke_shell(self):
        self.shell = self.ssh_client.invoke_shell()

    def connect(self, device):
        self.accept_fingerprint()
        self.ssh_client.connect(
            **device.__dict__,
            password=getpass('Enter password:'),
            look_for_keys=False,
            allow_agent=False
        )
        self.invoke_shell()

    def send(self, command):
        self.shell.send(command)
        sleep(1)

    def receive(self):
        return self.shell.recv(10_000).decode().strip()

    def disconnect(self):
        self.ssh_client.close()