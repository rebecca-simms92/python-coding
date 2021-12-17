from FizzBuzz import *

""" Test cases, expected results and ceilings of the input numbers to be defined """
testcase = [105, 210, 315]
expected_result = ['FizzBuzzPop'] * 3
result = fizzbuzz_compute(315)

def set_test(testnum):
    result = fizzbuzz_compute(testnum)
    return result[testnum]

def test():
    result = []
    for i in testcase:
        result.append(set_test(i))
    for index in range(len(result)):
        if result[index] == expected_result[index]:
            print('%s pass!' % testcase[index])


if __name__ == '__main__':
    test()
