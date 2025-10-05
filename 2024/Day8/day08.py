# 2024 Day 8 Code

sample_1 = """..........
...#......
..........
....a.....
..........
.....a....
..........
......#...
..........
.........."""



class AntennaMap():
    def __init__(self, map_blob):
        self.map = self.parse_map(map_blob)
        self.rows_range = range(len(self.map))
        self.cols_range = range(len(self.map[0]))
        self.antennas = self.find_antennas()
        
    def parse_map(self, map_blob):
        rows = map_blob.split("\n")
        return [list(row) for row in rows]
    
    def find_antennas(self):
        antennas = []
        for row in range(len(self.map)):
            for col in range(len(self.map[0])):
                if self.map[row][col] != '.':
                    antennas.append((row,col))
        return antennas

    def set_antinodes(self, antenna_1, antenna_2):
        pass

    def set(self, value, row, col):
        if self._accessible(row, col):
            self.map[row][col] = value
            return value
        return False

    def get(self, row, col):
        if self._accessible(row, col):
            return self.map[row][col]
        return False

    def _accessible(self, row, col):
        return row in self.rows_range and col in self.cols_range


    
    



