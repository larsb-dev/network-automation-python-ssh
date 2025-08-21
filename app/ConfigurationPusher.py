class ConfigurationPusher:
    def push(self, config, ssh_connection):
        with open(config, 'r') as file:
            for line in file:
                command = line.strip()
                if command:
                    ssh_connection.send(command + '\n')