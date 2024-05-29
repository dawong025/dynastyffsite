# rosters.py - A file to load dynasty rosters onto an excel spreadsheet

from datetime import datetime
import time
from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa
import json
from openpyxl import Workbook, load_workbook
from update_sheets import *
sc = OAuth2(None, None, from_file='oauth2.json')

gm = yfa.Game(sc, 'nfl')

leagues = gm.league_ids(year = 2023)
dynasty = gm.to_league('423.l.202017')

team_keys = []
owner_names = []
tms = dynasty.teams()
for key in tms:
    team_keys.append(key)
    owner_names.append(dynasty.teams()[key]["managers"][0]["manager"]["nickname"])

league = dict(zip(owner_names, team_keys))
# print(league)
def get_rosters(week):
    # temp list for a team
    rosters = []
    team = []
    for i in range (0,len(team_keys)):
        for item in dynasty.to_team(team_keys[i]).roster(week):
            position = ""
            if item["eligible_positions"][0] == "D": 
                position = item["eligible_positions"][1]
            else:
                position = item["eligible_positions"][0]
            player_dict = {
                "name": item["name"],
                "position": position,
                "player_id": item["player_id"]
            }
            # print(player_dict)
            team.append(player_dict)
        
        team_dict = {
            "team_key": team_keys[i],
            "team_owner": owner_names[i],
            "roster": team

        }
        team = []
        rosters.append(team_dict)

    return rosters

rosters = get_rosters(17) 
print(len(rosters)) 

# [TODO] Transaction updates are way too inefficient, needs optimization
end_date = dynasty.settings()['end_date']
end_date_as_dt = datetime.strptime(dynasty.settings()['end_date'], '%Y-%m-%d')

eta = dynasty.transactions("add", 15)
etd = dynasty.transactions("drop", 15)
post_17_transactions = [x for x in eta if 
                         end_date_as_dt < datetime.strptime(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(x['timestamp']))), '%Y-%m-%d %H:%M:%S')]
extend = [x for x in eta if 
                         end_date_as_dt < datetime.strptime(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(x['timestamp']))), '%Y-%m-%d %H:%M:%S')]

post_17_transactions.extend(extend)

for x in post_17_transactions:
    # print(x["type"])
    if x["type"] == 'add':
        player_dict = {
            "name": x["players"]["0"]['player'][0][2]['name']['full'],
            "position": x["players"]["0"]['player'][0][4]['display_position'],
            "player_id": x["players"]["0"]['player'][0][1]["player_id"]
        }
        for team in rosters:
            if team['team_key'] == x["players"]["0"]['player'][1]['transaction_data'][0]['destination_team_key']:
                team["roster"].append(player_dict)

    elif x["type"] == 'drop':
        player_id = x["players"]["0"]['player'][0][1]["player_id"]

        for team in rosters: 
            if team["team_key"] == x["players"]["0"]['player'][1]['transaction_data'][0]['destination_team_key']:
                for player in team["roster"]:
                    if team["roster"]["player_id"] == player_id:
                        team["roster"].remove(player)
                                
    # else: #add + drop
# ----------------------------------------------------------------

for i in range (0, 12):
    load_team(rosters[i]["team_owner"], rosters[i]['roster'])




