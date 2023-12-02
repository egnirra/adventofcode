def read_input() -> list[str]:
    output = []
    with open("day1/input.txt") as f:
        for line in f.readlines():
            line = line.replace("\n","")
            output.append(line)
    return output

def find_first_num(line: str):
    for char in line:
        if char.isdigit():
            return char

def main():
    input = read_input()
    result = 0
    for line in input:
        result += int(find_first_num(line) + find_first_num(line[::-1]))        
    print(result)



if __name__ == '__main__':
    main()