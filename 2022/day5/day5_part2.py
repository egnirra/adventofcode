



def crates(data) -> list:
    array = []
    temp_arr = []
    for d in data:
        d = d.replace("\n", "")
        if "move" in d:
            break
        try:
            int(d)
            temp_arr.reverse()
            array.append(temp_arr)
            temp_arr = []
        except:
            temp_arr.append(d.replace("[","").replace("]",""))

    return array

def moves(data) -> list:
    moves = []
    d: str
    for d in data[66:]:
        d = d.replace("\n", "")
        move = d.replace("move ","").replace("from ","").replace("to ","").split(" ")

        moves.append(move)
    return moves


with open("2022/day5/input.txt") as f:
    data = f.readlines()
    matches = 0
    crate_arr = crates(data)
    move_creates = moves(data)
    for move in move_creates:
        for crate_from in move[1]:
            _move = int(move[0])
            popped_item = crate_arr[int(crate_from) - 1][-_move:]
            del crate_arr[int(crate_from) - 1][-_move:]
            for p in popped_item:
                crate_arr[int(move[2]) - 1].append(p)

    result = ""
    c: list
    for c in crate_arr:
        result += c[-1]
    print(result)