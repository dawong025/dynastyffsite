from datetime import datetime
import time
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


print(dynasty.player_details([32734]))
