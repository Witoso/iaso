import os

def test_readme():
    basepath = os.path.dirname(__file__)
    assert os.path.isfile(os.path.join(basepath, '..', 'README.md'))
