from datetime import datetime
import time
from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa
from openpyxl import Workbook, load_workbook
from update_sheets import *
from roster import *
from update_sheets import clear_sheet
import json

sc = OAuth2(None, None, from_file='oauth2.json')
gm = yfa.Game(sc, 'nfl')

leagues = gm.league_ids(year = 2023)
print(leagues)
dynasty = gm.to_league('423.l.202017')

league_years = {
    2018: '380.l.76665',
    2019: '390.l.33135',
    2020: '399.l.20675',
    2021: '406.l.78372',
    2022: '414.l.105716',
    2023: '423.l.202017'
}

tms = dynasty.teams()

team_keys = []
owner_names = []
for key in tms:
    team_keys.append(key)
    owner_names.append(dynasty.teams()[key]["managers"][0]["manager"]["nickname"])

league = dict(zip(owner_names, team_keys))
print(league)

clear_sheet('dff.xlsx', 'Roster Template') 

