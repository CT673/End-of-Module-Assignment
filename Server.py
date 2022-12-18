# Server
import os
import socket

import Config

s = socket.socket()
print('Socket created')
s.bind((Config.server_address, Config.port_number))
s.listen(3)  # take it out or put it into the config file (config.timeout(3))
print('Waiting for connections')

# Deserialization
def des(deserialization):
    if Config.deserialization_option == "JSON":
        return json.loads(deserialization)

    elif Config.deserialization_option == "BINARY":
        return pickle.loads(deserialization)

    elif Config.deserialization_option == "XML":
        return dict2xml(deserialization, wrap="dictionary", indent="  ")

    else:
        print("format not recognised")


payload = des(COUNTRIES)
s.recv(payload)
while True:
       c, addr = s.accept()
    name = c.recv(1024).decode()  # put the number into the config file # print("connected with ", addr, name)
    if Config.opt == 1:
        print(name)
    else:
        sys.exit()
        
    c.send(bytes('Welcome to the dictionary', 'utf-8'))  # messages into the config file
    c.close()

    
