priority = ''.join([chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(i) for i in range(ord('A'), ord('Z') + 1)])
score = 0

with open('p3.txt', mode='r') as f:
    group = []

    for i, line in enumerate(f, start=1):
        group.append(line)

        if i % 3 == 0:
            a,b,c = group[0], group[1], group[2]
            for char in a:
                if b.find(char) != -1 and c.find(char) != -1:
                    score += priority.find(char) + 1
                    break
            group.clear()

print(score)
