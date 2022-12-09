stream = list(open('p6.txt').read())
print(stream)

# stream = list(input('Stream: '))

def duplicates_present(x):
    checked = []
    for elem in x:
        if elem in checked:
            return True
        else:
            checked.append(elem)
    return False

for i in range(len(stream)):
    marker = stream[i-14:i]

    if len(marker) != 0:
        if not duplicates_present(marker):
            print(i)
            break
