from code06 import *

map: list[list[str]] = LabMap('06_data.dat')

def test_data_parsing():
    print(map)
    assert map[0][0] == "."
    assert map[0][4] == "#"
    assert len(map) == 10

