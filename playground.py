# playground.py - A file to test various commands

from datetime import datetime
import time
from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa
import json
import operator
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
            
            player_details_name = ''
            if '\'' in item["name"]:
                player_details_name = item["name"].rsplit('\'', 1)[1]
                # print(player_details_name + dynasty.player_details(player_details_name)[0]["editorial_team_full_name"])
            else:
                player_details_name = item["name"]
            player = Player(
                item["name"], 
                position, 
                item["player_id"]
                # , dynasty.player_details(player_details_name)[0]["editorial_team_full_name"]
                )
            team.append(player)
        roster = Roster(owner_names[i], team_keys[i], team)
        team = []
        rosters.append(roster)

    return rosters

rosters = get_rosters(17)
rosters.sort()
for roster in rosters:
    print(f"{roster.owner_name} - {roster.team_key}")

#Manage rosters for final post week 17 adds
end_dt_as_dt = datetime.strptime(dynasty.settings()['end_date'], '%Y-%m-%d')

raw_transactions = []
add_transactions = dynasty.transactions("add", 15)
raw_transactions.extend(add_transactions)
drop_transactions = dynasty.transactions("drop", 15)
for drop in drop_transactions:
    flag = 'n'
    for at in add_transactions:
        if drop['transaction_id'] == at['transaction_id']:
            flag = 'y'
            break
    if flag == 'n':
        raw_transactions.extend(drop_transactions)
    flag = 'n'

end_transactions = [x for x in raw_transactions if 
                        end_dt_as_dt < datetime.strptime(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(x['timestamp']))), '%Y-%m-%d %H:%M:%S')]


for x in end_transactions:
    # print(x["type"])
    if x["type"] == 'add/drop':
        # player_details_name = ''
        # if '\'' in x["players"]["0"]['player'][0][2]['name']['full']:
        #     player_details_name = x["players"]["0"]['player'][0][2]['name']['full'].rsplit('\'', 1)[1]
        # else:
        #     player_details_name = x["players"]["0"]['player'][0][2]['name']['full']
        print(x["players"]["0"]['player'][0])
        
for player in rosters[1].roster:
    print(player.position)
# load_team(rosters[1].owner_name, rosters[1].roster)
# Initial roster load
# for i in range(0, len(owner_names)):
#     load_team(rosters[i].owner_name, rosters[i].roster)               
