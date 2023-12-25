import re
import numpy
import time as Time

def read_input() -> list[str]:
    output = []
    with open("2023/day6/input.txt") as f:
        for line in f.readlines():
            line = line.replace("\n","")
            output.append(line)
    return output

class Race:
    def __init__(self, time: str, distance: str) -> None:
        self.time = int(time)
        self.distance = int(distance)

    def __str__(self) -> str:
        return f'time: {self.time} distance: {self.distance}'
    def __repr__(self) -> str:
        return f'\ntime: {self.time} distance: {self.distance}'
    
    def calc_winning_races(self):
        output = 0
        for time in range(0, self.time + 1):
            distance = (self.time - time) * time
            if distance > self.distance:
                output += 1
            elif distance < self.distance and output > 1:
                break
        return output




def main():
    input_lines = read_input()
    time = re.findall(r'\b\d+\b', input_lines[0].replace(' ',''))
    distance = re.findall(r'\b\d+\b', input_lines[1].replace(' ',''))
    joined = list(zip(time, distance))
    races = [Race(*race) for race in joined]
    wins = [race.calc_winning_races() for race in races]
    

    print(numpy.prod(wins))
if __name__ == '__main__':
    main()