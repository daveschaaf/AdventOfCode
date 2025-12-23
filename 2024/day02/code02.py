## 2024 Day 2, Part 1
def part1(data):
    """
    Determines the number of safe reports in an array of reports
    
    A report is safe based on 2 rules:
        Rule 1: Reports are strictly monotonic (all increasing or all decreasing)
        Rule 2: Any two adjacent levels differ by at least one and at most three.
    
    Args:
        data: a list of lists with a series of integers

    Returns:
        int: the number of safe reports in the original data
        list: a list of the reports that are determined to be unsafe
    """
    
    safe: int = 0

    unsafe_reports: [list] = []

    for raw_report in data:
        
        # Normalize the monotonicity by determining which direction
        # the series should be (in/de)creasing
        if raw_report[-1] - raw_report[0] > 0:
            direction = 1
        else:
            direction = -1
        
        # Find the difference between 2 consecutive elements and normalize it
        # by multiplying by out expected direction
        deltas = [direction * (raw_report[i] - raw_report[i - 1]) for i in range(1,len(raw_report))]
        
        # Check that all differences between 2 consecutive values are in 1-3
        rules = all([n >= 1 and n<= 3 for n in deltas])
        
        if rules:
            safe += 1
        else:
            unsafe_reports.append(raw_report)
    
    return safe, unsafe_reports



# Part 2

def part2(data):
    """
    Check a list of unsafe reports to determine if they can be safe with dampening

    A report is safe with dampening if it would pase Rule 1 and Rule 2 after
    removing exactly 1 value

    Args:
        data: a list of reports

    Returns:
        int: the number reports that are safe with dampening
    """

    safe_dampened_reports: int = 0

    for raw_report in data:
        
        # Create an array of dampened reports: 1 with each possible value removed
        dampened_reports: [list] = [raw_report[:i] + raw_report[i+1:] for i in range(len(raw_report))]
        
        # Check all the dampened_reports against out part 1 algorithm
        safe, _ = part1(dampened_reports)
        if safe > 1:
            print(safe)
        
        # if any of them are safe then the original report is safe when dampened  
        if safe > 0:
            safe_dampened_reports += 1

    return safe_dampened_reports



if __name__ == "__main__":

    data: [list] = []

    with open("02_data.txt", "r") as file:
        for line in file:
            line = line.split(' ')
            line[-1] = line[-1].replace("\n", "")
            line = [int(n) for n in line]
            data.append(line)

    part1_solution, part2_data = part1(data)
    print("Solution to 2024 Day 2, Part 1:")
    print(part1_solution)
    # 572
    
    # Pass only the unsafe reports from Part 1 into Part 2
    part2_solution = part2(part2_data)
    print("Solution to 2024 Day 2, Part 2:")
    print(part2_solution + part1_solution)
    # 612
    
