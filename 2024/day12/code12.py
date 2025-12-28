
def parse_map(raw_map):
    rows = raw_map.split('\n')
    return [list(row) for row in rows]

class Region():
    def __init__(self, parsed_map, starting_cell):
        self.area = 1
        self.perimeter = 4
        self.garden = parsed_map
        self.nrow = len(parsed_map)
        self.ncol = len(parsed_map[0])
        self.visited = set()
        self.plot_garden(starting_cell)
        
    def price(self):
        return self.area * self.perimeter

    def plot_garden(self, cell):
        value = self.get_value(*cell)
        self.perimeter = self.dfs_perimeter(cell, value)

    def dfs_perimeter(self, cell, value):
        if self.get_value(*cell) != value:
            return 1
        if cell in self.visited:
            return 0
        self.visited.add(cell)
        
        up = (cell[0]-1, cell[1])
        down = (cell[0]+1, cell[1])
        left = (cell[0], cell[1]-1)
        right = (cell[0], cell[1]+1)
        directions = [up, down, left, right]
        return sum(map(lambda d: self.dfs_perimeter(d, value), directions))

        
    def get_value(self, row, col):
        if row < 0 or col < 0 or row > self.nrow-1 or col > self.ncol-1:
            return None
        return self.garden[row][col]

