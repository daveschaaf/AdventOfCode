from code06 import *


def test_data_parsing():
    lab_map: LabMap = LabMap('06_data.dat')

    assert lab_map.map[0][0] == "."
    assert lab_map.map[0][4] == "#"
    assert len(lab_map.map) == 10
    assert lab_map.soldier == (6,4)
    assert lab_map.map[6][4] == lab_map.VISITED
    assert lab_map.soldier_direction == lab_map.SOLDIER_DIRECTION[lab_map.SOLDIER_UP]
    assert lab_map.move_soldier() == (5,4)
    assert lab_map.turn_soldier(lab_map.TURN_RIGHT) == lab_map.SOLDIER_DIRECTION[lab_map.SOLDIER_RIGHT]
    assert lab_map.move_soldier() == (5,5)
    assert lab_map.turn_soldier(lab_map.TURN_RIGHT) == lab_map.SOLDIER_DIRECTION[lab_map.SOLDIER_DOWN]
    assert lab_map.move_soldier() == (6,5)
    assert lab_map.turn_soldier(lab_map.TURN_RIGHT) == lab_map.SOLDIER_DIRECTION[lab_map.SOLDIER_LEFT]
    assert lab_map.move_soldier() == (6,4)
    assert lab_map.turn_soldier(lab_map.TURN_RIGHT) == lab_map.SOLDIER_DIRECTION[lab_map.SOLDIER_UP]
    assert lab_map.map[6][4] == lab_map.VISITED
    assert lab_map.map[5][4] == lab_map.VISITED
    assert lab_map.map[5][5] == lab_map.VISITED
    assert lab_map.map[6][5] == lab_map.VISITED

def test_sample():
    lab_map: LabMap = LabMap('06_data.dat')
    assert lab_map.soldier == (6,4)
    starting_position = lab_map.soldier
    assert lab_map.patrol() == 41
    assert len(lab_map.path()) == 41
   
    loops = 0
    for position in lab_map.path():
        if position == tuple(starting_position):
            continue
        blocked_map = LabMap(file_name = '06_data.dat', obstruction = position)
        result = blocked_map.patrol()
        if result == -1:
            loops += 1
    assert loops == 6

def test_full():

    full_map: LabMap = LabMap('06_data_full.dat')
    starting_position = full_map.soldier
    assert full_map.patrol() == 4752
    assert len(full_map.path()) == 4752
    
    loops = 0
    for position in full_map.path():
        if position == tuple(starting_position):
            continue
        blocked_map = LabMap(file_name = '06_data_full.dat', obstruction = position)
        result = blocked_map.patrol()
        if result == -1:
            loops += 1
            print(f"Found loop #{loops}")
    assert loops == 1
    # 1800 too high
    # 1704 incorrect
