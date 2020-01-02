# Pyramid Sum

\*requirements: `python 3.^`

## 1. Installing

Git clone this repository

```
git clone www.github.com/smammadov1992/PyramidSum.git
```

## 2. Running File

In this repisitory you will find `triangle.txt` which is the text file we will sort through and add the adjecent sum (adjacent row below).
To run the algorithm simple run

```
python pyramid_sum.py triangle.txt
```

You can change `triangle.txt` to any other file with the same format.

## Algorithm

The algorithm to sort and add the adjacent sum is:

```python
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
```
