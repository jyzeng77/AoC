calories = []
curr_total = 0

with open('p1.txt', mode='r') as f:
    for line in f:
        try: 
            curr_total += int(line.strip())
        except BaseException as e:
            print(e)
            calories.append(curr_total)
            curr_total = 0

print(max(calories))
