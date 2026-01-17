
def parse_map(raw_map):
    rows = raw_map.split('\n')
    return [list(row) for row in rows]

class Region():
    def __init__(self, parsed_map, starting_cell):
        self.garden = parsed_map
        self.nrow = len(parsed_map)
        self.ncol = len(parsed_map[0])
        self.plots = set()
        self.starting_cell = starting_cell
        self.value = self.get_value(*starting_cell)
        self.find_garden_cells()
        self.calculate_perimeter()
        self.calculate_sides()
        
    def price(self):
        return self.area * self.perimeter
    def discounted_price(self):
        return self.area * self.sides

    def find_garden_cells(self):
        self.area = 0
        stack = [self.starting_cell]

        while stack:
            r, c = stack.pop()
            if (r, c) in self.plots:
                continue
            
            self.plots.add((r, c))
            self.area += 1

            for ortho_r, ortho_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if (ortho_r, ortho_c) not in self.plots and self.get_value(ortho_r, ortho_c) == self.value:
                    stack.append((ortho_r, ortho_c))
    
    def calculate_perimeter(self):
        self.perimeter = 0
        for r, c in self.plots:
            for ortho_r, ortho_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if (ortho_r, ortho_c) not in self.plots:
                    self.perimeter += 1

    def calculate_sides(self):
        self.sides = 0
        for r, c in self.plots:
            d = (r+1, c) in self.plots
            u = (r-1, c) in self.plots
            rt = (r, c+1) in self.plots
            l = (r, c-1) in self.plots
            ul = (r-1, c-1) in self.plots
            ur = (r-1, c+1) in self.plots
            dl = (r+1, c-1) in self.plots
            dr = (r+1, c+1) in self.plots

            self.sides += sum([u and l and not ul,
                                u and rt and not ur,
                                d and l and not dl,
                                d and rt and not dr,
                                not u and not l,
                                not u and not rt,
                                not d and not l,
                                not d and not rt])

    def get_value(self, row, col):
        if row < 0 or col < 0 or row > self.nrow-1 or col > self.ncol-1:
            return None
        return self.garden[row][col]

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
