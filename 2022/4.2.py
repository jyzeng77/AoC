overlapped = 0

def has_intersection(a,b):
    if len(list(filter(lambda x: x in b, a))) != 0:
        return True
    return False

with open('p4.txt') as f:
    for line in f:
        pair = line.strip().split(',')

        elf1 = pair[0].split('-')
        elf1 = [i for i in range(int(elf1[0]), int(elf1[1])+1)]
        elf2 = pair[1].split('-')
        elf2 = [i for i in range(int(elf2[0]), int(elf2[1])+1)]
        
        if has_intersection(elf1,elf2):
            overlapped += 1

print(overlapped)
