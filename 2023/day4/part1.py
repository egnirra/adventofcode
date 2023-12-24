import re

class Card:
    def __init__(self, id: int, my_numbers: list[int], winning_numbers: list[int]) -> None:
        self.id = id
        self.my_numbers = my_numbers
        self.winning_numbers = winning_numbers
        self.matched_numbers = list()
        self.total_points = 0


    def calc_points(self):
        if len(self.matched_numbers) == 0:
            return 0
        if len(self.matched_numbers) == 1:
            return 1
        
        total = 1
        for _ in range(1, len(self.matched_numbers)):
            total = total * 2
        self.total_points = total
        return total
    
    def match_numbers(self):
        self.matched_numbers = [num for num in self.my_numbers if num in self.winning_numbers]
        return self.matched_numbers
            
    def __str__(self) -> str:
        return f'id: {self.id}\nmy_numbers: {self.my_numbers}\nwinning_numbers: {self.winning_numbers}\nmatched_numbers: {self.matched_numbers}'
    def __repr__(self) -> str:
        return f'id: {self.id}\nmy_numbers: {self.my_numbers}\nwinning_numbers: {self.winning_numbers}\nmatched_numbers: {self.matched_numbers}'

def parse_card(line: str):
    card_id = line[5]
    winning_numbers, my_numbers = re.sub('^(.*?):\s', '', line).replace('  ', ' ').split(' | ')
    winning_numbers = [int(win_num) for win_num in winning_numbers.split(' ') if win_num.isdigit()]
    my_numbers = [int(my_num) for my_num in my_numbers.split(' ') if my_num.isdigit()]
    return Card(card_id, my_numbers, winning_numbers)

def read_input() -> list[str]:
    output = []
    with open("2023/day4/input.txt") as f:
        for line in f.readlines():
            line = line.replace("\n","")
            output.append(line)
    return output


def main():
    input_lines = read_input()
    cards = [parse_card(card) for card in input_lines]

    output = 0
    for card in cards:
        card.match_numbers()
        output += card.calc_points()
    print(output)


    #print(input_lines)
if __name__ == '__main__':
    main()