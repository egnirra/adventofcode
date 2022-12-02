import sys
abc = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors'
}
 
xyz = {
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors'
}

lookup = {
    'Rock': 'Scissors',
    'Paper': 'Rock',
    'Scissors': 'Paper'
}
points = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3
}

"Rock => Scissors"
"Paper => Rock"
"Scissors => Paper"


games_played = []

with open("2022/day2/input.txt") as f:
    data = f.readlines()
    
    for d in data:
        d = d.replace("\n","")
        opponent = abc.get(d[0])
        me = xyz.get(d[2])

        if me == opponent:
            # Draw 3 points
            games_played.append(3 + points[me])
        elif lookup[me] == opponent:
            # I win 6 points
            games_played.append(6 + points[me])
        else:
            # I lost = 0 points
            games_played.append(points[me])



print(sum(games_played))