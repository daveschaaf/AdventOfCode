from code06 import *


def test_data_parsing():
    lab_map: LabMap = LabMap('06_data.dat')

    assert lab_map.map[0][0] == "."
    assert lab_map.map[0][4] == "#"
    assert len(lab_map.map) == 10
    assert lab_map.soldier == [6,4]
    assert lab_map.map[6][4] == lab_map.VISITED
    assert lab_map.soldier_direction == lab_map.SOLDIER_DIRECTION[lab_map.SOLDIER_UP]
    assert lab_map.move_soldier() == [5,4]
    assert lab_map.turn_soldier() == lab_map.SOLDIER_DIRECTION[lab_map.SOLDIER_RIGHT]
    assert lab_map.move_soldier() == [5,5]
    assert lab_map.turn_soldier() == lab_map.SOLDIER_DIRECTION[lab_map.SOLDIER_DOWN]
    assert lab_map.move_soldier() == [6,5]
    assert lab_map.turn_soldier() == lab_map.SOLDIER_DIRECTION[lab_map.SOLDIER_LEFT]
    assert lab_map.move_soldier() == [6,4]
    assert lab_map.turn_soldier() == lab_map.SOLDIER_DIRECTION[lab_map.SOLDIER_UP]
    assert lab_map.map[6][4] == lab_map.VISITED
    assert lab_map.map[5][4] == lab_map.VISITED
    assert lab_map.map[5][5] == lab_map.VISITED
    assert lab_map.map[6][5] == lab_map.VISITED
    assert lab_map.patrol() == 42

def test_part_1():
    lab_map: LabMap = LabMap('06_data.dat')
    assert lab_map.patrol() == 41


    full_map: LabMap = LabMap('06_data_full.dat')
    assert full_map.patrol() == 4752

