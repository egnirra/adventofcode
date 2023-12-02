from itertools import groupby

class Cube:
    def __init__(self, count: int, color: str) -> None:
        self.color = color
        self.count = count

    def __str__(self) -> str:
        return self.color

    def __repr__(self) -> str:
        return self.color

class Game:
    def __init__(self, game: int) -> None:
        self.game = game
        self.cubes = []

    def __str__(self) -> str:
        return f'Game {self.game}: {self.cubes}'

    def __repr__(self) -> str:
        return f'Game {self.game}: {self.cubes}'
    
    def add_cube(self, cube: Cube):
        self.cubes.append(cube)

def read_input() -> list[str]:
    output = []
    with open("day2/input.txt") as f:
        for line in f.readlines():
            line = line.replace("\n","")
            output.append(line)
    return output



def main():
    input = read_input()
    count_game = 0
    for i in input:
        split_game = i.split(': ')
        games = Game(int(split_game[0].replace('Game ','')))
        split_cube = split_game[1].split('; ')
        for cube_list in split_cube:
            cubes = cube_list.split(', ')
            for cube in cubes:
                c = cube.split(' ')
                games.add_cube(Cube(int(c[0]), c[1]))
        add_game = True
        for cube in games.cubes:
            if cube.color == 'red' and cube.count > 12:
                add_game = False
            if cube.color == 'green' and cube.count > 13:
                add_game = False
            if cube.color == 'blue' and cube.count > 14:
                add_game = False

        if add_game:
            count_game += games.game
    print(count_game)


if __name__ == '__main__':
    main()