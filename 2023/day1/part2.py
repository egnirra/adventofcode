def read_input() -> list[str]:
    output = []
    with open("day1/input.txt") as f:
        for line in f.readlines():
            line = line.replace("\n","")
            output.append(line)
    return output

def word_to_num(line: str):
    words = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    replace_at = []
    for word in words:
        last = 0
        for count in range(10):
            index = None
            try:
                index = line.index(word, last)
            except:
                pass
            if index is not None:
                last = index + 1
                replace_at.append((index, words[word]))
    if replace_at == []:
        output = line
    
    list_line = list(line)
    for replace in replace_at:
        index = replace[0]
        number = replace[1]
        list_line[index] = str(number)
        output = "".join(list_line)
    return output


def find_first_num(line: str):
    for char in line:
        if char.isdigit():
            return char

def main():
    input = read_input()
    result = 0
    for line in input:
        line = word_to_num(line)
        print(line)
        result += int(find_first_num(line) + find_first_num(line[::-1]))        
    print(result)

#55639

if __name__ == '__main__':
    main()