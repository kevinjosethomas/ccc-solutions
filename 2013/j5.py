from copy import deepcopy

my_team = int(input())
num_of_games = int(input())
teams = {
    1: {"score": 0, "games": []},
    2: {"score": 0, "games": []},
    3: {"score": 0, "games": []},
    4: {"score": 0, "games": []},
}

for _ in range(num_of_games):

    game = list(map(int, input().split()))

    teams[game[0]]["games"].append(game[1])
    teams[game[1]]["games"].append(game[0])

    if game[2] > game[3]:
        teams[game[0]]["score"] += 3
    elif game[2] < game[3]:
        teams[game[1]]["score"] += 3
    else:
        teams[game[0]]["score"] += 1
        teams[game[1]]["score"] += 1

remaining_games = []

for team in teams.keys():
    if len(teams[team]["games"]) == 3:
        continue

    possible_teams = [1, 2, 3, 4]
    possible_teams.remove(team)

    for game in teams[team]["games"]:
        possible_teams.remove(game)

    for pt in possible_teams:
        missing_game = sorted([team, pt])
        if missing_game not in remaining_games:
            remaining_games.append(missing_game)

possible_wins = 0

# print(teams)


def calculate_remaining_games(teams_, rem_games):

    if not rem_games:
        highest_team = 0
        highest_score = 0

        scores = [teams_[t]["score"] for t in teams_.keys()]
        if scores.count(max(scores)) > 1:
            return

        for t in teams_.keys():
            if teams_[t]["score"] > highest_score:
                highest_score = teams_[t]["score"]
                highest_team = t

        global possible_wins

        if highest_team == my_team:
            possible_wins += 1

        return

    game = rem_games[0]
    rem_games.pop(0)

    # if first team wins
    t1_win_teams = deepcopy(teams_)
    t1_win_teams[game[0]]["score"] += 3

    # print("t1 win:")
    # print(t1_win_teams)
    # print("\n\n")

    calculate_remaining_games(t1_win_teams, [g for g in rem_games])

    # if second team wins
    t2_win_teams = deepcopy(teams_)
    t2_win_teams[game[1]]["score"] += 3

    # print("t2 win:")
    # print(t2_win_teams)
    # print("\n\n")

    calculate_remaining_games(t2_win_teams, [g for g in rem_games])

    # if tied
    tied_teams = deepcopy(teams_)
    tied_teams[game[0]]["score"] += 1
    tied_teams[game[1]]["score"] += 1

    # print("tied:")
    # print(tied_teams)
    # print("\n\n")

    calculate_remaining_games(tied_teams, [g for g in rem_games])


calculate_remaining_games(teams, remaining_games)

print(possible_wins)
