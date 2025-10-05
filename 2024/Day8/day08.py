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

    
    



