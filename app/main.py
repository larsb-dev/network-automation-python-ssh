from dotenv import load_dotenv
from ConfigurationPusher import ConfigurationPusher
from SSHConnection import SSHConnection
from Switch import Switch
import os

def main():
    load_dotenv()
    ip_address = os.getenv("IP_ADDRESS")
    port = os.getenv("PORT")
    ssh_user = os.getenv("SSH_USER")

    switch = Switch(ip_address, port, ssh_user)
    ssh_connection = SSHConnection()
    config_pusher = ConfigurationPusher()

    ssh_connection.connect(switch)
    config_pusher.push('../device_configs/asw01.txt', ssh_connection)
    output = ssh_connection.receive()
    print(output)
    ssh_connection.disconnect()

if __name__ == "__main__":
    main()