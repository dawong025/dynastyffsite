import sqlite3
from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa
from update_sheets import *
from roster import *
sc = OAuth2(None, None, from_file='oauth2.json')
gm = yfa.Game(sc, 'nfl')
import time

dff_db = sqlite3.connect("dynasty-db.db")

cursor = dff_db.cursor()

league_years = {
    2018: '380.l.76665',
    2019: '390.l.33135',
    2020: '399.l.20675',
    2021: '406.l.78372',
    2022: '414.l.105716',
    2023: '423.l.202017',
    2024: '449.l.35107'
}

'''
Insert league members based on league years
'''
# for yr in range(2018, 2025):
#     leagues = gm.league_ids(year = yr)
#     dynasty = gm.to_league(league_years[yr])

#     tms = dynasty.teams()

#     team_keys = []
#     owner_names = []
#     league = {}
#     for key in tms:
#         league[dynasty.teams()[key]["managers"][0]["manager"]["nickname"]] = key

#     for lg_member in league:
#         try:
#             cursor.execute('''
#                            INSERT INTO league_members (year, team_key, member_name)
#                            VALUES
#                            (?, ?, ?)
#                            ''',
#                            (yr, league[lg_member], lg_member))
#             dff_db.commit()
#         except Exception as e:
#             continue
# # Data patching:  '--hidden--' case for Leslie 2018
# cursor.execute('''
#                UPDATE league_members
#                SET member_name = 'Leslie'
#                WHERE member_name = '--hidden--' and year = 2018
               
#                ''')
# dff_db.commit()

# # Data patching: For 2017 season on NFL Fantasy, needed for 2017 rookie draft picks insert
# cursor.execute(
#     '''
#         INSERT INTO league_members (team_key, member_name, year)
#         VALUES
#         (1,'Darren' , 2017),
#         (2, 'Jacob' , 2017),
#         (3, 'Christopher' , 2017),
#         (4,'Nicholas' , 2017),
#         (5,'Terence' , 2017),
#         (6,'Johnathan Alexander' , 2017),
#         (7, 'Elston' , 2017),
#         (8,'Johnny' , 2017),
#         (9,'Henry' , 2017),
#         (10,'Eric' , 2017),
#         (11,'Mags' , 2017),
#         (12,'Kelvin' , 2017)
#     '''
# )
# dff_db.commit()