import sys
def get_pyramid_sum(file):
    # reading the file: storing into single array
    with open(file) as f:
        lines = f.readlines()
    
    # splitting array: building an array of arrays
    # split \n spaces
    pyramid_string = []
    for l in lines:
        pyramid_string.append(l.split())
    
    # converting strings into ints
    pyramid_numbers = []
    for p in pyramid_string:
        numbers = []
        for s in p:
            numbers.append(int(s))
        pyramid_numbers.append(numbers)
    
    # calculating sum
    adjacent_sum = 0
    for i,p in enumerate(pyramid_numbers):
        # if odd: grab median
        if len(p) % 2 == 1:
            median_idx = len(p) // 2
            adjacent_sum += p[median_idx] # grabbing median
        else:
            median_idx = (len(p) // 2) - 1 
            adjacent_sum += p[median_idx]
            
        print(f'Adding: {p[median_idx]} from row: {i+1}')
    
    # return, print
    print(f'The total sum: {adjacent_sum}')
    
if __name__ == "__main__":
    file = sys.argv[1]
    get_pyramid_sum(file)