
with open("2022/day4/input.txt") as f:
    data = f.readlines()
    matches = 0

    for d in data:
        first, second = d.replace("\n", "").split(",")
        first_num, first_last_num = first.split("-")
        second_num, second_last_num = second.split("-")
        first_range  = list(range(int(first_num), int(first_last_num) + 1))
        second_range = list(range(int(second_num), int(second_last_num) + 1))

        if second_range[0] in first_range or second_range[:0] in first_range:
            matches += 1
        elif first_range[0] in second_range or first_range[:0] in second_range:
            matches += 1
    print(matches)