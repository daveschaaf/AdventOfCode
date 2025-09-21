from copy import deepcopy
from typing import Optional

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

    def __init__(self, file_name: str, obstruction: Optional[tuple] = None):
        self.map = self.parse_map(file_name)
        if obstruction:
            self.map[obstruction[0]][obstruction[1]] = self.WALL
        self.soldier: list[int] = self.find_soldier()
        self.starting_position = self.soldier.copy()
        self.soldier_direction = self.SOLDIER_DIRECTION[self.map[self.soldier[0]][self.soldier[1]]]
        self.detect_turn()
        self.starting_direction = self.soldier_direction
        self.mark_visited()

    def patrol(self):
        looped = False
        moves = 0
        size = len(self.map)*len(self.map[0])
        while not looped:
            try:
                self.move_soldier()
                moves += 1
                print(self)
                looped = (self.soldier == self.starting_position and self.soldier_direction == self.starting_direction)
                looped = looped or moves > size
            except IndexError:
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
        if self.map[row][col] == self.WALL:
            self.turn_soldier(self.TURN_RIGHT)

    def move_soldier(self) -> list[int]:
        row: int = self.soldier[0] + self.soldier_direction[0]
        col: int = self.soldier[1] + self.soldier_direction[1]
        self.soldier = [row, col]
        self.mark_visited()
        self.detect_turn()
        return self.soldier

    def turn_soldier(self, turn = TURN_RIGHT) -> tuple[int, int]:
        soldier = self.soldier_direction
        direction = (turn[0][0]*soldier[0] + turn[0][1]*soldier[1],
                    turn[1][0]*soldier[0] + turn[1][1]*soldier[1])
        self.soldier_direction = direction
        return direction
    
    def mark_visited(self) -> None:
        self.map[self.soldier[0]][self.soldier[1]] = self.VISITED

    def find_soldier(self) -> list[int]:
        row: int = len(self.map)
        col: int = len(self.map[0])
        for i in range(row):
            for j in range(col):
                if self.map[i][j] in self.SOLDIERS:
                    return [i,j]
        return [-1]

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
