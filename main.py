from configparser import ConfigParser
parser = ConfigParser()
parser.read('project.config')

print(parser.get('webdriver', 'driver_file_path'))