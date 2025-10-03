# 2024 Day 7 Part 1

sample = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

def parse_sample(sample):
    lines = sample.split("\n")
    lines_split = [line.split(": ") for line in lines]
    line_list = [ [int(line[0]), [int(n) for n in line[1].split(" ")]] for line in lines_split]
    return line_list

def parse_data(file):
    line_list = []
    for line in file:
        line = line.replace("\n",'')
        line_split = line.split(": ")
        line_list.append([int(line_split[0]), [int(n) for n in line_split[1].split(" ")]])
    return line_list

def calculate_calibration(calibration_list):
    calibration = []
    for data in calibration_list:
        calibration.append(Calculator(data[0], data[1]))
    return sum([calculator.target for calculator in calibration if calculator.calc_part_1()])

def calculate_part_2(calibration_list):
    calibration = []
    for data in calibration_list:
        calibration.append(Calculator(data[0], data[1]))
    return sum([calculator.target for calculator in calibration if calculator.calc_part_2()])

class Calculator():

    class CalcNode():
        def __init__(self, val_1, val_2 = None):
            self.val_1 = val_1
            self.val_2 = val_2
            self.plus_val = val_1 + val_2
            self.multiply_val = val_1 * val_2
            self.concat_val = val_1*(10**(len(str(val_2)))) + val_2

    def __init__(self, target, vals):
        self.target = target
        root_node = vals[:2]
        child_nodes = vals[2:]
        self.nodes = [Calculator.CalcNode(root_node[0], root_node[1])]
        self.part_2_nodes = self.nodes
        for val in child_nodes:
            self.add_part_1_layer(val)
            self.add_part_2_layer(val)

    def add_part_1_layer(self, node_val):
        new_nodes = []
        for node in self.nodes:
            new_nodes.append(Calculator.CalcNode(node_val, node.plus_val))
            new_nodes.append(Calculator.CalcNode(node_val, node.multiply_val))
        self.nodes = new_nodes

    def add_part_2_layer(self, node_val):
        new_nodes = []
        for node in self.part_2_nodes:
            new_nodes.append(Calculator.CalcNode(node.plus_val, node_val))
            new_nodes.append(Calculator.CalcNode(node.multiply_val, node_val))
            new_nodes.append(Calculator.CalcNode(node.concat_val, node_val))

        self.part_2_nodes = new_nodes

    def calc_part_1(self):
        for node in self.nodes:
            if self.target == node.multiply_val or self.target == node.plus_val:
                return True
        return False

    def calc_part_2(self):
        for node in self.part_2_nodes:
            if self.target in [node.multiply_val, node.plus_val, node.concat_val] :
                return True
        return False
        


