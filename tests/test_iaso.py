import iaso
import pytest
import os
import yaml


def test_no_file():
    with pytest.raises(FileNotFoundError):
        iaso.read_iaso_file()


@pytest.fixture
def create_file():
    filename = '.iaso.yml'
    with open(filename, 'w+') as file:
        file.write("this is a file")
    yield
    try:
        os.remove(filename)
    except OSError:
        pass


def test_file(create_file):
    yaml = iaso.read_iaso_file()
    print(yaml)
    assert yaml == "this is a file"


@pytest.fixture
def create_invalid_yaml_file():
    filename = '.iaso.yml'
    with open(filename, 'w+') as file:
        file.write("unbalanced brackets: ][")
    yield
    try:
        os.remove(filename)
    except OSError:
        pass


def test_invalid_yaml(create_invalid_yaml_file):
    with pytest.raises(yaml.YAMLError):
        iaso.read_iaso_file()
