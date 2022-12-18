import json
import os
import pickle
import dict2xml as dict2xml
import Config
import socket
from dict2xml import dict2xml
from cryptography.fernet import Fernet
COUNTRIES = Config.countries

s = socket.socket()
client = socket.socket()
client.connect((Config.server_address, Config.port_number))
print("Welcome to the dictionary:")

for key, value in COUNTRIES.items():
    print(key, value)

    
# Serialization/ pickle file
def serialise_dictionary(self, serialization):
    if Config.serialization_option == "JSON":
        with open('dico.json', 'w') as f:
            json.dump(self.dictionary, f)
            print('Dictionary serialised. Filename: JSON')
    elif Config.serialization_option == "BINARY":
        with open('dico.bin', 'wb') as f:
            pickle.dump(self.dictionary, f)
            print('Dictionary serialised. Filename: Binary')
    elif format == "XML":
        xml_content = dict2xml(self.dictionary, wrap="dictionary", indent="  ")
        with open('dico.xml', 'w') as f:
            f.write(xml_content)
            f.close()
            print('Dictionary serialised as XML. Filename: xml')
            #we do not need to write to files, we can return either JSON, pickle or XML
            
# Edit dictionary
class old_dictionary(COUNTRIES):
    def __init__(self):
        self = COUNTRIES()

    def add(self, key, value):
        self[key] = value


edits = old_dictionary()
edits.key = input("")
edits.values = input("")
edits.add(edits.key, edits.value)

print(edits)
