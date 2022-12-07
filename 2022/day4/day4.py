
with open("2022/day4/input.txt") as f:
    data = f.readlines()
    matches = 0

    for d in data:
        first, second = d.replace("\n", "").split(",")
        first_num, first_last_num = first.split("-")
        second_num, second_last_num = second.split("-")


        
        first_range = range(int(first_num), int(first_last_num))
        second_range = range(int(second_num), int(second_last_num))
        
        if second_range.start >= first_range.start and second_range.stop <= first_range.stop:
            print(first_range)
            print(second_range)
            matches += 1
        elif first_range.start >= second_range.start and first_range.stop <= second_range.stop:
            print(first_range)
            print(second_range)
            matches += 1

    print(matches)