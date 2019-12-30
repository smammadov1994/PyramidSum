# Pyramid Sum
*requirements: ```python 3.^```

## 1. Installing
Git clone this repository
```
git clone www.github.com/smammadov1992/PyramidSum.git
```

## 2. Running File
In this repisitory you will find ```triangle.txt``` which is the text file we will sort through and add the adjecent sum (adjacent row below).

To run the algorithm simple run

```
python pyramid_sum.py triangle.txt
```

You can change ```triangle.txt``` to any other file with the same format. 

## Algorithm
The algorithm to sort and add the adjacent sum is:
```python
# 1. Reading raw text file
with open(file) as f:
    lines = f.readlines()

# 2. splitting array: building an array of arrays
# split \n spaces
pyramid_string = []
for l in lines:
    pyramid_string.append(l.split())

# 3. converting strings into ints
pyramid_numbers = []
for p in pyramid_string:
    numbers = []
    for s in p:
        numbers.append(int(s))
    pyramid_numbers.append(numbers)

# 4. calculating sum
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

# 5. return, print
print(f'The total sum: {adjacent_sum}')
    
```