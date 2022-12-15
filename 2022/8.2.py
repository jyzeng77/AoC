grid = []

def trees_visible(num, lst, inverse=False):
    # Inverse is for lists that have closer trees at the end
    visible = 0
    if inverse:
        # Remember that this affects the list arg directly
        lst.reverse() 
        
    for elem in lst:
        if elem < num:
            visible += 1
        else:
            visible += 1
            break
    
    return visible

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

high_score = 0

for row in range(len(grid)):
    for col in range(len(grid[row])):
        num = grid[row][col]
        left = trees_visible(num, other_trees_in_row(row, col, grid)[0], inverse=True)
        right = trees_visible(num, other_trees_in_row(row, col, grid)[1])
        above = trees_visible(num, other_trees_in_col(row, col, grid)[0],inverse=True)
        below = trees_visible(num, other_trees_in_col(row, col, grid)[1])
        score = left * right * above * below
        if score > high_score:
            high_score = score

print(high_score)
