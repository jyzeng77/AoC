priority = ''.join([chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(i) for i in range(ord('A'), ord('Z') + 1)])
score = 0

with open('p3.txt', mode='r') as f:
    for line in f:
        midpoint = int(len(line) / 2)
        a = line[0:midpoint]
        b = line[midpoint:-1]
        
        for char in a:
            if b.find(char) != -1:
                score += priority.find(char) + 1
                break

print(score)
