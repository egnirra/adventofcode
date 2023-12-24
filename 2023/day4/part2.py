import re
def read_input() -> list[str]:
    output = []
    with open("2023/day4/input.txt") as f:
        for line in f.readlines():
            line = line.replace("\n","")
            output.append(line)
    return output
class Card:
    def __init__(self, id: int, my_numbers: list[int], winning_numbers: list[int]) -> None:
        self.id = id
        self.my_numbers = my_numbers
        self.winning_numbers = winning_numbers
        self.matched_numbers = list()
        self.total_points = 0


    def calc_points(self):        
        self.total_points = len(self.matched_numbers)
        return self.total_points
    
    def match_numbers(self):
        self.matched_numbers = [num for num in self.my_numbers if num in self.winning_numbers]
        return self.matched_numbers
            
    def __str__(self) -> str:
        return f'\nid: {self.id}\nmy_numbers: {self.my_numbers}\nwinning_numbers: {self.winning_numbers}\nmatched_numbers: {self.matched_numbers}\n'
    def __repr__(self) -> str:
        return f'\nid: {self.id}\nmy_numbers: {self.my_numbers}\nwinning_numbers: {self.winning_numbers}\nmatched_numbers: {self.matched_numbers}\n'

def parse_card(line: str):
    winning_numbers, my_numbers = line.split(' | ')

    my_numbers = re.findall(r'\b\d+\b', my_numbers)
    winning_numbers = re.findall(r'\b\d+\b', winning_numbers)

    card_id = int(winning_numbers.pop(0))

    winning_numbers = [int(win_num) for win_num in winning_numbers]
    my_numbers = [int(my_num) for my_num in my_numbers]
    return Card(card_id, my_numbers, winning_numbers)

def copy_card(card: Card):
    pass




def main():
    input_lines = read_input()
    cards = [parse_card(card) for card in input_lines]

    number_cards = 0
    new_cards = []
    for c, card in enumerate(cards, start=1):
        print(c)
        card.match_numbers()
        card.calc_points()
        if card.total_points == 0:
            new_cards.append(card)
            continue

        until = c + card.total_points
        if until >= len(cards):
            until = len(cards)

        extra_cards = [copy for copy in new_cards if copy.id == card.id]
        for extra in extra_cards:
            for new in cards[c:until]:
                new_cards.append(new)

        for new in cards[c:until]:
            new_cards.append(new)
        new_cards.append(card)

        

    new_cards.sort(key = lambda card: card.id)
    print(len(new_cards))


    #print(input_lines)
if __name__ == '__main__':
    main()