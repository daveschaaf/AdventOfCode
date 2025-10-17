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
        self.antinodes_part_2 = defaultdict(set)

    def part_1(self):
        self.antinodes = defaultdict(set)
        for antenna, locations in self.antennas.items():
            self.set_antinodes_part_1(antenna, locations)
        compiled_antinodes = set()
        for antinodes in self.antinodes.values():
            for node in antinodes:
                compiled_antinodes.add(node)
        return len(compiled_antinodes)
    
    def part_2(self):
        for antenna, locations in self.antennas.items():
            self.set_antinodes_part_2(antenna, locations)
        print("Part 2 antinodes set")
        compiled_antinodes = set()
        for antinodes in self.antinodes_part_2.values():
            for node in antinodes:
                compiled_antinodes.add(node)
        print("Returning Part 2")
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

    def set_antinodes_part_2(self,value, antennas):
        for ant in antennas:
            self.antinodes_part_2[value].add(ant)
        for i in range(len(antennas) - 1):
            for j in range(i+1, len(antennas)):
                ant1 = antennas[i]
                ant2 = antennas[j]
                vector1 = [ 
                    ant1[0] - ant2[0],
                    ant1[1] - ant2[1]
                ]
                # When on the same row or same col, mark all cells in that row/col

                if vector1[0] == 0:
                    vector1[1] = 1
                if vector1[1] == 0:
                    vector1[0] = 1

                vector2 = [
                    vector1[0] * -1,
                    vector1[1] * -1
                ]

                node_vector1 = self._calc_next_node(ant1, vector1)
                while self._accessible(*node_vector1):
                    self.antinodes_part_2[value].add(node_vector1)
                    node_vector1 = self._calc_next_node(node_vector1, vector1)
                
                node_vector2 = self._calc_next_node(ant2, vector2)
                while self._accessible(*node_vector2):
                    self.antinodes_part_2[value].add(node_vector2)
                    node_vector2 = self._calc_next_node(node_vector2, vector2)
        print(self)
    def _calc_next_node(self, node, vector):
        row = node[0] + vector[0]
        col = node[1] + vector[1]
        return (row, col)

    def add_antinode(self, antenna, row, col):
        if self._accessible(row, col):
            self.antinodes[antenna].add((row,col))

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

    def __str__(self):
        output_map = []
        map_copy = self.map.copy()
        for val_set in self.antinodes_part_2.values():
            for node in val_set:
                map_copy[node[0]][node[1]] = "%"
           
        for row in map_copy:
            map_string="".join(row.copy())
            output_map.append(map_string)
        print("\n")
        return "\n".join([str(r) for r in output_map])


    
    



