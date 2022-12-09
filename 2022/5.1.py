import re 

stacks = []

# Flag: Collecting the items in stacks? 
# Or can we continue to the rearrangement?
taking_stock = True   

# Do we need to count the number of stacks?
counting = True

with open('ex5.txt', 'r') as f:

    for line in f:
        if counting:
            num_columns = int(len(line) / 4)
            stacks = [[]]*num_columns
            counting = False

        if taking_stock:
            processed_line = list(line[1:-1:4])
            print(processed_line)
            if '1' in processed_line:
                taking_stock = False
                continue
            else:
                for i in range(len(stacks)):
                    if not processed_line[i].isspace():
                        print(i)
                        stacks[i].insert(0, processed_line[i])
                    print(stacks)
                    
        if not taking_stock:
            print('moving')
            if line.strip() == '':
                continue
            number, move_from, move_to= re.findall(r'\d+', line)
            number, move_from, move_to = int(number), int(move_from)-1, int(move_to)-1


            stacks[move_to].extend(stacks[move_from][-number:len(stacks[move_from])])
            del stacks[move_from][-number:len(stacks[move_from])]

for stack in stacks:
    print(stack[-1],end='')
print()
