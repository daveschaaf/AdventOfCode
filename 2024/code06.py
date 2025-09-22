from copy import deepcopy
from typing import Optional
from collections import defaultdict

class LabMap():
    SOLDIER_UP = "^"
    SOLDIER_LEFT = "<"
    SOLDIER_RIGHT = ">"
    SOLDIER_DOWN = "v"
    SOLDIER_DIRECTION = {
        SOLDIER_UP: (-1,0),
        SOLDIER_RIGHT: (0,1),
        SOLDIER_DOWN: (1,0),
        SOLDIER_LEFT: (0,-1)
    }
    SOLDIERS = (SOLDIER_DOWN, SOLDIER_LEFT, SOLDIER_RIGHT, SOLDIER_UP)

    TURN_RIGHT = [[ 0, 1],[-1, 0]]

    VISITED = "X"
    WALL = "#"

    def __init__(self, file_name: Optional[str] = None, obstruction: Optional[tuple[int, int]] = None, 
                 map: Optional[list[list[int]]] = None):
        if map:
            self.map = map
        elif file_name:
            self.map = self.parse_map(file_name)
        if obstruction:
            self.map[obstruction[0]][obstruction[1]] = self.WALL
        self.soldier: tuple[int, int] = self.find_soldier()
        self.soldier_direction = self.SOLDIER_DIRECTION[self.map[self.soldier[0]][self.soldier[1]]]
        self.detect_turn()
        self.mark_visited()


    def patrol(self):
        steps = set()
        step = tuple()
        while step not in steps:
            steps.add(step)
            step = self.soldier + self.move_soldier()
            if -1 in step:
                return sum([1 for row in self.map for col in row if col == self.VISITED])
        return -1

    def path(self):
        row: int = len(self.map)
        col: int = len(self.map[0])
        path = []
        for i in range(row):
            for j in range(col):
                if self.map[i][j] == self.VISITED:
                    path.append((i,j))
        return path

    def detect_turn(self):
        row: int = self.soldier[0] + self.soldier_direction[0]
        col: int = self.soldier[1] + self.soldier_direction[1]
        if (row < 0 or row > len(self.map) - 1) or (col < 0 or col > len(self.map[0]) - 1):
            return -1
        else:
            if self.map[row][col] == self.WALL:
                self.turn_soldier(self.TURN_RIGHT)
                try:
                    self.detect_turn()
                except RecursionError:
                    print(self)
                    print(self.soldier)

    def move_soldier(self) -> tuple[int, int]:
        row: int = self.soldier[0] + self.soldier_direction[0]
        col: int = self.soldier[1] + self.soldier_direction[1]
        if (row < 0 or row > len(self.map) - 1) or (col < 0 or col > len(self.map[0]) - 1):
            return (-1, -1)
        self.soldier = (row, col)
        self.mark_visited()
        self.detect_turn()
        return self.soldier

    def turn_soldier(self, turn) -> tuple[int, int]:
        soldier = self.soldier_direction
        direction = (turn[0][0]*soldier[0] + turn[0][1]*soldier[1],
                    turn[1][0]*soldier[0] + turn[1][1]*soldier[1])
        self.soldier_direction = direction
        return direction
    
    def mark_visited(self) -> None:
        self.map[self.soldier[0]][self.soldier[1]] = self.VISITED

    def find_soldier(self) -> tuple[int, int]:
        row: int = len(self.map)
        col: int = len(self.map[0])
        for i in range(row):
            for j in range(col):
                if self.map[i][j] in self.SOLDIERS:
                    return (i,j)
        return (-1, -1)

    def parse_map(self, file_name: str) -> list[list[str]]:
        map: list[list[str]] = []
        with open(file_name, 'r') as file:
            for line in file:
                line = str(line).replace("\n","")
                map.append(list(line))
        return map

    def __str__(self) -> str:
        display = deepcopy(self.map)
        marker = [k for k, v in self.SOLDIER_DIRECTION.items() if v == self.soldier_direction][0]
        display[self.soldier[0]][self.soldier[1]] = marker

        for line in display:
            line.append("\n")
        return "\n"+"".join(["".join(line) for line in display])
