


with open("2022/day1/input.txt") as f:
    data = f.readlines()
    data_len = len(data)
    calories = []
    current = 0
    index = 0
    for d in data:
        index = index + 1
        try:
            d = int(d)
            current = current + d
        except:
            # Empty line, new Elf 
            # Add total calories from previous Elf
            calories.append(current)

            # set current to
            current = 0

        # We need to ensure last Elf is added also
        if data_len == index:
            calories.append(current)
            break
            

    calories.sort(reverse=True)
    print(f"Most calories {calories[0]}")

    print(f"Sum of top 3: {sum(calories[0:3])}")
    print(calories[0:3])