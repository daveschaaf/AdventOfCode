
def parse_map(raw_map):
    rows = raw_map.split('\n')
    return [list(row) for row in rows]

class Region():
    def __init__(self, parsed_map, starting_cell):
        self.area = 0
        self.perimeter = 0
        self.garden = parsed_map
        self.nrow = len(parsed_map)
        self.ncol = len(parsed_map[0])
        self.plots = set()
        self.sides = 0
        self.value = self.get_value(*starting_cell)
        self.plot_garden(starting_cell)
        
    def price(self):
        return self.area * self.perimeter
    def discounted_price(self):
        return self.area * self.sides

    def plot_garden(self, cell):
        # self.perimeter, _ = self.dfs_perimeter(cell, value)
        self.find_garden_cells(cell)

    def find_garden_cells(self, starting_cell):
        """
        Replaces dfs_perimeter
        Populates self.plots with all the connected cells of the same value
        Perimeter count should be handled separately
        """
        stack = [starting_cell]

        while stack:
            print(stack)
            r, c = stack.pop()
            if (r, c) in self.plots or self.get_value(r, c) != self.value:
                continue
            
            self.plots.add((r, c))
            for ortho_r, ortho_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                stack.append((ortho_r, ortho_c))



    # def dfs_perimeter(self, cell, value):
    #     if self.get_value(*cell) != value:
    #         return 1, True
    #     if cell in self.plots:
    #         return 0, False
    #     self.plots.add(cell)
    #     self.area += 1
    #
    #     local_boundaries = {}
    #     total_edges = 0
    #     for direction, neighbor_coords in self.ortho_neighbors(cell).items():
    #         edge_count, is_boundary = self.dfs_perimeter(neighbor_coords, value)
    #         total_edges += edge_count
    #         local_boundaries[direction] = [neighbor_coords, is_boundary]
    #     self.sides += self.plot_corners(local_boundaries, cell, value) 
    #     return total_edges, False 
    
    def plot_corners(self, local_boundaries, cell):
        def outside_region(neighbor):
            return self.get_value(*neighbor) != self.value
        corners = 0

        up = local_boundaries['up'][1]
        down = local_boundaries['down'][1]
        left = local_boundaries['left'][1]
        right = local_boundaries['right'][1]
        corners += sum([up and right, up and left, down and right, down and left])
        
        local_diagonals = self.diag_neighbors(cell)
        ul = not up and not left and outside_region(local_diagonals['ul'])
        ur = not up and not right and outside_region(local_diagonals['ur'])
        dl = not down and not left and outside_region(local_diagonals['dl'])
        dr = not down and not right and outside_region(local_diagonals['dr'])
        corners += sum([ul, ur, dl, dr])
        return corners

    def get_value(self, row, col):
        if row < 0 or col < 0 or row > self.nrow-1 or col > self.ncol-1:
            return None
        return self.garden[row][col]
    
    def diag_neighbors(self, cell):
        diag_keys = ['ul', 'ur', 'dr', 'dl']
        all_directions = self.neighbors(cell)
        return {key: all_directions[key] for key in diag_keys}

    def ortho_neighbors(self, cell):
        ortho_keys = ['up', 'down', 'left', 'right']
        all_directions = self.neighbors(cell)
        return {key: all_directions[key] for key in ortho_keys}
    
    def neighbors(self, cell):
        up = (cell[0]-1, cell[1])
        down = (cell[0]+1, cell[1])
        left = (cell[0], cell[1]-1)
        right = (cell[0], cell[1]+1)
        ul = (cell[0]-1, cell[1]-1)
        ur = (cell[0]-1, cell[1]+1)
        dl = (cell[0]+1, cell[1]-1)
        dr = (cell[0]+1, cell[1]+1)
        udlr = {"up": up, "down": down, "left": left,"right": right,
                'ul': ul, 'ur': ur, 'dl': dl, 'dr': dr}
        return udlr 

def calc_total_price(raw_map, pricing):
    parsed_map = parse_map(raw_map)
    total_price = 0
    plotted = set()
    for row in range(len(parsed_map)):
        for col in range(len(parsed_map[0])):
            plot = (row, col)
            if plot not in plotted:
                region = Region(parsed_map, plot)
                if pricing == "standard":
                    total_price += region.price()
                else:
                    total_price += region.discounted_price()
                plotted = plotted.union(region.plots)
    return total_price

def part1(raw_map):
    return calc_total_price(raw_map, "standard")

def part2(raw_map):
    return calc_total_price(raw_map, "discounted")
