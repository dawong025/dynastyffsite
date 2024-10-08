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

# def insert_roster_db(roster_obj, week, year):
#     cursor.execute('''
#         SELECT member_id FROM league_members WHERE team_key = ?
#         ''', (roster_obj.team_key,))
#     member_id = cursor.fetchone()[0]
#     for player in roster_obj.roster:
#         try:
#             cursor.execute(
#                 '''
#                     INSERT INTO Player(position, name, yahoo_player_id)
#                     VALUES
#                     (?,?,?)
#                 ''', (player.position, player.name, player.player_id)
#             )
#             dff_db.commit()
#             cursor.execute('SELECT last_insert_rowid()')
#             last_inserted_id = cursor.fetchone()[0]

#             cursor.execute(
#                 '''
#                     INSERT INTO weekly_rostered (week, year, member_id, player_id)
#                     VALUES
#                     (?,?,?,?)
#                 ''', (week, year, member_id, last_inserted_id)
#             )
#             dff_db.commit()
#         except Exception as e:
#             cursor.execute('''SELECT player_id from player where yahoo_player_id = ?''', (player.player_id,))
#             yahoo_player_id = cursor.fetchone()[0]
            
#             cursor.execute(
#                 '''
#                     INSERT INTO weekly_rostered (week, year, member_id, player_id)
#                     VALUES
#                     (?,?,?,?)
#                 ''', (week, year, member_id, yahoo_player_id)
#             )
#             dff_db.commit()

# league_years = {
#     2018: '380.l.76665',
#     2019: '390.l.33135',
#     2020: '399.l.20675',
#     2021: '406.l.78372',
#     2022: '414.l.105716',
#     2023: '423.l.202017',
#     2024: '449.l.35107'
# }

# '''
# Insert rosters per team per week/year
# '''

# # break years into ranges - e.g. 2018 through 2020 since API is rate limited
# for yr in range(2024, 2025):
#     league_week = 1

#     leagues = gm.league_ids(year = yr)
#     dynasty = gm.to_league(league_years[yr])

#     tms = dynasty.teams()

#     team_keys = []
#     owner_names = []
#     for key in tms:
#         team_keys.append(key)
#         owner_names.append(dynasty.teams()[key]["managers"][0]["manager"]["nickname"])

#     league = dict(zip(owner_names, team_keys))
#     if dynasty.current_week() < dynasty.end_week(): # For current season (in progress)
#         while (league_week <= dynasty.current_week()):
#             rosters = get_rosters(dynasty, team_keys, owner_names, league_week)

#             for i in range(0, len(owner_names)):
#                 insert_roster_db(rosters[i], league_week, yr)
#             print(f'{league_week} is done.')

#             league_week += 1
#     else: # For previous seasons
#         while (league_week <= dynasty.end_week() + 1): 
#             rosters = get_rosters(dynasty, team_keys, owner_names, league_week)

#             for i in range(0, len(owner_names)):
#                 insert_roster_db(rosters[i], league_week, yr)
#             print(f'{league_week} is done.')

#             league_week += 1

# cursor.execute('''
#                 INSERT INTO Player(position, name, yahoo_player_id)
#                 VALUES
#                 (?,?,?)
#             ''', ('LB', 'Junior Colson', 40941))
# cursor.execute('''
#                 INSERT INTO Player(position, name, yahoo_player_id)
#                 VALUES
#                 (?,?,?)
#             ''', ('RB', 'Javian Hawkins', 33731))
# cursor.execute('''
#                 INSERT INTO Player(position, name, yahoo_player_id)
#                 VALUES
#                 (?,?,?)
#             ''', ('TE', 'Michael Roberts', 30240))
# cursor.execute('''
#                 INSERT INTO Player(position, name, yahoo_player_id)
#                 VALUES
#                 (?,?,?)
#             ''', ('RB', 'Jaylen Samuels', 31135))
# cursor.execute('''
#                 INSERT INTO Player(position, name, yahoo_player_id)
#                 VALUES
#                 (?,?,?)
#             ''', ('DB', 'Karl Joseph', 29248))
cursor.execute('''
                INSERT INTO Player(position, name, yahoo_player_id)
                VALUES
                (?,?,?)
            ''', ('RB', 'Joe Williams', 30234))

dff_db.commit()


