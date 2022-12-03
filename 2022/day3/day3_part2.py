upper = 38 # To start at 27, if A = 65 then 65 - 38 = 27
lower = 96 # To start at 1, if a = 97 then 96 - 97 = 1

sum_prio = 0

with open("2022/day3/input.txt") as f:
    data = f.readlines()
    idx = 0
    current = list()
    for d in data:
        d = d.replace("\n", "")
        current.append(d)
        idx = idx + 1
        if idx == 3:
            equal = set(current[0]).intersection(set(current[1])).intersection(set(current[2]))
            current = list()
            idx = 0
            for e in equal:
                char_num = ord(e)
                if char_num > lower:
                    char_num = char_num - lower
                else:
                    char_num = char_num - upper

                sum_prio = sum_prio + char_num
print(sum_prio)