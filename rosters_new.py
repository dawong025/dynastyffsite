from datetime import datetime
import time
from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa
import json
from openpyxl import Workbook, load_workbook
from update_sheets import *
from roster import *
sc = OAuth2(None, None, from_file='oauth2.json')
gm = yfa.Game(sc, 'nfl')

leagues = gm.league_ids(year = 2023)
dynasty = gm.to_league('423.l.202017')

tms = dynasty.teams()

team_keys = []
owner_names = []
for key in tms:
    team_keys.append(key)
    owner_names.append(dynasty.teams()[key]["managers"][0]["manager"]["nickname"])

league = dict(zip(owner_names, team_keys))

def get_rosters(week):
    rosters = []
    team = []
    for i in range (0,len(team_keys)):
        for item in dynasty.to_team(team_keys[i]).roster(week):
            position = ""
            if item["eligible_positions"][0] == "D": 
                position = item["eligible_positions"][1]
            else:
                position = item["eligible_positions"][0]
            player = Player(item["name"], position, item["player_id"])
            team.append(player)
        roster = Roster(owner_names[i], team_keys[i], team)
        team = []
        rosters.append(roster)

    return rosters

rosters = get_rosters(17) 

load_team(rosters[0].owner_name, rosters[0].roster)
