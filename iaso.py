import os
import sys
import yaml

def read_iaso_file():
    dir = os.getcwd()
    with open(dir + '/.iaso.yml') as file:
        read_data = file.read()
    return read_data


