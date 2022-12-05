import re 

# Flag: Collecting the items in stacks? 
# Or can we continue to the rearrangement?
taking_stock = True   

with open('ex5.txt', 'r') as f:
    num_columns = int(len(f.readline()) / 4)
    stacks = [[] for i in range(num_columns)]

    for line in f:
        print(line)

