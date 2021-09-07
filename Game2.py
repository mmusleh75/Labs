import random
# input comma separated elements as string
str = str(input("Enter comma separated list of teams: "))
print("Input string: ", str)

# conver to the list
participating_teams = str.split (",")
print("list: ", participating_teams)

#teams = ["Gold", "Steal","Platinum","Yellow","OSHS","OWHS", "OEHS"]
#teams =["team 1"]
playing_team=[]

def play_game_now(playing_team):

    if len(playing_team) < 2:
        print("not enough teams to play")
        exit(1)

    print("PLAYING TEAM: ", playing_team)


    east_team = playing_team[0]
    west_team = playing_team[1]

    east_team_score = random.randint(1, 100)
    west_team_score = random.randint(1, 100)

    if east_team_score > west_team_score:
        winning_team = east_team
        winning_team_score = east_team_score
        playing_team.remove(west_team)
    else:
        winning_team = west_team
        winning_team_score = west_team_score
        playing_team.remove(east_team)

    print("winning team:", winning_team, " /w score", winning_team_score)

if __name__ == '__main__':

    for team in participating_teams:
        # if there are two teams ready to play, then call the function
        if len(playing_team) == 2:
            play_game_now(playing_team)

        playing_team.append(team)

    play_game_now(playing_team)
