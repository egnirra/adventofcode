
with open("2022/day6/input.txt") as f:
    data = f.readline()
    last = ""
    count = 14
    for d in range(len(data)):
        check = set(data[d:count])
        if len(check) == 14:
            print(f"Number of chars needed: {d + 14}")
            break
        count += 1
        

