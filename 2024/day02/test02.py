from code02 import part1, part2

# Part 1

def test_part1():

    data = [[1,2,3]]
    safe_report_count, unsafe_report_data = part1(data)
    assert safe_report_count == 1, "Part 1 returns the count of safe reports"
    assert unsafe_report_data == [], "Returns the list of unsafe reports"

    unsafe_report = [-1,1,-1]
    data = [[1,2,3], unsafe_report]
    safe_report_count, unsafe_report_data = part1(data)
    assert safe_report_count == 1, "Part 1 returns the count of safe reports"
    assert unsafe_report_data == [unsafe_report], "Returns the list of unsafe reports"



def test_part2_inludes():

    def assert_included_report(data, expectation=1):
        dampened_report_count = part2([data])
        assert dampened_report_count == expectation

    assert_included_report([29, 32, 30, 31, 34, 35, 37])
    assert_included_report([91, 94, 93, 96, 97])
    assert_included_report([2, 5, 6, 8, 6])
    assert_included_report([73, 71, 69, 68, 65, 66, 62])
    assert_included_report([1,2,3,4,5,6])
    assert_included_report([1, 6, 4, 6, 7, 8, 10])

def test_part2_excludes():
    def assert_excluded_report(data, expectation=0):
        dampened_report_count, safe, error = part2([data])
        assert dampened_report_count == expectation, "Unsafe reports with 2 errors are excluded"

    data = [[9,4,8,2,5,4,3,2]]
    dampened_report_count = part2(data)
    assert dampened_report_count == 0, "Unsafe reports with 2 errors are excluded"

    data = [[9,10,8,9,5,4,3,2]]
    dampened_report_count = part2(data)
    assert dampened_report_count == 0, "Unsafe reports with 2 errors are excluded"

    data = [[-1,4,-4,-5,-9,-6,-7]]
    dampened_report_count = part2(data)
    assert dampened_report_count == 0, "Unsafe reports with 2 errors are excluded"

