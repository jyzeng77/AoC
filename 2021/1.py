prev_num = 0
increases = 0

interval = 50
chunk = [0, interval] # My computer can't read all the data at once so I need to process in 50 ln intervals

with open("p1.txt", "r", buffering=10000000) as f:
    txt = f.readlines()
    for i in range(len(txt)//interval + 1):
        for line in txt[chunk[0]:chunk[1]]:
            curr_num = int(line)
            print(curr_num)
            if curr_num > prev_num and prev_num != 0:
                increases += 1
                print("increase")
            prev_num = curr_num
        chunk[0] += 50; chunk[1] += 50

print(increases)
