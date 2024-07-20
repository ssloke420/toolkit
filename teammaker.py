players = []
n = int(input("How many people are playing? "))
for i in range(n):
    name = input(f"Player {i+1} name? ")
    score = float(input(f"Player {i+1} rating out of 10? "))
    players.append((name, score)) 

# Sort players by their rating in descending order
players.sort(key=lambda x: x[1], reverse=True)

team1 = []
team2 = []
team1_score = 0
team2_score = 0

# Distribute players to teams to balance their ratings
for player in players:
    if team1_score <= team2_score:
        team1.append(player)
        team1_score += player[1]
    else:
        team2.append(player)
        team2_score += player[1]

# Print Team 1
print("Team 1:")
for player in team1:
    print(f"{player[0]} with rating {player[1]}")

# Print Team 2
print("\nTeam 2:")
for player in team2:
    print(f"{player[0]} with rating {player[1]}")
