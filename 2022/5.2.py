f = open('p5.txt')
stks = []

building_stks = True

for line in f:
    if building_stks:
        if len(stks) == 0:
            stks = [[] for i in range(int(len(line)/4))]
        elif '1' in line:
            building_stks = False
            continue
        
        processed_line = list(line[1:-1:4])
        
        for i, stk in enumerate(stks):
            if processed_line[i] != ' ': 
                stk.insert(0, processed_line[i])
    
    else:
        directives = line.split()[1::2]

        if len(directives) != 0:
            move_amt, move_from, move_to = int(directives[0]), int(directives[1]) - 1, int(directives[2]) - 1
            
            stks[move_to].extend(stks[move_from][-move_amt:])
            del stks[move_from][-move_amt:]

print(''.join([stk[-1] for stk in stks]))