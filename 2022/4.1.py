subsets = 0

def is_subset(a,b):
    if list(filter(lambda elem: elem in b, a)) == a:
        return True
    return False

with open('p4.txt') as f:
    for line in f:
        pair = line.strip().split(',')

        elf1 = pair[0].split('-')
        elf1 = [i for i in range(int(elf1[0]), int(elf1[1])+1)]
        elf2 = pair[1].split('-')
        elf2 = [i for i in range(int(elf2[0]), int(elf2[1])+1)]
        
        if is_subset(elf1,elf2) or is_subset(elf2,elf1):
            subsets += 1

print(subsets)
