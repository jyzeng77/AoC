grid = []
visible = 0

def is_biggest_number(num, lst):
    if len(list(filter(lambda x: x >= num, lst))) == 0:
        return True
    return False

def other_trees_in_row(row, col, lst):
    left = lst[row][0:col]
    right = lst[row][col+1:]
    return left, right

def other_trees_in_col(row, col, lst):
    above = [r[col] for r in lst[0:row]]
    below = [r[col] for r in lst[row+1:]]
    return above, below

with open('p8.txt') as f:
    grid = [[int(char) for char in line.strip()] for line in f]

for row in range(len(grid)):
    for col in range(len(grid[row])):
        if row == 0 or col == 0 \
        or row == len(grid) - 1 \
        or col == len(grid[row]) - 1:
            visible += 1
        else:
            left = other_trees_in_row(row, col, grid)[0]
            right = other_trees_in_row(row, col, grid)[1]
            above = other_trees_in_col(row, col, grid)[0]
            below = other_trees_in_col(row, col, grid)[1]
            num = grid[row][col]

            if is_biggest_number(num, left) \
            or is_biggest_number(num, right) \
            or is_biggest_number(num, above) \
            or is_biggest_number(num, below):
                visible += 1
            
print(visible)
