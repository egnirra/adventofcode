def read_input() -> list[str]:
    output = []
    with open("2023/day3/input.txt") as f:
        for line in f.readlines():
            line = line.replace("\n","")
            output.append(line)
    return output

def find_index_number(input_lines) -> list[tuple]:
    output = []
    for c, input in enumerate(input_lines):
        number = ''
        last = 0
        for i, num in enumerate(input):
            if num.isdigit():
                last = i
                number += num
            elif last + 1 == i and number != '':
                output.append((c, i - 1, number))
                number = ''
            if i == len(input) - 1 and number != '':
                output.append((c, i, number))

                
    return output

def find_index_char(input_lines) -> list[tuple]:
    output = []
    numbers = [f"{i}" for i in range(1, 10)]
    for c, input in enumerate(input_lines):
        for i, num in enumerate(input):
            if num != '.' and num not in numbers:
                output.append((c, i, num))


    return output


def process_numbers_chars(numbers: tuple, chars: list[tuple], len_lines: int, len_row: int):
    number_line = numbers[0]
    number_row = numbers[1]
    number_num = numbers[2]
    check_above = True
    check_below = True
    check_before = True
    check_after = True
    len_nums = len(number_num) - 1
    before = number_row - len_nums - 1
    after = number_row + 1
    range_nums = list(range(before, after + 1))
    if number_row - len_nums == 0:
        check_before = False
    elif number_row == len_row:
        check_after = False

    if number_line == 0:
        check_above = False
    elif number_line == len_lines:
        check_below = False

    for char in chars:
        char_line = char[0]
        char_row = char[1]
        if check_above and char_row in range_nums and char_line == number_line - 1:
            return numbers
        if check_below and char_row in range_nums and char_line == number_line + 1:
            return numbers
        if check_before and char_row == before and char_line == number_line:    
            return numbers
        if check_after and char_row == after and char_line == number_line:
            return numbers
            


def main():
    input_lines = read_input()
    numbers = find_index_number(input_lines)
    chars = find_index_char(input_lines)
    all_found = []
    output = 0
    for c, num in enumerate(numbers):
        numbers_found = process_numbers_chars(num, chars, len(input_lines), len(input_lines[0]) - 1)
        if numbers_found is not None:
            all_found.append(numbers_found)
            output += int(numbers_found[2])

    print(output)
if __name__ == '__main__':
    main()