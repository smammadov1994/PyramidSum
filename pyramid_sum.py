import sys
# 1.


def convert_2_numbers(file):
    """
    helper function to convert a file into an array of numbers. This will be the basis of our data in integers to build our path algorithm
    """
    # 1. reading lines
    with open(file) as f:
        lines = f.readlines()
    # 2. converting to array of strings
    pyramid_string = [l.split() for l in lines]
    # 3. converting to numbers to perform operations
    pyramid_numbers = [[int(s) for s in p] for p in pyramid_string]
    return pyramid_numbers
# 2.


def maximum_path_finding_sum(value, m):
    """
    Path finding algorithm
    """
    # loop for bottom-up calculation
    for i in range(m-1, -1, -1):
        for j in range(i+1):
            # for each element, check both
            # elements just below the number
            # and below right to the number
            # add the maximum of them to it
            if (value[i+1][j] > value[i+1][j+1]):
                value[i][j] += value[i+1][j]
            else:
                value[i][j] += value[i+1][j+1]
    # return the top element
    # which stores the maximum sum
    return value[0][0]


if __name__ == "__main__":
    file = sys.argv[1]
    value = convert_2_numbers(file)
    max_path_sum = maximum_path_finding_sum(value, len(value)-1)
    print(f'The optimal path sum is: {max_path_sum}')
