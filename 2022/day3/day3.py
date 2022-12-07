upper = 38 # To start at 27, if A = 65 then 65 - 38 = 27
lower = 96 # To start at 1, if a = 97 then 96 - 97 = 1

sum_prio = 0

with open("2022/day3/input.txt") as f:
    data = f.readlines()

    for d in data:
        d = d.replace("\n", "")
        text_len_div = int((len(d)) / 2)

        first, second = d[0:text_len_div], d[text_len_div::]
        equal = set(first) & set(second)
        for e in equal:
            char_num = ord(e)
            if char_num > lower:
                char_num -= lower
            else:
                char_num -= upper

            sum_prio += char_num
print(sum_prio)