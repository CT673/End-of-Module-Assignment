# Server
import json
import os
import pickle
from pickle import dumps, loads, load, dump

import socket
from dict2xml import dict2xml
from cryptography.fernet import Fernet

#from encryption_helper import EncryptionHelper
#from configparser import NoSectionError, NoOptionError
import Config

# Deserialization
def des(deserialization):
    if Config.deserialization_option == "JSON":
        return json.loads(deserialization)
    elif Config.deserialization_option == "BINARY":
        return loads(deserialization)
    elif Config.deserialization_option == "XML":
        return dict2xml(deserialization, wrap="dictionary", indent="  ")
    else:
        print("format not recognised")

def ser(serialization):
    if Config.serialization_option == "JSON":
        return json.dumps(serialization)
    elif Config.serialization_option == "BINARY":
        return pickle.dumps(serialization)
    elif Config.serialization_option == "XML":
        return dict2xml(serialization, wrap="dictionary", indent="  ")
    else:
        print("format not recognised")

def decrypt():
    f = Fernet(Config.key)
    text = input("GrpC.txt").encode()
    encrypted = f.encrypt(text)
    decrypted = f.decrypt(encrypted)
def encrypt():
    f = Fernet(Config.key)
    text = input("GrpC.txt").encode()
    encrypted = f.encrypt(text)
    print("Encrypted dictionary")

payload = (Config.Countries)
payload_en = ser(Config.Countries)

Cont = payload
otp = input('Where do you want to print it (1 to console, 2 to a XML, 3 to a TXT encrypted, 4 to a TXT, 5 to a JSON)?: ')
if otp == '1':
    print(payload)
elif otp == '2':
    with open('GrpC.XML', mode='w') as Config.Countries:
        print(payload, file=Config.Countries)
elif otp == '3':
    with open('GrpC_encrypt.txt', mode='w') as Config.Countries:
        print(payload_en, file=Config.Countries)
elif otp == '4':
    with open('GrpC.txt', mode='w') as Config.Countries:
        print(payload, file=Config.Countries)
elif otp == '5':
    with open('GrpC.json', mode='w') as Config.Countries:
        print(payload, file=Config.Countries)
else:
    print('You write an invalid number, please try again')
