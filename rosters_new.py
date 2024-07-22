
from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa
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

rosters = get_rosters(dynasty, team_keys, owner_names, 18)

for roster in rosters:
    for player in roster.roster:
        print(player)

    print('-------------------------------')

# Initial roster load
# for i in range(0, len(owner_names)):
#     load_team(rosters[i].owner_name, rosters[i].roster)    

# clear_sheet('dff.xlsx', 'S8 End Roster')           
