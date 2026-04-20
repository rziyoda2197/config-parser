import configparser

class ConfigParser:
    def __init__(self, filename):
        self.config = configparser.ConfigParser()
        self.filename = filename

    def read_config(self):
        self.config.read(self.filename)

    def get_value(self, section, key):
        return self.config.get(section, key)

    def get_values(self, section):
        return dict(self.config.items(section))

    def add_section(self, section):
        self.config.add_section(section)

    def add_key(self, section, key, value):
        self.config.set(section, key, value)

    def save_config(self):
        with open(self.filename, 'w') as config_file:
            self.config.write(config_file)

# Misol fayl: config.ini
# [database]
# host = localhost
# port = 5432
# username = admin
# password = admin

# [server]
# host = 0.0.0.0
# port = 8080

config = ConfigParser('config.ini')
config.read_config()

print(config.get_value('database', 'host'))  # localhost
print(config.get_values('server'))  # {'host': '0.0.0.0', 'port': '8080'}
config.add_section('logging')
config.add_key('logging', 'level', 'INFO')
config.save_config()
