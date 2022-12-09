
with open("2022/day6/input.txt") as f:
    data = f.readline()
    last = ""
    count = 4
    for d in range(len(data)):
        check = set(data[d:count])
        if len(check) == 4:
            print(f"Number of chars needed: {d + 4}")
            break
        count += 1
        

