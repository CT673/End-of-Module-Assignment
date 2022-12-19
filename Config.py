# Creating a dictionary of 20 countries
from cryptography.fernet import Fernet
Countries = dict({'1': 'Argentina',
                  '2': 'Australia',
                  '3': 'Brazil',
                  '4': 'Colombia',
                  '5': 'Egypt',
                  '6': 'France',
                  '7': 'Germany',
                  '8': 'Greece',
                  '9': 'Hong Kong',
                  '10': 'Kiribati',
                  '11': 'Lesotho',
                  '12': 'Madagascar',
                  '13': 'Mexico',
                  '14': 'Nepal',
                  '15': 'New Zealand',
                  '16': 'Nigeria',
                  '17': 'Philippines',
                  '18': 'Portugal',
                  '19': 'United Arab Emirates',
                  '20': 'United Kingdom'})

serialization_option = "XML"
serialization_option = "JSON"
serialization_option = "BINARY"

deserialization_option = "XML"
deserialization_option = "JSON"
deserialization_option = "BINARY"

server_address = 'localhost'
port_number = 9999

opt = 1
file_name = "GrpC.txt"
key = Fernet.generate_key()
