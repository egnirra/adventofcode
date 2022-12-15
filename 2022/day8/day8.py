
visable_pos = set()
default_vis = []

def part_one(array):
    for x in range(len(array)): # left to right
        current = 0
        previous = []
        for y in range(len(array[0])):
            previous.append(int(current))
            previous.sort(reverse=True)
            current = int(array[x][y])

            checkxy(previous, (current, x, y))

    for x in range(len(array)): # right to left
        current = 0
        previous = []
        for y in range(len(array[0])):
            previous.append(int(current))
            previous.sort(reverse=True)
            current = int(array[x][::-1][y])

            checkxy(previous, (current, x, len(array[0]) - 1 - y))

    for x in range(len(array[0])): # up to down
        current = 0
        previous = []
        for y in range(len(array)):
            previous.append(int(current))
            previous.sort(reverse=True)
            current = int(array[y][x])

            checkxy(previous, (current, y, x))

    for x in range(len(array[0])): # down to up
        current = 0
        previous = []
        for y in range(len(array)):
            previous.append(int(current))
            previous.sort(reverse=True)
            current = int(array[::-1][y][x])
            checkxy(previous, (current, len(array) - 1 - y, x))

def checkxy(previous: list, current: tuple):

    if current[0] > previous[0]:
        visable_pos.add(current)
    else:
        return

with open("2022/day8/input.txt") as f:
    array = []
    array_rev = []
    for line in f.readlines():
        line = line.replace("\n","")
        array.append([*line])
        array_rev.append([*line[::-1]])
        
    part_one(array)

    vis_corners = len(array[0])
    vis_corners = (vis_corners - 1) * 4
    vis = []

    for v in visable_pos:
        match v:
            case [_, 0, _]:
                pass
            case [_, 98, _]:
                pass
            case [_, _, 0]:
                pass
            case [_, _, 98]:
                pass
            case _:
                vis.append(v)
                vis.sort()
    for v in vis:
        print(v)
    print(len(vis) + vis_corners)