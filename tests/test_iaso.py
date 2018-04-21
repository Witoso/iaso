import iaso
import pytest
import os

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
    assert iaso.read_iaso_file() == "this is a file"


