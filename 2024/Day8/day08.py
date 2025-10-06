# 2024 Day 8 Code


class AntennaMap():

    ANTINODE = "%"
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

    def set_antinodes(self, antennas, mark = ANTINODE):
        for i in range(len(antennas) - 1):
            for j in range(i+1, len(antennas)):
                ant1 = antennas[i]
                ant2 = antennas[j]
                print(f"{ant1=}, {ant2=}")
                vector1 = (
                    ant1[0] - ant2[0],
                    ant1[1] - ant2[1]
                )
                vector2 = (
                    vector1[0] * -1,
                    vector1[1] * -1
                )
                self.set(mark, ant1[0] + vector1[0], ant1[1] + vector1[1])
                self.set(mark, ant2[0] + vector2[0], ant2[1] + vector2[1])

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


    
    



