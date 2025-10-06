# 2024 Day 8 Code
from collections import defaultdict

class AntennaMap():
    BLANK = "."
    ANTINODE = "#"
    def __init__(self, map_blob):
        self.map = self.parse_map(map_blob)
        self.rows_range = range(len(self.map))
        self.cols_range = range(len(self.map[0]))
        self.antennas = self.find_antennas()
        self.antinodes = defaultdict(set)
        for antenna, locations in self.antennas.items():
            self.set_antinodes_part_1(antenna, locations)
        self.antinodes_part_2 = defaultdict(set)
        for antenna, locations in self.antennas.items():
            self.set_antinodes_part_2(antenna, locations)


    def part_1(self):
        compiled_antinodes = set()
        for antinodes in self.antinodes.values():
            for node in antinodes:
                compiled_antinodes.add(node)
        return len(compiled_antinodes)
    
    def part_2(self):
        compiled_antinodes = set()
        for antinodes in self.antinodes_part_2.values():
            for node in antinodes:
                compiled_antinodes.add(node)
        return len(compiled_antinodes)
        
    def parse_map(self, map_blob):
        rows = map_blob.split("\n")
        return [list(row) for row in rows]
    
    def find_antennas(self):
        antennas = defaultdict(list)
        for row in self.rows_range:
            for col in self.cols_range:
                value = self.map[row][col]
                if value != self.BLANK and value != self.ANTINODE:
                    antennas[value].append((row,col))
        return antennas

    def set_antinodes(self,value, antennas, mark = ANTINODE):
        self.set_antinodes_part_1(value, antennas, mark)

    def set_antinodes_part_1(self,value, antennas, mark = ANTINODE):
        for i in range(len(antennas) - 1):
            for j in range(i+1, len(antennas)):
                ant1 = antennas[i]
                ant2 = antennas[j]
                vector1 = (
                    ant1[0] - ant2[0],
                    ant1[1] - ant2[1]
                )
                vector2 = (
                    vector1[0] * -1,
                    vector1[1] * -1
                )
                self.add_antinode(value,  ant1[0] + vector1[0], ant1[1] + vector1[1])
                self.set(mark, ant1[0] + vector1[0], ant1[1] + vector1[1])

                self.add_antinode(value, ant2[0] + vector2[0], ant2[1] + vector2[1])
                self.set(mark, ant2[0] + vector2[0], ant2[1] + vector2[1])

    def set_antinodes_part_2(self,value, antennas, mark = ANTINODE):
        for i in range(len(antennas) - 1):
            for j in range(i+1, len(antennas)):
                ant1 = antennas[i]
                ant2 = antennas[j]
                vector1 = (
                    ant1[0] - ant2[0],
                    ant1[1] - ant2[1]
                )
                vector2 = (
                    vector1[0] * -1,
                    vector1[1] * -1
                )

                node_vector1 = (ant1[0] + vector1[0], ant1[1] + vector1[1])
                while self._accessible(*node_vector1):
                    self.antinodes_part_2[value].add(node_vector1)
                    node_vector1 = (node_vector1[0] + vector1[0], node_vector1[1] + vector1[1])


                node_vector2 = (ant2[0] + vector2[0], ant2[1] + vector2[1])
                while self._accessible(*node_vector2):
                    self.antinodes_part_2[value].add(node_vector2)
                    node_vector2 = (node_vector2[0] + vector2[0], node_vector2[1] + vector2[1])

    
    def add_antinode(self, antenna, row, col):
        if self._accessible(row, col):
            self.antinodes[antenna].add((row,col))

    def set(self, value, row, col):
        #print(f"set: {value=} {row=} {col=}")
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


    
    



