from copy import deepcopy

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

    def __init__(self, file_name: str):
        self.map = self.parse_map(file_name)
        self.soldier: list[int] = self.find_soldier()
        self.soldier_direction = self.SOLDIER_DIRECTION[self.map[self.soldier[0]][self.soldier[1]]]
        self.mark_visited()

    def patrol(self):
        steps = 0
        for _ in range(len(self.map[0])*(len(self.map))):
            try:
                self.move_soldier()
                steps += 1
            except IndexError:
                print(self)
                return sum([1 for row in self.map for col in row if col == self.VISITED])

    def move_soldier(self) -> list[int]:
        row: int = self.soldier[0] + self.soldier_direction[0]
        col: int = self.soldier[1] + self.soldier_direction[1]
        if self.map[row][col] == self.WALL:
            self.turn_soldier(self.TURN_RIGHT)
            row: int = self.soldier[0] + self.soldier_direction[0]
            col: int = self.soldier[1] + self.soldier_direction[1]
        self.soldier = [row, col]
        self.mark_visited()
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
