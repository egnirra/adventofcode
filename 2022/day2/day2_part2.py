import sys
abc = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors'
}

win_lose_Draw = {
    'X': 'Lose',
    'Y': 'Draw',
    'Z': 'Win'
}
win_lookup = {
    'Rock': 'Scissors',
    'Paper': 'Rock',
    'Scissors': 'Paper'
}
lose_lookup = {
    'Rock': 'Paper',
    'Paper': 'Scissors',
    'Scissors': 'Rock'
}

points = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3
}

games_played = []

with open("2022/day2/input.txt") as f:
    data = f.readlines()
    
    for d in data:
        d = d.replace("\n","")

        opponent = abc.get(d[0])
        outcome = win_lose_Draw[d[2]]

        if outcome == "Draw":
            # Draw 3 points
            games_played.append(3 + points[opponent])
        elif outcome == "Win":
            # I win 6 points
            winning = lose_lookup[opponent]
            games_played.append(6 + points[winning])
        elif outcome == "Lose":
            # I lost = 0 points
            losing = win_lookup[opponent]
            games_played.append(points[losing])



print(sum(games_played))