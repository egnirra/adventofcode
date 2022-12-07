def item_priority(item):
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38

total_priority = 0

with open('2022/day3/input.txt') as f:
    for line in f:
        first_compartment = set(line[:len(line)//2])
        second_compartment = set(line[len(line)//2:])
        intersection = first_compartment & second_compartment
        priority = item_priority(list(intersection)[0])
        total_priority += priority

print(total_priority)