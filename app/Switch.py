from app.Device import Device

class Switch(Device):
    def __init__(self, hostname, port, username):
        super().__init__(hostname, port, username)