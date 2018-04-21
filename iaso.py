import os
import sys
import yaml

def read_structure_file():
    dir = os.getcwd()
    with open(dir + '/.iaso.yml') as file:
        read_data = file.read()
    return read_data

def read_yaml(yaml):
    pass

