from collections import defaultdict


def parse_data(filename):
    output = defaultdict(list)
    labels = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water',
              'water-to-light', 'light-to-temperature', 'temperature-to-humidity',
              'humidity-to-location']
    key = labels[0]
    label_line = False
    with open(filename, 'r') as file:
        for line in file:
            line.replace('\\n', '')
            if 'seeds' in line:
                output['seeds'] = list(map(int,line.split(" ")[1:]))
                continue
            for label in labels:
                if label in line:
                    key = label
                    label_line = True
            if not label_line and line != "\n":
                codex = [int(x) for x in line.split(' ')]
                output[key].append(codex)
            label_line = False
    return output
            
def seed_to_soil(num, conversion_tables):
    return num
    
    
