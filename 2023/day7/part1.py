import re
import numpy
from enum import Enum
from itertools import groupby
CARDS = {
    'A': 12,
    'K': 11,
    'Q': 10,
    'J': 9,
    'T': 8,
    '9': 7,
    '8': 6,
    '7': 5,
    '6': 4,
    '5': 3,
    '4': 2,
    '3': 1,
    '2': 0
}

def read_input() -> list[str]:
    output = []
    with open("2023/day7/input.txt") as f:
        for line in f.readlines():
            line = line.replace("\n","")
            output.append(line)
    return output

class CardType(Enum):
    five_of_kind = 7
    four_of_kind = 6
    full_house = 5
    three_of_kind = 4
    two_pair = 3
    one_pair = 2
    high_card = 1
    none = 0
    def __str__(self):
        cls_name = self.__class__.__name__
        return f'{cls_name}.{self.name}: {self.value}'
    def __repr__(self):
        cls_name = self.__class__.__name__
        return f'{cls_name}.{self.name}: {self.value}'
    

class Card:
    def __init__(self, cards: list, bid: str) -> None:
        self.cards_sorted = sorted(list(cards))
        self.cards = list(cards)
        self.bid = int(bid)
        self.type = CardType.none
        self.rank = 0

    def __str__(self) -> str:
        return f'\nCards: {self.cards}; Bid: {self.bid}; Type: {self.type}; Rank: {self.rank}'
    def __repr__(self) -> str:
        return f'\nCards: {self.cards}; Bid: {self.bid}; Type: {self.type}; Rank: {self.rank}'

    def find_of_kind(self) -> CardType:
        for k, g in groupby(self.cards_sorted):
            match len(list(g)):
                case 5:
                    self.type = CardType.five_of_kind
                    return self.type
                case 4:
                    self.type = CardType.four_of_kind
                    return self.type
    def find_others(self) -> CardType:
        if self.type is not CardType.none:
            return self.type
        output = [len(list(g)) for k, g in groupby(self.cards_sorted)]
        match sorted(output):
            case [2, 3]:
                self.type = CardType.full_house
            case [_, _ ,3]:
                self.type = CardType.three_of_kind
            case [_, 2, 2]:
                self.type = CardType.two_pair
            case [_, _, _, 2]:
                self.type = CardType.one_pair

        if len(set(output)) == len(self.cards_sorted):
            self.type = CardType.high_card
        return self.type

    def solve(self):
        self.find_of_kind()
        self.find_others()

def compare_equal_hands(curr: Card, next: Card):
    join = list(zip(curr.cards, next.cards))
    for curr_lbl, next_lbl in join:
        if CARDS[curr_lbl] > CARDS[next_lbl]:
            return True
        elif CARDS[curr_lbl] < CARDS[next_lbl]:
            return False
    return False

def solve(cards: list[Card]):
    for i, card in enumerate(cards):
        if i + 1 == len(cards):
            break
        if card.type is cards[i+1].type:
            curr = compare_equal_hands(card, cards[i+1])
            if curr:
                cards[i+1].rank, card.rank = card.rank, cards[i+1].rank
                cards[i+1], cards[i] = cards[i], cards[i+1]

def main():
    input_lines = read_input()

    cards = [Card(*card.split(' ')) for card in input_lines]
    for card in cards:
        card.solve()

    cards.sort(key = lambda x: x.type.value)
    for i, card in enumerate(cards, start   = 1):
        card.rank = i

    solve(cards)
    cards.sort(key = lambda x: x.rank)

    winnings = 0
    for card in cards:
        winnings += card.rank * card.bid


    print(cards)
    print(winnings)
if __name__ == '__main__':
    main()