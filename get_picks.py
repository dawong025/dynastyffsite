'''
get_picks.py - Used to get the default draft position per owner pre-trades.

Reverse draft position for bottom 6 seeds, higher pick for winner of consolation 
match for playoff teams (e.g. winner of 5vs6 matchup gets 1.07)
'''

from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa
import operator

sc = OAuth2(None, None, from_file='oauth2.json')
gm = yfa.Game(sc, 'nfl')
leagues = gm.league_ids(year = 2023)
dynasty = gm.to_league('423.l.202017')

team_names = []
owner_names = []

# iterate through initial dictionary to get team_key
list_team_keys = list(dynasty.teams().keys())
# Get list of team names

for key in list_team_keys:
    print(dynasty.teams()[key])
    if "\'" in dynasty.teams()[key]["name"]:
        continue
    else:
        team_names.append(dynasty.teams()[key]["name"])
        owner_names.append(dynasty.teams()[key]["managers"][0]["manager"]["nickname"])
league = dict(zip(owner_names, team_names))

# print(organization)
    # 1 -> 12
    # 2 -> 11
    # 3 -> 9
    # 4 -> 10
    # 5 -> 7
    # 6 -> 8
    # no change to bottom 6, just flip order
orig_pick_positions = []
for key in dynasty.standings():
    pick = 0
    if key["rank"] < 7:
        match key["rank"]:
            case 1: pick = 12
            case 2: pick = 11
            case 3: pick = 9
            case 4: pick = 10
            case 5: pick = 7
            case 6: pick = 8
            case _: pick = 0
    else:
        match key["playoff_seed"]:
            case "7": pick = 6
            case "8": pick = 5
            case "9": pick = 4
            case "10": pick = 3
            case "11": pick = 2
            case "12": pick = 1
            case _: pick = 0            

    pick_position = {
        "name": key["name"],
        "pick": pick
    }
    orig_pick_positions.append(pick_position)

orig_pick_positions = sorted(orig_pick_positions, key = operator.itemgetter("pick"))
for item in orig_pick_positions:
    print(item["name"] + " - " + str(item["pick"]))


